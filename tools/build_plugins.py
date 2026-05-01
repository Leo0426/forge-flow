#!/usr/bin/env python3
"""
Build Claude Code and Codex plugin packages from .claude-plugin/plugin.json.

Output:
  build/plugins/claude-code/forgeflow/   - load with: claude --plugin-dir
  build/plugins/codex/forgeflow/         - load with: codex plugin marketplace add
"""

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
PLUGIN_JSON = ROOT / ".claude-plugin" / "plugin.json"
BUILD_DIR = ROOT / "build" / "plugins"


def load_plugin_config() -> dict:
    with open(PLUGIN_JSON) as f:
        return json.load(f)


def resolve_skill_dirs(config: dict) -> list[Path]:
    dirs = []
    for skill_path in config["skills"]:
        resolved = (ROOT / skill_path).resolve()
        if not resolved.is_dir():
            print(f"warning: skill directory not found: {resolved}", file=sys.stderr)
            continue
        dirs.append(resolved)
    return dirs


def build_claude_code(config: dict, skill_dirs: list[Path]) -> Path:
    out = BUILD_DIR / "claude-code" / "forgeflow"
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    # Copy each skill directory, preserving bucket/skill structure relative to skills/
    for skill_dir in skill_dirs:
        rel = skill_dir.relative_to(ROOT / "skills")
        dest = out / "skills" / rel
        shutil.copytree(skill_dir, dest)

    # Write plugin manifest with updated skill paths
    manifest = {k: v for k, v in config.items() if k != "skills"}
    manifest["skills"] = [
        f"./skills/{skill_dir.relative_to(ROOT / 'skills')}"
        for skill_dir in skill_dirs
    ]
    plugin_dir = out / ".claude-plugin"
    plugin_dir.mkdir()
    with open(plugin_dir / "plugin.json", "w") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    return out


def build_codex(config: dict, skill_dirs: list[Path]) -> Path:
    out = BUILD_DIR / "codex" / "forgeflow"
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    for skill_dir in skill_dirs:
        rel = skill_dir.relative_to(ROOT / "skills")
        dest = out / "skills" / rel
        shutil.copytree(skill_dir, dest)

    # Codex uses .agents/plugins/ manifest location
    manifest = {k: v for k, v in config.items() if k != "skills"}
    manifest["skills"] = [
        f"./skills/{skill_dir.relative_to(ROOT / 'skills')}"
        for skill_dir in skill_dirs
    ]
    agents_dir = out / ".agents" / "plugins"
    agents_dir.mkdir(parents=True)
    with open(agents_dir / "plugin.json", "w") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    return out


def main():
    config = load_plugin_config()
    skill_dirs = resolve_skill_dirs(config)

    if not skill_dirs:
        print("error: no valid skill directories found", file=sys.stderr)
        sys.exit(1)

    cc_out = build_claude_code(config, skill_dirs)
    codex_out = build_codex(config, skill_dirs)

    print(f"built {len(skill_dirs)} skills")
    print(f"  claude-code : {cc_out.relative_to(ROOT)}")
    print(f"  codex       : {codex_out.relative_to(ROOT)}")
    print()
    print("load claude-code plugin:")
    print(f"  claude --plugin-dir ./{cc_out.relative_to(ROOT)}")
    print()
    print("load codex plugin:")
    print(f"  codex plugin marketplace add ./{codex_out.relative_to(ROOT).parent}")


if __name__ == "__main__":
    main()
