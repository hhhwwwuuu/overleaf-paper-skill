#!/usr/bin/env python3
from __future__ import annotations

import json
import py_compile
import tempfile
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    ".agents/plugins/marketplace.json",
    ".claude-plugin/marketplace.json",
    ".claude-plugin/plugin.json",
    ".codex-plugin/plugin.json",
    ".mcp.json",
    "plugins/overleaf-paper/.codex-plugin/plugin.json",
    "plugins/overleaf-paper/.mcp.json",
    "plugins/overleaf-paper/skills/overleaf-paper/SKILL.md",
    "plugins/overleaf-paper/mcp-server/package.json",
    "plugins/overleaf-paper/mcp-server/tsconfig.json",
    "plugins/overleaf-paper/mcp-server/src/index.ts",
    "plugins/overleaf-paper/mcp-server/dist/index.js",
    "skills/overleaf-paper/SKILL.md",
    "skills/overleaf-paper/references/overleaf-git.md",
    "skills/overleaf-paper/references/jss-writing-formatting.md",
    "skills/overleaf-paper/scripts/jss_latex_check.py",
    "claude/overleaf-paper/SKILL.md",
    "claude/overleaf-paper/references/overleaf-git.md",
    "claude/overleaf-paper/references/jss-writing-formatting.md",
    "claude/overleaf-paper/scripts/jss_latex_check.py",
    "mcp-server/package.json",
    "mcp-server/tsconfig.json",
    "mcp-server/src/index.ts",
    "mcp-server/dist/index.js",
    "README.md",
    "LICENSE",
]

JSON_FILES = [
    ".agents/plugins/marketplace.json",
    ".claude-plugin/marketplace.json",
    ".claude-plugin/plugin.json",
    ".codex-plugin/plugin.json",
    ".mcp.json",
    "plugins/overleaf-paper/.codex-plugin/plugin.json",
    "plugins/overleaf-paper/.mcp.json",
    "mcp-server/package.json",
    "mcp-server/tsconfig.json",
    "plugins/overleaf-paper/mcp-server/package.json",
    "plugins/overleaf-paper/mcp-server/tsconfig.json",
]

SKILL_FILES = [
    "skills/overleaf-paper/SKILL.md",
    "claude/overleaf-paper/SKILL.md",
    "plugins/overleaf-paper/skills/overleaf-paper/SKILL.md",
]

PY_FILES = [
    "skills/overleaf-paper/scripts/jss_latex_check.py",
    "claude/overleaf-paper/scripts/jss_latex_check.py",
    "plugins/overleaf-paper/skills/overleaf-paper/scripts/jss_latex_check.py",
]


def fail(message: str) -> None:
    raise SystemExit(f"ERROR: {message}")


def check_exists() -> None:
    missing = [path for path in REQUIRED if not (ROOT / path).exists()]
    if missing:
        fail("Missing required files: " + ", ".join(missing))


def check_json(path: str) -> None:
    with (ROOT / path).open("r", encoding="utf-8-sig") as handle:
        json.load(handle)


def check_skill(path: str, expected_name: str) -> None:
    text = (ROOT / path).read_text(encoding="utf-8-sig")
    match = re.match(r"---\s*(.*?)\s*---", text, re.S)
    if not match:
        fail(f"{path} is missing YAML frontmatter")
    frontmatter = match.group(1)
    if not re.search(rf"^name:\s*{re.escape(expected_name)}\s*$", frontmatter, re.M):
        fail(f"{path} has missing or wrong name")
    if not re.search(r"^description:\s*\S.+$", frontmatter, re.M):
        fail(f"{path} is missing description")


def check_marketplace() -> None:
    data = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text(encoding="utf-8-sig"))
    plugins = data.get("plugins", [])
    if not any(plugin.get("name") == "overleaf-paper" and plugin.get("source", {}).get("path") == "./plugins/overleaf-paper" for plugin in plugins):
        fail("marketplace.json must expose ./plugins/overleaf-paper")



def check_claude_marketplace() -> None:
    data = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8-sig"))
    plugins = data.get("plugins", [])
    if not any(plugin.get("name") == "overleaf-paper" and plugin.get("source") == "./" for plugin in plugins):
        fail(".claude-plugin/marketplace.json must expose overleaf-paper from ./")


def check_bundled_mcp() -> None:
    external_import = re.compile(r"^\s*import\s+.+\s+from\s+['\"]@modelcontextprotocol/", re.M)
    for path in ["mcp-server/dist/index.js", "plugins/overleaf-paper/mcp-server/dist/index.js"]:
        text = (ROOT / path).read_text(encoding="utf-8-sig")
        if external_import.search(text):
            fail(f"{path} must be bundled and must not import @modelcontextprotocol at runtime")

def main() -> int:
    check_exists()
    for path in JSON_FILES:
        check_json(path)
    for path in SKILL_FILES:
        check_skill(path, "overleaf-paper")
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        for index, path in enumerate(PY_FILES):
            py_compile.compile(str(ROOT / path), cfile=str(tmpdir_path / f"check_{index}.pyc"), doraise=True)
    check_marketplace()
    check_claude_marketplace()
    check_bundled_mcp()
    print("Project validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
