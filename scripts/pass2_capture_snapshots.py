#!/usr/bin/env python3
"""Capture lab/tools snapshots for learn_verification_planning_management."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SCRIPT = ROOT / ".cursor/skills/module-slides/scripts/capture_lab_snapshot.py"
BASE = "http://127.0.0.1:8080/tools"
COURSE = ROOT / "courses/learn_verification_planning_management"

CAPTURES = [
    ("module00-intro", "index", "tools-index.png"),
    ("module01-verif-plan-check", "verif-plan-check", None),
    ("module02-test-taxonomy", "test-taxonomy", None),
    ("module03-feature-matrix", "feature-matrix", None),
    ("module04-cover-bins", "cover-bins", None),
    ("module05-coverage-closure", "coverage-closure", None),
    ("module06-risk-plan", "risk-plan", None),
    ("module07-seed-tags", "seed-tags", None),
    ("module08-regression-triage", "regression-triage", None),
    ("module09-verif-metrics", "verif-metrics", None),
    ("module10-ci-farm-flow", "ci-farm-flow", None),
    ("module11-signoff-checklist", "signoff-checklist", None),
    ("module12-vip-handoff", "vip-handoff", None),
    ("module13-wrap", "index", "tools-index.png"),
]


def main() -> int:
    rc = 0
    for slug, lab, name in CAPTURES:
        mod = COURSE / slug
        cmd = [
            sys.executable,
            str(SCRIPT),
            str(mod.relative_to(ROOT)).replace("\\", "/"),
            "--lab",
            lab,
            "--base",
            BASE,
            "--wait-ms",
            "2000",
            "--height",
            "900",
        ]
        if name:
            cmd.extend(["--name", name])
        print(f"\n=== {slug} ({lab}) ===")
        r = subprocess.run(cmd, cwd=ROOT).returncode
        if r != 0:
            rc = r
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
