#!/usr/bin/env python3
"""Discover, generate, and verify the repository's published skill inventory.

The plugin directories and their two manifests are the source of truth.  All
checked-in indexes are deterministic outputs of this module and use only the
Python standard library.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable


SCHEMA_VERSION = 1
PLUGIN_DIR_NAME = "plugins"
CLAUDE_MANIFEST = Path(".claude-plugin/plugin.json")
CODEX_MANIFEST = Path(".codex-plugin/plugin.json")
SKILLS_DIR = Path("skills")
DEPRECATED_SKILLS = frozenset({"article-visual-planner", "cover-pixel-avatar"})
CONFIRMED_WITH_DOCS = frozenset(
    {
        "cover-3d-eye-with-docs",
        "cover-cream-orange-knowledge-poster-with-docs",
        "cover-light-product-with-docs",
        "cover-sketch-knowledge-poster-with-docs",
    }
)

GENERATED_DIR = Path("generated")
REGISTRY_PATH = GENERATED_DIR / "skill-registry.json"
INSTALL_INDEX_PATH = GENERATED_DIR / "install-index.json"
INSTALL_INDEX_SHELL_PATH = GENERATED_DIR / "install-index.sh"
COVER_TIPS_STYLES_PATH = GENERATED_DIR / "cover-tips-styles.json"
STYLE_SPEC_PATH = Path("style-specs/with-docs.json")
STYLE_INDEX_PATH = GENERATED_DIR / "with-docs-style-index.json"
CLAUDE_MARKETPLACE_PATH = Path(".claude-plugin/marketplace.json")
CODEX_MARKETPLACE_PATH = Path(".agents/plugins/marketplace.json")
COVER_TIPS_SKILL_PATH = Path("plugins/cover-tips/skills/cover-tips/SKILL.md")
COVER_TIPS_ROUTES_BEGIN = "<!-- BEGIN GENERATED COVER-TIPS ROUTES -->"
COVER_TIPS_ROUTES_END = "<!-- END GENERATED COVER-TIPS ROUTES -->"
STYLE_PROJECTION_BEGIN = "<!-- BEGIN GENERATED STYLE SPEC: {base_skill} -->"
STYLE_PROJECTION_END = "<!-- END GENERATED STYLE SPEC: {base_skill} -->"
STYLE_PROJECTION_PATTERN = re.compile(
    r"\n<!-- BEGIN GENERATED STYLE SPEC: [^>]+ -->.*?"
    r"<!-- END GENERATED STYLE SPEC: [^>]+ -->\n?",
    re.DOTALL,
)

MARKETPLACE_NAME = "cover-prompt-skills"
MARKETPLACE_OWNER = {"name": "imartinstudio"}
CODEX_MARKETPLACE_INTERFACE = {
    "displayName": "Cover Prompt Skills",
    "shortDescription": "Cover-first visual prompt skills for covers, posters, and article visual planning",
    "developerName": "imartinstudio",
    "category": "Design",
}
SKILL_NAME_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


class RegistryError(Exception):
    """Raised for malformed plugin inventory input."""


def relative_path(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RegistryError(f"invalid JSON: {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise RegistryError(f"manifest must contain a JSON object: {path}")
    return value


def parse_frontmatter(path: Path) -> dict[str, str]:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        raise RegistryError(f"cannot read skill: {path}: {exc}") from exc

    if not lines or lines[0].strip() != "---":
        raise RegistryError(f"SKILL.md must start with YAML frontmatter: {path}")

    end = next(
        (index for index, line in enumerate(lines[1:], start=1) if line.strip() == "---"),
        None,
    )
    if end is None:
        raise RegistryError(f"SKILL.md frontmatter is not closed: {path}")

    fields: dict[str, str] = {}
    for line in lines[1:end]:
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        fields[key.strip()] = value.strip().strip("\"'")

    for required in ("name", "description"):
        if not fields.get(required):
            raise RegistryError(f"SKILL.md frontmatter needs {required}: {path}")
    return fields


def sha256_file(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError as exc:
        raise RegistryError(f"cannot hash artifact: {path}: {exc}") from exc


def normalized_style_artifact_sha256(path: Path) -> str:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise RegistryError(f"cannot hash artifact: {path}: {exc}") from exc
    normalized = STYLE_PROJECTION_PATTERN.sub("", text)
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def render_generated_block(begin: str, end: str, body: str) -> str:
    return "\n".join((begin, body, end))


def extract_generated_block(text: str, begin: str, end: str, path: Path) -> str:
    if text.count(begin) != 1 or text.count(end) != 1:
        raise RegistryError(
            f"generated block markers must occur exactly once: {path}"
        )
    start = text.index(begin)
    end_start = text.index(end)
    if end_start < start:
        raise RegistryError(f"generated block markers are out of order: {path}")
    end_position = end_start + len(end)
    return text[start:end_position]


def replace_generated_block(
    text: str,
    begin: str,
    end: str,
    expected: str,
    path: Path,
    *,
    allow_append: bool,
) -> str:
    begin_count = text.count(begin)
    end_count = text.count(end)
    if begin_count == 0 and end_count == 0 and allow_append:
        return f"{text.rstrip()}\n\n{expected}\n"
    actual = extract_generated_block(text, begin, end, path)
    start = text.index(begin)
    end_position = start + len(actual)
    return text[:start] + expected + text[end_position:]


def load_style_spec(root: Path) -> dict[str, Any]:
    path = root / STYLE_SPEC_PATH
    if not path.is_file():
        raise RegistryError(f"style spec is missing: {relative_path(path, root)}")
    spec = read_json(path)
    if spec.get("schema_version") != SCHEMA_VERSION:
        raise RegistryError(f"unsupported style spec schema: {relative_path(path, root)}")
    if spec.get("name") != "cover-with-docs-style-spec":
        raise RegistryError(f"unexpected style spec name: {relative_path(path, root)}")

    styles = spec.get("styles")
    if not isinstance(styles, list) or not styles:
        raise RegistryError(f"style spec styles must be a non-empty list: {relative_path(path, root)}")

    expected_with_docs = {
        base: f"{base}-with-docs" for base in sorted(
            name.removesuffix("-with-docs") for name in CONFIRMED_WITH_DOCS
        )
    }
    actual_bases: set[str] = set()
    for style in styles:
        if not isinstance(style, dict):
            raise RegistryError(f"style spec entries must be objects: {relative_path(path, root)}")
        base = style.get("base_skill")
        with_docs = style.get("with_docs_skill")
        if not isinstance(base, str) or not isinstance(with_docs, str):
            raise RegistryError(f"style spec entries need base_skill and with_docs_skill: {relative_path(path, root)}")
        if base in actual_bases:
            raise RegistryError(f"duplicate style spec entry: {base}")
        actual_bases.add(base)
        if expected_with_docs.get(base) != with_docs:
            raise RegistryError(f"style spec pairing is not confirmed: {base} -> {with_docs}")
        for field in (
            "base_skill_path",
            "with_docs_skill_path",
            "visual_system",
            "article_visual_system",
            "base_rule_markers",
            "with_docs_rule_markers",
            "artifact_sha256",
        ):
            if not style.get(field):
                raise RegistryError(f"style spec entry {base} needs {field}")
        for marker_field in ("base_rule_markers", "with_docs_rule_markers"):
            markers = style[marker_field]
            if not isinstance(markers, list) or not all(isinstance(marker, str) and marker for marker in markers):
                raise RegistryError(f"style spec entry {base} has invalid {marker_field}")
        hashes = style["artifact_sha256"]
        if not isinstance(hashes, dict):
            raise RegistryError(f"style spec entry {base} has invalid artifact_sha256")
        for artifact in ("base_skill", "with_docs_skill"):
            digest = hashes.get(artifact)
            if not isinstance(digest, str) or len(digest) != 64:
                raise RegistryError(f"style spec entry {base} has invalid {artifact} hash")
            try:
                int(digest, 16)
            except ValueError as exc:
                raise RegistryError(f"style spec entry {base} has invalid {artifact} hash") from exc

    if actual_bases != set(expected_with_docs):
        missing = sorted(set(expected_with_docs) - actual_bases)
        extra = sorted(actual_bases - set(expected_with_docs))
        raise RegistryError(f"style spec pair set mismatch: missing={missing}, extra={extra}")
    return spec


def render_cover_tips_routes(registry: dict[str, Any]) -> str:
    plugins = {plugin["name"]: plugin for plugin in registry["plugins"]}
    with_docs_by_base = {
        pair["base"]: pair["with_docs"] for pair in registry["with_docs_pairs"]
    }
    lines = [
        COVER_TIPS_ROUTES_BEGIN,
        "| Display name | Single-cover route | Article-package route |",
        "| --- | --- | --- |",
    ]
    for base in registry["base_skills"]:
        article_route = with_docs_by_base.get(base)
        article_cell = f"`{article_route}`" if article_route else "—"
        lines.append(
            f"| {plugins[base]['display_name']} | `{base}` | {article_cell} |"
        )
    lines.append(COVER_TIPS_ROUTES_END)
    return "\n".join(lines)


def render_style_spec_projection(style: dict[str, Any], target: str) -> str:
    payload: dict[str, Any] = {
        "base_skill": style["base_skill"],
        "with_docs_skill": style["with_docs_skill"],
        "visual_system": style["visual_system"],
    }
    if target == "with-docs":
        payload["article_visual_system"] = style["article_visual_system"]
    body = "\n".join(
        (
            "<!-- Generated from style-specs/with-docs.json; do not edit by hand. -->",
            "```json",
            json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True),
            "```",
        )
    )
    return render_generated_block(
        STYLE_PROJECTION_BEGIN.format(base_skill=style["base_skill"]),
        STYLE_PROJECTION_END.format(base_skill=style["base_skill"]),
        body,
    )


def synchronize_generated_skill_blocks(root: Path, registry: dict[str, Any]) -> None:
    spec = load_style_spec(root)
    route_path = root / COVER_TIPS_SKILL_PATH
    try:
        route_text = route_path.read_text(encoding="utf-8")
    except OSError as exc:
        raise RegistryError(f"cannot read CoverTips skill: {route_path}: {exc}") from exc
    route_block = render_cover_tips_routes(registry)
    route_updated = replace_generated_block(
        route_text,
        COVER_TIPS_ROUTES_BEGIN,
        COVER_TIPS_ROUTES_END,
        route_block,
        route_path,
        allow_append=False,
    )
    if route_updated != route_text:
        route_path.write_text(route_updated, encoding="utf-8")

    plugins = {plugin["name"]: plugin for plugin in registry["plugins"]}
    for style in spec["styles"]:
        for target, skill_name in (
            ("base", style["base_skill"]),
            ("with-docs", style["with_docs_skill"]),
        ):
            plugin = plugins.get(skill_name)
            if plugin is None:
                raise RegistryError(f"style spec references undiscovered skill: {skill_name}")
            skill_path = root / plugin["skill_path"]
            try:
                skill_text = skill_path.read_text(encoding="utf-8")
            except OSError as exc:
                raise RegistryError(f"cannot read skill: {skill_path}: {exc}") from exc
            projection = render_style_spec_projection(style, target)
            begin = STYLE_PROJECTION_BEGIN.format(base_skill=style["base_skill"])
            end = STYLE_PROJECTION_END.format(base_skill=style["base_skill"])
            updated = replace_generated_block(
                skill_text,
                begin,
                end,
                projection,
                skill_path,
                allow_append=True,
            )
            if updated != skill_text:
                skill_path.write_text(updated, encoding="utf-8")


def validate_cover_tips_routes(root: Path, registry: dict[str, Any]) -> list[str]:
    path = root / COVER_TIPS_SKILL_PATH
    try:
        text = path.read_text(encoding="utf-8")
        actual = extract_generated_block(
            text, COVER_TIPS_ROUTES_BEGIN, COVER_TIPS_ROUTES_END, path
        )
    except (OSError, RegistryError) as exc:
        return [str(exc)]
    expected = render_cover_tips_routes(registry)
    if actual != expected:
        return [f"CoverTips generated route table drifted: {relative_path(path, root)}"]
    return []


def build_style_index(root: Path, registry: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    try:
        spec = load_style_spec(root)
    except RegistryError as exc:
        return {}, [str(exc)]

    plugins = {plugin["name"]: plugin for plugin in registry["plugins"]}
    errors: list[str] = []
    indexed_styles: list[dict[str, Any]] = []
    for style in sorted(spec["styles"], key=lambda item: item["base_skill"]):
        base = style["base_skill"]
        with_docs = style["with_docs_skill"]
        base_plugin = plugins.get(base)
        with_docs_plugin = plugins.get(with_docs)
        if base_plugin is None or with_docs_plugin is None:
            errors.append(f"style spec references undiscovered skills: {base}, {with_docs}")
            continue

        expected_base_path = base_plugin["skill_path"]
        expected_with_docs_path = with_docs_plugin["skill_path"]
        if style["base_skill_path"] != expected_base_path:
            errors.append(f"style spec base path mismatch: {base}")
        if style["with_docs_skill_path"] != expected_with_docs_path:
            errors.append(f"style spec with-docs path mismatch: {with_docs}")

        base_path = root / expected_base_path
        with_docs_path = root / expected_with_docs_path
        try:
            base_text = base_path.read_text(encoding="utf-8")
            with_docs_text = with_docs_path.read_text(encoding="utf-8")
            actual_base_hash = normalized_style_artifact_sha256(base_path)
            actual_with_docs_hash = normalized_style_artifact_sha256(with_docs_path)
        except (OSError, RegistryError) as exc:
            errors.append(str(exc))
            continue

        expected_hashes = style["artifact_sha256"]
        if actual_base_hash != expected_hashes["base_skill"]:
            errors.append(f"base SKILL.md drifted from style spec: {base}")
        if actual_with_docs_hash != expected_hashes["with_docs_skill"]:
            errors.append(f"with-docs SKILL.md drifted from style spec: {with_docs}")

        for marker in style["base_rule_markers"]:
            if marker not in base_text:
                errors.append(f"base style rule marker missing for {base}: {marker}")
        for marker in style["with_docs_rule_markers"]:
            if marker not in with_docs_text:
                errors.append(f"with-docs rule marker missing for {with_docs}: {marker}")

        for target, skill_name, skill_text in (
            ("base", base, base_text),
            ("with-docs", with_docs, with_docs_text),
        ):
            expected_projection = render_style_spec_projection(style, target)
            begin = STYLE_PROJECTION_BEGIN.format(base_skill=base)
            end = STYLE_PROJECTION_END.format(base_skill=base)
            try:
                actual_projection = extract_generated_block(
                    skill_text, begin, end, root / (expected_base_path if target == "base" else expected_with_docs_path)
                )
            except RegistryError as exc:
                errors.append(str(exc))
                continue
            if actual_projection != expected_projection:
                errors.append(
                    f"style spec projection drifted for {skill_name}: "
                    f"{STYLE_SPEC_PATH.as_posix()} does not match generated block"
                )

        indexed_styles.append(
            {
                "base_skill": base,
                "with_docs_skill": with_docs,
                "base_skill_path": expected_base_path,
                "with_docs_skill_path": expected_with_docs_path,
                "base_skill_sha256": actual_base_hash,
                "with_docs_skill_sha256": actual_with_docs_hash,
                "visual_system": style["visual_system"],
                "article_visual_system": style["article_visual_system"],
                "base_rule_markers": style["base_rule_markers"],
                "with_docs_rule_markers": style["with_docs_rule_markers"],
            }
        )

    try:
        spec_hash = sha256_file(root / STYLE_SPEC_PATH)
    except RegistryError as exc:
        errors.append(str(exc))
        spec_hash = ""
    return {
        "schema_version": SCHEMA_VERSION,
        "source_spec": STYLE_SPEC_PATH.as_posix(),
        "source_spec_sha256": spec_hash,
        "styles": indexed_styles,
    }, errors


def require_string(value: Any, field: str, path: Path) -> str:
    if not isinstance(value, str) or not value.strip():
        raise RegistryError(f"{field} must be a non-empty string: {path}")
    return value


def require_skill_name(value: Any, field: str, path: Path) -> str:
    name = require_string(value, field, path)
    if SKILL_NAME_PATTERN.fullmatch(name) is None:
        raise RegistryError(f"invalid skill name for {field}: {name!r}: {path}")
    return name


def contains_files(path: Path) -> bool:
    try:
        return any(
            child.is_file() or (child.is_dir() and contains_files(child))
            for child in path.iterdir()
        )
    except OSError as exc:
        raise RegistryError(f"cannot inspect directory: {path}: {exc}") from exc


def iter_plugin_directories(root: Path) -> Iterable[Path]:
    plugins_dir = root / PLUGIN_DIR_NAME
    if not plugins_dir.is_dir():
        raise RegistryError(f"plugin directory is missing: {plugins_dir}")

    for path in sorted(plugins_dir.iterdir(), key=lambda item: item.name):
        if not path.is_dir() or path.name in DEPRECATED_SKILLS:
            continue
        if contains_files(path):
            yield path


def validate_deprecated_directories(root: Path) -> list[str]:
    errors: list[str] = []
    for name in sorted(DEPRECATED_SKILLS):
        path = root / PLUGIN_DIR_NAME / name
        if not path.is_dir():
            continue
        try:
            if contains_files(path):
                errors.append(
                    f"deprecated plugin directory must be empty or absent: {relative_path(path, root)}"
                )
        except RegistryError as exc:
            errors.append(str(exc))
    return errors


def inspect_plugin(plugin_dir: Path, root: Path) -> tuple[dict[str, Any] | None, list[str]]:
    errors: list[str] = []
    directory_name = plugin_dir.name
    try:
        require_skill_name(directory_name, "plugin directory name", plugin_dir)
    except RegistryError as exc:
        errors.append(str(exc))
    claude_path = plugin_dir / CLAUDE_MANIFEST
    codex_path = plugin_dir / CODEX_MANIFEST

    if not claude_path.is_file():
        errors.append(f"missing Claude manifest: {relative_path(claude_path, root)}")
    if not codex_path.is_file():
        errors.append(f"missing Codex manifest: {relative_path(codex_path, root)}")
    if errors:
        return None, errors

    try:
        claude = read_json(claude_path)
        codex = read_json(codex_path)
    except RegistryError as exc:
        return None, [str(exc)]

    try:
        claude_name = require_skill_name(claude.get("name"), "Claude manifest name", claude_path)
        codex_name = require_skill_name(codex.get("name"), "Codex manifest name", codex_path)
        claude_display_name = require_string(
            claude.get("displayName"), "Claude manifest displayName", claude_path
        )
        claude_description = require_string(
            claude.get("description"), "Claude manifest description", claude_path
        )
        codex_skills = require_string(codex.get("skills"), "Codex manifest skills", codex_path)
        codex_interface = codex.get("interface")
        if not isinstance(codex_interface, dict):
            raise RegistryError(f"Codex manifest interface must be an object: {codex_path}")
        codex_display_name = require_string(
            codex_interface.get("displayName"),
            "Codex interface displayName",
            codex_path,
        )
    except RegistryError as exc:
        errors.append(str(exc))
        return None, errors

    if claude_name != directory_name:
        errors.append(
            f"directory name {directory_name!r} does not match Claude manifest name {claude_name!r}"
        )
    if codex_name != directory_name:
        errors.append(
            f"directory name {directory_name!r} does not match Codex manifest name {codex_name!r}"
        )
    if codex_skills != "./skills/":
        errors.append(f"Codex manifest skills must be './skills/': {relative_path(codex_path, root)}")
    if claude_display_name != codex_display_name:
        errors.append(
            f"manifest displayName mismatch for {directory_name!r}: "
            f"Claude={claude_display_name!r}, Codex={codex_display_name!r}"
        )

    skills_dir = plugin_dir / SKILLS_DIR
    skill_dirs = sorted(
        (path for path in skills_dir.iterdir() if path.is_dir()), key=lambda item: item.name
    ) if skills_dir.is_dir() else []
    if not skills_dir.is_dir():
        errors.append(f"missing skills directory: {relative_path(skills_dir, root)}")
    if len(skill_dirs) != 1:
        errors.append(
            f"expected exactly one skill directory under {relative_path(skills_dir, root)}, "
            f"found {len(skill_dirs)}"
        )

    skill_dir = skill_dirs[0] if len(skill_dirs) == 1 else skills_dir / directory_name
    skill_path = skill_dir / "SKILL.md"
    if not skill_path.is_file():
        errors.append(f"missing SKILL.md: {relative_path(skill_path, root)}")
        frontmatter: dict[str, str] = {}
    else:
        try:
            frontmatter = parse_frontmatter(skill_path)
        except RegistryError as exc:
            errors.append(str(exc))
            frontmatter = {}

    skill_directory_name = skill_dir.name
    frontmatter_name = frontmatter.get("name", "")
    try:
        require_skill_name(skill_directory_name, "skill directory name", skill_dir)
    except RegistryError as exc:
        errors.append(str(exc))
    try:
        require_skill_name(frontmatter_name, "SKILL.md frontmatter name", skill_path)
    except RegistryError as exc:
        errors.append(str(exc))
    if skill_directory_name != directory_name:
        errors.append(
            f"skill directory name {skill_directory_name!r} does not match plugin {directory_name!r}"
        )
    if frontmatter_name != directory_name:
        errors.append(
            f"SKILL.md frontmatter name {frontmatter_name!r} does not match plugin {directory_name!r}"
        )

    if errors:
        return None, errors

    if directory_name.endswith("-with-docs"):
        kind = "with-docs"
    elif directory_name == "cover-tips":
        kind = "router"
    else:
        kind = "base"

    plugin = {
        "name": directory_name,
        "kind": kind,
        "path": relative_path(plugin_dir, root),
        "skill_path": relative_path(skill_path, root),
        "claude_manifest_path": relative_path(claude_path, root),
        "codex_manifest_path": relative_path(codex_path, root),
        "directory_name": directory_name,
        "claude_manifest_name": claude_name,
        "codex_manifest_name": codex_name,
        "skill_directory_name": skill_directory_name,
        "frontmatter_name": frontmatter_name,
        "display_name": claude_display_name,
        "description": claude_description,
        "version": require_string(claude.get("version"), "Claude manifest version", claude_path),
    }
    return plugin, []


def discover(root: Path) -> tuple[dict[str, Any], list[str]]:
    errors = validate_deprecated_directories(root)
    plugins: list[dict[str, Any]] = []
    seen_names: set[str] = set()

    try:
        plugin_dirs = list(iter_plugin_directories(root))
    except RegistryError as exc:
        return {"schema_version": SCHEMA_VERSION, "plugins": []}, [str(exc)]

    for plugin_dir in plugin_dirs:
        plugin, plugin_errors = inspect_plugin(plugin_dir, root)
        errors.extend(plugin_errors)
        if plugin is None:
            continue
        name = plugin["name"]
        if name in seen_names:
            errors.append(f"duplicate plugin name: {name}")
            continue
        seen_names.add(name)
        plugins.append(plugin)

    plugins.sort(key=lambda item: item["name"])
    names = {plugin["name"] for plugin in plugins}
    base_skills = sorted(
        plugin["name"] for plugin in plugins if plugin["kind"] == "base"
    )
    with_docs_skills = sorted(
        plugin["name"] for plugin in plugins if plugin["kind"] == "with-docs"
    )
    pairs: list[dict[str, str]] = []
    for with_docs in with_docs_skills:
        base = with_docs.removesuffix("-with-docs")
        if base not in names:
            errors.append(f"with-docs skill has no base skill: {with_docs} -> {base}")
            continue
        pairs.append({"base": base, "with_docs": with_docs})
    pairs.sort(key=lambda item: item["with_docs"])

    actual_with_docs = set(with_docs_skills)
    unexpected_with_docs = sorted(actual_with_docs - CONFIRMED_WITH_DOCS)
    missing_with_docs = sorted(CONFIRMED_WITH_DOCS - actual_with_docs)
    for name in unexpected_with_docs:
        errors.append(f"unconfirmed with-docs skill is not allowed: {name}")
    for name in missing_with_docs:
        errors.append(f"confirmed with-docs skill is missing: {name}")

    article_visual_styles = sorted(pair["base"] for pair in pairs)
    all_skills = sorted(names)
    install_index = {
        "all_skills": all_skills,
        "standalone_skills": all_skills,
        "base_skills": base_skills,
        "with_docs_skills": with_docs_skills,
        "cover_tips": "cover-tips" if "cover-tips" in names else None,
    }
    registry = {
        "schema_version": SCHEMA_VERSION,
        "source": {
            "plugins_directory": PLUGIN_DIR_NAME,
            "manifests": [CLAUDE_MANIFEST.as_posix(), CODEX_MANIFEST.as_posix()],
            "skill_file": "skills/<name>/SKILL.md",
            "with_docs_style_spec": STYLE_SPEC_PATH.as_posix(),
        },
        "plugins": plugins,
        "base_skills": base_skills,
        "with_docs_skills": with_docs_skills,
        "with_docs_pairs": pairs,
        "article_visual_styles": article_visual_styles,
        "cover_tips_styles": base_skills,
        "install_index": install_index,
        "excluded_skills": sorted(DEPRECATED_SKILLS),
    }
    return registry, errors


def install_index(registry: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "all_skills": registry["install_index"]["all_skills"],
        "standalone_skills": registry["install_index"]["standalone_skills"],
        "base_skills": registry["base_skills"],
        "with_docs_skills": registry["with_docs_skills"],
        "cover_tips": registry["install_index"]["cover_tips"],
    }


def cover_tips_styles(registry: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "cover_styles": registry["cover_tips_styles"],
        "article_visual_styles": registry["article_visual_styles"],
        "with_docs_skills": registry["with_docs_skills"],
    }


def claude_marketplace(registry: dict[str, Any]) -> dict[str, Any]:
    return {
        "name": MARKETPLACE_NAME,
        "owner": MARKETPLACE_OWNER,
        "plugins": [
            {
                "name": plugin["name"],
                "source": f"./plugins/{plugin['name']}",
                "description": plugin["description"],
            }
            for plugin in registry["plugins"]
        ],
    }


def codex_marketplace(registry: dict[str, Any]) -> dict[str, Any]:
    return {
        "name": MARKETPLACE_NAME,
        "interface": CODEX_MARKETPLACE_INTERFACE,
        "plugins": [
            {
                "name": plugin["name"],
                "source": {"source": "local", "path": f"./plugins/{plugin['name']}"},
                "policy": {
                    "installation": "AVAILABLE",
                    "authentication": "ON_INSTALL",
                },
                "category": "Design",
            }
            for plugin in registry["plugins"]
        ],
    }


def shell_install_index(registry: dict[str, Any]) -> str:
    lines = [
        "#!/usr/bin/env bash",
        "# Generated by scripts/skill_registry.py; do not edit by hand.",
        "# shellcheck shell=bash",
        "",
    ]
    for variable, values in (
        ("ALL_SKILLS", registry["install_index"]["all_skills"]),
        ("BASE_SKILLS", registry["base_skills"]),
        ("WITH_DOCS_SKILLS", registry["with_docs_skills"]),
    ):
        for value in values:
            require_skill_name(value, f"generated {variable} value", Path(INSTALL_INDEX_SHELL_PATH))
        lines.append(f"{variable}=(")
        lines.extend(f'  "{value}"' for value in values)
        lines.append(")")
        lines.append("")
    lines.append('COVER_TIPS_SKILL="cover-tips"')
    lines.append("")
    return "\n".join(lines)


def generated_files(
    root: Path, registry: dict[str, Any], style_index: dict[str, Any]
) -> dict[Path, bytes]:
    def json_bytes(value: Any) -> bytes:
        return (
            json.dumps(value, ensure_ascii=False, indent=2, sort_keys=False) + "\n"
        ).encode("utf-8")

    return {
        root / REGISTRY_PATH: json_bytes(registry),
        root / INSTALL_INDEX_PATH: json_bytes(install_index(registry)),
        root / COVER_TIPS_STYLES_PATH: json_bytes(cover_tips_styles(registry)),
        root / STYLE_INDEX_PATH: json_bytes(style_index),
        root / INSTALL_INDEX_SHELL_PATH: shell_install_index(registry).encode("utf-8"),
        root / CLAUDE_MARKETPLACE_PATH: json_bytes(claude_marketplace(registry)),
        root / CODEX_MARKETPLACE_PATH: json_bytes(codex_marketplace(registry)),
    }


def print_json(value: Any) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=False))


def print_errors(errors: list[str]) -> None:
    for error in errors:
        print(f"error: {error}", file=sys.stderr)


def command_discover(root: Path) -> int:
    registry, errors = discover(root)
    print_json(registry)
    if errors:
        print_errors(errors)
        return 1
    return 0


def command_generate(root: Path) -> int:
    registry, errors = discover(root)
    if errors:
        print_errors(errors)
        return 1
    try:
        synchronize_generated_skill_blocks(root, registry)
    except RegistryError as exc:
        print_errors([str(exc)])
        return 1
    style_index, style_errors = build_style_index(root, registry)
    errors.extend(style_errors)
    if errors:
        print_errors(errors)
        return 1
    for path, contents in generated_files(root, registry, style_index).items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(contents)
        print(f"generated {relative_path(path, root)}")
    return 0


def command_check(root: Path) -> int:
    registry, errors = discover(root)
    errors.extend(validate_cover_tips_routes(root, registry))
    style_index, style_errors = build_style_index(root, registry)
    errors.extend(style_errors)
    if errors:
        print_errors(errors)
        return 1

    mismatches: list[str] = []
    for path, expected in generated_files(root, registry, style_index).items():
        if not path.is_file():
            mismatches.append(f"missing generated file: {relative_path(path, root)}")
            continue
        if path.read_bytes() != expected:
            mismatches.append(f"generated file is stale: {relative_path(path, root)}")

    if mismatches:
        print_errors(mismatches)
        return 1
    print(f"registry check passed: {len(registry['plugins'])} plugins")
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("discover", "generate", "check"))
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root (defaults to the current repository)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    root = args.root.resolve()
    if args.command == "discover":
        return command_discover(root)
    if args.command == "generate":
        return command_generate(root)
    return command_check(root)


if __name__ == "__main__":
    raise SystemExit(main())
