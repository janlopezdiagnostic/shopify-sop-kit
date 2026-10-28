#!/usr/bin/env python3
"""Cheap hygiene checks for the kit.

Fails on: em dashes, unresolved placeholder brackets other than the
sanctioned [TO CONFIRM] marker, and any term passed via the FORBIDDEN_TERMS
environment variable (comma separated). Forbidden terms are supplied at run
time so the list itself is never committed to the repo.
"""
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEXT_SUFFIXES = {".md", ".txt", ".py"}
failures = []

forbidden = [t.strip() for t in os.environ.get("FORBIDDEN_TERMS", "").split(",") if t.strip()]

for path in sorted(ROOT.rglob("*")):
    if ".git" in path.parts or path.suffix not in TEXT_SUFFIXES:
        continue
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT)
    if "\u2014" in text or "\u2013" in text:
        failures.append(f"{rel}: contains an em or en dash")
    for match in re.findall(r"\[(?!TO CONFIRM)[A-Z][A-Z ]{2,}\]", text):
        failures.append(f"{rel}: unsanctioned bracket marker {match}")
    for term in forbidden:
        if term.lower() in text.lower():
            failures.append(f"{rel}: contains a forbidden term (from env)")

if failures:
    print("CHECK FAILED")
    for failure in failures:
        print(" -", failure)
    sys.exit(1)
print("check ok:", len(list(ROOT.rglob('*.md'))), "markdown files scanned")
