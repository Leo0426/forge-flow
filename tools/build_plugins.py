#!/usr/bin/env python3
"""
Build Claude Code and Codex plugin packages from .claude-plugin/plugin.json.

Output:
  build/plugins/claude-code/forgeflow/   - load with: claude --plugin-dir
  build/plugins/codex/                   - load with: codex plugin marketplace add
    .agents/plugins/marketplace.json
    plugins/forgeflow/
      .codex-plugin/plugin.json
      skills/
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


def build_codex(config: dict, skill_dirs: list[Path]) -> tuple[Path, Path]:
    """Returns (marketplace_root, plugin_dir)."""
    marketplace_root = BUILD_DIR / "codex"
    plugin_dir = marketplace_root / "plugins" / "forgeflow"

    if marketplace_root.exists():
        shutil.rmtree(marketplace_root)
    plugin_dir.mkdir(parents=True)

    for skill_dir in skill_dirs:
        rel = skill_dir.relative_to(ROOT / "skills")
        dest = plugin_dir / "skills" / rel
        shutil.copytree(skill_dir, dest)

    # Plugin manifest: .codex-plugin/plugin.json
    plugin_manifest = {
        "name": config["name"],
        "version": config["version"],
        "description": config["description"],
        "author": config.get("author", {}),
        "license": config.get("license", "MIT"),
        "skills": "./skills/",
        "interface": {
            "displayName": "ForgeFlow",
            "shortDescription": config["description"],
            "developerName": config.get("author", {}).get("name", ""),
            "category": "Engineering",
            "capabilities": ["Interactive"],
            "defaultPrompt": [f"Help me use {config['name']}."],
        },
    }
    codex_plugin_dir = plugin_dir / ".codex-plugin"
    codex_plugin_dir.mkdir()
    with open(codex_plugin_dir / "plugin.json", "w") as f:
        json.dump(plugin_manifest, f, ensure_ascii=False, indent=2)

    # Marketplace manifest: .agents/plugins/marketplace.json
    marketplace_manifest = {
        "name": f"{config['name']}-plugins",
        "plugins": [
            {
                "name": config["name"],
                "source": {"source": "local", "path": "./plugins/forgeflow"},
                "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
                "category": "Engineering",
            }
        ],
    }
    agents_dir = marketplace_root / ".agents" / "plugins"
    agents_dir.mkdir(parents=True)
    with open(agents_dir / "marketplace.json", "w") as f:
        json.dump(marketplace_manifest, f, ensure_ascii=False, indent=2)

    return marketplace_root, plugin_dir


def main():
    config = load_plugin_config()
    skill_dirs = resolve_skill_dirs(config)

    if not skill_dirs:
        print("error: no valid skill directories found", file=sys.stderr)
        sys.exit(1)

    cc_out = build_claude_code(config, skill_dirs)
    codex_marketplace, codex_plugin = build_codex(config, skill_dirs)

    print(f"built {len(skill_dirs)} skills")
    print(f"  claude-code : {cc_out.relative_to(ROOT)}")
    print(f"  codex       : {codex_plugin.relative_to(ROOT)}")
    print()
    print("load claude-code plugin:")
    print(f"  claude --plugin-dir ./{cc_out.relative_to(ROOT)}")
    print()
    print("load codex plugin:")
    print(f"  codex plugin marketplace add ./{codex_marketplace.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
