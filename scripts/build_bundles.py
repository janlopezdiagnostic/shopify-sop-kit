#!/usr/bin/env python3
"""Build the release ZIPs into dist/.

Runs scripts/check.py first and refuses to build if it fails.
- shopify-sop-kit-full.zip: the whole kit, readable anywhere.
- shopify-sop-kit-core.zip: skill + modules + templates + prompt, the
  upload set for any AI assistant.
- shopify-sop-writer-skill.zip: a shopify-sop-writer folder holding
  SKILL.md, interview.md, the modules, and the templates, for native Skill
  upload in Claude.
"""
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
SKIP_DIRS = {".git", "dist", "scripts", "__pycache__"}

check = subprocess.run([sys.executable, str(ROOT / "scripts/check.py")], cwd=ROOT)
if check.returncode != 0:
    sys.exit("check.py failed; not building")

DIST.mkdir(exist_ok=True)


def add_tree(zf, base, arc_prefix=""):
    for path in sorted(base.rglob("*")):
        if path.is_dir() or any(part in SKIP_DIRS for part in path.parts):
            continue
        zf.write(path, arc_prefix + str(path.relative_to(base)))


with zipfile.ZipFile(DIST / "shopify-sop-kit-full.zip", "w", zipfile.ZIP_DEFLATED) as zf:
    add_tree(zf, ROOT)
with zipfile.ZipFile(DIST / "shopify-sop-kit-core.zip", "w", zipfile.ZIP_DEFLATED) as zf:
    for name in ["prompt.md", "PROBLEM.md", "START-HERE.md", "PRIVACY.md"]:
        zf.write(ROOT / name, name)
    for folder in ["skill", "modules", "templates"]:
        for path in sorted((ROOT / folder).rglob("*")):
            if path.is_file():
                zf.write(path, str(path.relative_to(ROOT)))
with zipfile.ZipFile(DIST / "shopify-sop-writer-skill.zip", "w", zipfile.ZIP_DEFLATED) as zf:
    base = "shopify-sop-writer"
    zf.write(ROOT / "skill/SKILL.md", f"{base}/SKILL.md")
    zf.write(ROOT / "skill/interview.md", f"{base}/interview.md")
    for folder in ["modules", "templates"]:
        for path in sorted((ROOT / folder).rglob("*")):
            if path.is_file():
                zf.write(path, f"{base}/{folder}/{path.name}")

print("built:", ", ".join(p.name for p in sorted(DIST.glob('*.zip'))))
