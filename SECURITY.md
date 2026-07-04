# Security Policy

## Supported Versions

| Version | Supported |
| ------- | --------- |
| Latest release on `main` | ✅ |
| Older tags | ❌ (please upgrade) |

## Reporting a Vulnerability

**Please do not open a public GitHub issue for security vulnerabilities.**

1. Prefer [GitHub Private vulnerability reporting](https://github.com/imartinstudio/cover-prompt-skills/security/advisories/new) if enabled on the repository.
2. Otherwise, open a **private** security advisory or contact the maintainer via GitHub Issues with minimal details and request a private channel.

We aim to acknowledge reports within **7 days** and will coordinate a fix and disclosure timeline.

## Scope

In scope:

- Skill definitions, install scripts, and plugin packaging in this repository
- Prompt injection or unsafe defaults in bundled cover-prompt skills that could mislead downstream image-generation workflows

Out of scope:

- Vulnerabilities in third-party image models, agent hosts, or design tools that load these prompts
- Output quality or aesthetic issues that are not security-relevant

## Security Expectations

- Install scripts should not fetch or execute code from unverified remote sources.
- Prompt files should not embed secrets, credentials, or exfiltration instructions.
