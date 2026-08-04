import json
import hashlib
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_COMMAND = ROOT / "scripts" / "skill_registry.py"

EXPECTED_BASE_SKILLS = {
    "cover-3d-eye",
    "cover-black-white-minimal",
    "cover-budapest-poster",
    "cover-cream-orange-knowledge-poster",
    "cover-editorial-collage",
    "cover-giant-perspective-poster",
    "cover-light-product",
    "cover-mckinsey-briefing-style",
    "cover-midnight-studio",
    "cover-sketch-knowledge-poster",
    "cover-tea-oriental",
    "cover-trendy-color-poster",
}
EXPECTED_WITH_DOCS = {
    "cover-3d-eye-with-docs",
    "cover-cream-orange-knowledge-poster-with-docs",
    "cover-light-product-with-docs",
    "cover-sketch-knowledge-poster-with-docs",
}
EXPECTED_ALL_SKILLS = EXPECTED_BASE_SKILLS | EXPECTED_WITH_DOCS | {"cover-tips"}
DEPRECATED_SKILLS = {"article-visual-planner", "cover-pixel-avatar"}
EXPECTED_STYLE_PAIRS = {
    "cover-3d-eye": "cover-3d-eye-with-docs",
    "cover-cream-orange-knowledge-poster": "cover-cream-orange-knowledge-poster-with-docs",
    "cover-light-product": "cover-light-product-with-docs",
    "cover-sketch-knowledge-poster": "cover-sketch-knowledge-poster-with-docs",
}


class SkillRegistryTests(unittest.TestCase):
    def run_registry(self, *arguments):
        result = subprocess.run(
            [sys.executable, str(REGISTRY_COMMAND), *arguments],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(
            result.returncode,
            0,
            msg=f"registry command failed: {result.args}\n{result.stdout}\n{result.stderr}",
        )
        return result

    def run_registry_expect_failure(self, *arguments):
        result = subprocess.run(
            [sys.executable, str(REGISTRY_COMMAND), *arguments],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(
            result.returncode,
            0,
            msg=f"registry command unexpectedly passed: {result.args}\n{result.stdout}\n{result.stderr}",
        )
        return result

    def load_json(self, path):
        self.assertTrue(path.is_file(), msg=f"generated file is missing: {path}")
        return json.loads(path.read_text(encoding="utf-8"))

    def sha256(self, path):
        return hashlib.sha256(path.read_bytes()).hexdigest()

    def run_local_installer(self, target, *arguments):
        home = target.parent / "home"
        home.mkdir(exist_ok=True)
        environment = os.environ.copy()
        environment.update(
            {
                "COVER_SKILLS_TARGET": str(target),
                "COVER_SKILLS_BACKUP_DIR": str(target.parent / "backup"),
                "HOME": str(home),
            }
        )
        return subprocess.run(
            ["bash", str(ROOT / "scripts" / "install.sh"), *arguments],
            cwd=ROOT,
            env=environment,
            capture_output=True,
            text=True,
        )

    def run_remote_installer_with_fake_curl(self, temporary_root, index_text):
        index_path = temporary_root / "remote-install-index.sh"
        index_path.write_text(index_text, encoding="utf-8")
        fake_bin = temporary_root / "bin"
        fake_bin.mkdir()
        fake_curl = fake_bin / "curl"
        fake_curl.write_text(
            "#!/usr/bin/env python3\n"
            "import shutil\n"
            "import sys\n"
            "from pathlib import Path\n"
            f"source = Path({str(index_path)!r})\n"
            "args = sys.argv[1:]\n"
            "output = Path(args[args.index('-o') + 1])\n"
            "shutil.copyfile(source, output)\n",
            encoding="utf-8",
        )
        fake_curl.chmod(0o755)

        target = temporary_root / "target"
        temp_dir = temporary_root / "tmp"
        temp_dir.mkdir()
        home = temporary_root / "home"
        home.mkdir()
        sentinel = temporary_root / "sentinel"
        environment = os.environ.copy()
        environment.update(
            {
                "COVER_SKILLS_TARGET": str(target),
                "COVER_SKILLS_BACKUP_DIR": str(temporary_root / "backup"),
                "HOME": str(home),
                "TMPDIR": str(temp_dir),
                "PATH": f"{fake_bin}{os.pathsep}{environment['PATH']}",
                "COVER_SKILLS_TEST_SENTINEL": str(sentinel),
            }
        )
        return subprocess.run(
            ["bash", str(ROOT / "install.sh"), "cover-tips"],
            cwd=temporary_root,
            env=environment,
            capture_output=True,
            text=True,
        ), sentinel

    def test_inventory_is_discovered_from_real_plugin_directories(self):
        payload = json.loads(self.run_registry("discover").stdout)
        names = {plugin["name"] for plugin in payload["plugins"]}

        self.assertEqual(names, EXPECTED_ALL_SKILLS)
        self.assertEqual(set(payload["base_skills"]), EXPECTED_BASE_SKILLS)
        self.assertEqual(set(payload["with_docs_skills"]), EXPECTED_WITH_DOCS)

    def test_manifest_and_frontmatter_names_match_plugin_directory(self):
        payload = json.loads(self.run_registry("discover").stdout)

        for plugin in payload["plugins"]:
            name = plugin["name"]
            self.assertEqual(plugin["directory_name"], name)
            self.assertEqual(plugin["claude_manifest_name"], name)
            self.assertEqual(plugin["codex_manifest_name"], name)
            self.assertEqual(plugin["skill_directory_name"], name)
            self.assertEqual(plugin["frontmatter_name"], name)

    def test_with_docs_pairing_is_selective_and_all_confirmed_pairs_have_a_base(self):
        payload = json.loads(self.run_registry("discover").stdout)
        pairs = {
            item["with_docs"]: item["base"] for item in payload["with_docs_pairs"]
        }

        self.assertEqual(set(pairs), EXPECTED_WITH_DOCS)
        self.assertEqual(
            set(pairs.values()),
            {name.removesuffix("-with-docs") for name in EXPECTED_WITH_DOCS},
        )
        self.assertEqual(
            set(payload["article_visual_styles"]),
            {name.removesuffix("-with-docs") for name in EXPECTED_WITH_DOCS},
        )
        self.assertTrue(EXPECTED_BASE_SKILLS - set(payload["article_visual_styles"]))

    def test_deprecated_entries_are_excluded_from_inventory_and_routes(self):
        payload = json.loads(self.run_registry("discover").stdout)
        names = {plugin["name"] for plugin in payload["plugins"]}

        self.assertTrue(DEPRECATED_SKILLS.isdisjoint(names))
        self.assertTrue(DEPRECATED_SKILLS.isdisjoint(payload["cover_tips_styles"]))
        self.assertTrue(
            DEPRECATED_SKILLS.isdisjoint(payload["install_index"]["all_skills"])
        )

    def test_generation_is_repeatable_and_produces_all_required_indexes(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_root = Path(temporary_directory)
            os.symlink(ROOT / "plugins", temporary_root / "plugins", target_is_directory=True)
            os.symlink(ROOT / "style-specs", temporary_root / "style-specs", target_is_directory=True)
            self.run_registry("generate", "--root", str(temporary_root))
            generated_paths = [
                temporary_root / "generated" / "skill-registry.json",
                temporary_root / "generated" / "install-index.json",
                temporary_root / "generated" / "install-index.sh",
                temporary_root / "generated" / "cover-tips-styles.json",
                temporary_root / "generated" / "with-docs-style-index.json",
                temporary_root / ".claude-plugin" / "marketplace.json",
                temporary_root / ".agents" / "plugins" / "marketplace.json",
            ]
            first = {
                path: path.read_bytes()
                for path in generated_paths
                if self.assert_file(path)
            }

            self.run_registry("generate", "--root", str(temporary_root))
            second = {path: path.read_bytes() for path in generated_paths}
            self.assertEqual(first, second)

    def test_generated_install_and_cover_tips_indexes_match_discovered_inventory(self):
        self.run_registry("check")
        registry = self.load_json(ROOT / "generated" / "skill-registry.json")
        install_index = self.load_json(ROOT / "generated" / "install-index.json")
        cover_tips = self.load_json(ROOT / "generated" / "cover-tips-styles.json")

        self.assertEqual(
            set(install_index["all_skills"]), EXPECTED_ALL_SKILLS
        )
        self.assertEqual(
            set(cover_tips["cover_styles"]), EXPECTED_BASE_SKILLS
        )
        self.assertEqual(
            set(cover_tips["article_visual_styles"]),
            {name.removesuffix("-with-docs") for name in EXPECTED_WITH_DOCS},
        )
        self.assertEqual(
            set(registry["install_index"]["all_skills"]),
            set(install_index["all_skills"]),
        )

    def test_shared_style_spec_locks_four_with_docs_skill_artifacts(self):
        self.run_registry("check")
        spec = self.load_json(ROOT / "style-specs" / "with-docs.json")
        style_index = self.load_json(ROOT / "generated" / "with-docs-style-index.json")
        spec_by_base = {style["base_skill"]: style for style in spec["styles"]}
        index_by_base = {style["base_skill"]: style for style in style_index["styles"]}

        self.assertEqual(set(spec_by_base), set(EXPECTED_STYLE_PAIRS))
        self.assertEqual(style_index["source_spec"], "style-specs/with-docs.json")
        self.assertEqual(set(index_by_base), set(EXPECTED_STYLE_PAIRS))

        for base_skill, with_docs_skill in EXPECTED_STYLE_PAIRS.items():
            style = spec_by_base[base_skill]
            indexed = index_by_base[base_skill]
            self.assertEqual(style["with_docs_skill"], with_docs_skill)
            self.assertTrue(style["visual_system"])
            self.assertTrue(style["article_visual_system"])
            self.assertTrue(style["base_rule_markers"])
            self.assertTrue(style["with_docs_rule_markers"])
            with_docs_path = ROOT / "plugins" / with_docs_skill / "skills" / with_docs_skill / "SKILL.md"
            self.assertEqual(
                style["artifact_sha256"]["with_docs_skill"],
                self.sha256(with_docs_path),
            )
            self.assertEqual(
                indexed["with_docs_skill_sha256"],
                style["artifact_sha256"]["with_docs_skill"],
            )
            self.assertEqual(indexed.get("visual_system"), style["visual_system"])
            self.assertEqual(
                indexed.get("article_visual_system"), style["article_visual_system"]
            )

    def copy_style_fixture(self, temporary_root):
        shutil.copytree(ROOT / "plugins", temporary_root / "plugins")
        (temporary_root / "style-specs").mkdir()
        shutil.copy2(
            ROOT / "style-specs" / "with-docs.json",
            temporary_root / "style-specs" / "with-docs.json",
        )

    def test_missing_style_spec_fails_check(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_root = Path(temporary_directory)
            shutil.copytree(ROOT / "plugins", temporary_root / "plugins")

            result = self.run_registry_expect_failure(
                "check", "--root", str(temporary_root)
            )

            self.assertIn("style spec is missing", result.stderr)

    def test_wrong_style_spec_pairing_fails_check(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_root = Path(temporary_directory)
            self.copy_style_fixture(temporary_root)
            spec_path = temporary_root / "style-specs" / "with-docs.json"
            spec = json.loads(spec_path.read_text(encoding="utf-8"))
            spec["styles"][0]["with_docs_skill"] = "cover-light-product-with-docs"
            spec_path.write_text(
                json.dumps(spec, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )

            result = self.run_registry_expect_failure(
                "check", "--root", str(temporary_root)
            )

            self.assertIn("style spec pairing is not confirmed", result.stderr)

    def test_skill_artifact_drift_fails_check(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_root = Path(temporary_directory)
            self.copy_style_fixture(temporary_root)
            drifted_skill = (
                temporary_root
                / "plugins"
                / "cover-3d-eye-with-docs"
                / "skills"
                / "cover-3d-eye-with-docs"
                / "SKILL.md"
            )
            drifted_skill.write_text(
                drifted_skill.read_text(encoding="utf-8") + "\nfixture drift\n",
                encoding="utf-8",
            )

            result = self.run_registry_expect_failure(
                "check", "--root", str(temporary_root)
            )

            self.assertIn("with-docs SKILL.md drifted", result.stderr)

    def test_style_rule_marker_drift_fails_check_in_isolated_fixture(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_root = Path(temporary_directory)
            self.copy_style_fixture(temporary_root)
            spec_path = temporary_root / "style-specs" / "with-docs.json"
            spec = json.loads(spec_path.read_text(encoding="utf-8"))
            spec["styles"][0]["base_rule_markers"][0] = "marker absent from fixture"
            spec_path.write_text(
                json.dumps(spec, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )

            result = self.run_registry_expect_failure(
                "check", "--root", str(temporary_root)
            )

            self.assertIn("base style rule marker missing", result.stderr)

    def test_registry_rejects_unsafe_manifest_skill_name(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_root = Path(temporary_directory)
            self.copy_style_fixture(temporary_root)
            manifest_path = (
                temporary_root
                / "plugins"
                / "cover-tips"
                / ".claude-plugin"
                / "plugin.json"
            )
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["name"] = "cover-tips;touch-invalid-name"
            manifest_path.write_text(
                json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )

            result = self.run_registry_expect_failure(
                "generate", "--root", str(temporary_root)
            )

            self.assertIn("invalid skill name", result.stderr)

    def test_remote_installer_rejects_unknown_inventory_line_without_sourcing_it(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_root = Path(temporary_directory)
            sentinel = "$COVER_SKILLS_TEST_SENTINEL"
            index = f'''#!/usr/bin/env bash
# Generated by scripts/skill_registry.py; do not edit by hand.
# shellcheck shell=bash

ALL_SKILLS=(
  "cover-tips"
)

touch "{sentinel}"
'''
            result, sentinel_path = self.run_remote_installer_with_fake_curl(
                temporary_root, index
            )

            self.assertNotEqual(result.returncode, 0, msg=result.stderr)
            self.assertFalse(sentinel_path.exists())
            self.assertIn("unrecognized", result.stderr)

    def test_remote_installer_rejects_unsafe_skill_value_without_sourcing_it(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_root = Path(temporary_directory)
            sentinel = "$COVER_SKILLS_TEST_SENTINEL"
            index = f'''#!/usr/bin/env bash
# Generated by scripts/skill_registry.py; do not edit by hand.
# shellcheck shell=bash

ALL_SKILLS=(
  "$(touch "{sentinel}")"
)

BASE_SKILLS=(
  "cover-tips"
)

WITH_DOCS_SKILLS=(
  "cover-tips"
)

COVER_TIPS_SKILL="cover-tips"
'''
            result, sentinel_path = self.run_remote_installer_with_fake_curl(
                temporary_root, index
            )

            self.assertNotEqual(result.returncode, 0, msg=result.stderr)
            self.assertFalse(sentinel_path.exists())
            self.assertIn("unsafe skill name", result.stderr)

    def test_local_installer_all_creates_seventeen_skill_symlinks(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            target = Path(temporary_directory) / "all-target"

            result = self.run_local_installer(target)

            self.assertEqual(
                result.returncode,
                0,
                msg=f"{result.stdout}\n{result.stderr}",
            )
            installed = {path.name for path in target.iterdir() if path.is_symlink()}
            self.assertEqual(installed, EXPECTED_ALL_SKILLS)
            self.assertEqual(len(installed), 17)
            for name in EXPECTED_ALL_SKILLS:
                link = target / name
                self.assertTrue(link.is_symlink())
                self.assertEqual(link.resolve(), (ROOT / "plugins" / name).resolve())

    def test_local_installer_can_install_with_docs_and_cover_tips_individually(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            target = Path(temporary_directory) / "individual-target"

            with_docs_result = self.run_local_installer(
                target, "cover-3d-eye-with-docs"
            )
            self.assertEqual(
                with_docs_result.returncode,
                0,
                msg=f"{with_docs_result.stdout}\n{with_docs_result.stderr}",
            )
            self.assertEqual(
                {path.name for path in target.iterdir() if path.is_symlink()},
                {"cover-3d-eye-with-docs"},
            )

            cover_tips_result = self.run_local_installer(target, "cover-tips")
            self.assertEqual(
                cover_tips_result.returncode,
                0,
                msg=f"{cover_tips_result.stdout}\n{cover_tips_result.stderr}",
            )
            self.assertEqual(
                {path.name for path in target.iterdir() if path.is_symlink()},
                {"cover-3d-eye-with-docs", "cover-tips"},
            )

    def test_local_and_remote_installers_consume_generated_install_inventory(self):
        local_installer = (ROOT / "scripts" / "install.sh").read_text(encoding="utf-8")
        remote_installer = (ROOT / "install.sh").read_text(encoding="utf-8")

        self.assertIn("generated/install-index.sh", local_installer)
        self.assertIn("generated/install-index.sh", remote_installer)
        self.assertIn("parse_remote_install_index", remote_installer)
        self.assertNotIn('source "$REMOTE_INSTALL_INDEX"', remote_installer)
        self.assertNotIn('find "$PLUGINS_DIR"', local_installer)

    def assert_file(self, path):
        self.assertTrue(path.is_file(), msg=f"generated file is missing: {path}")
        return True


if __name__ == "__main__":
    unittest.main()
