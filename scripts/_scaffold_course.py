#!/usr/bin/env python3
"""Scaffold courses/learn_verification_planning_management from syllabus."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COURSES = ROOT.parent
DST = ROOT

LAB_BASE_LOCAL = "http://127.0.0.1:8080/tools"
LAB_BASE_LIVE = "https://universal-verification-methodology.github.io/learning/tools"
LEGACY = "../verification_planning_management"

# Syllabus §14 — all planning browser labs shipped.
MODULES = [
    (0, "intro", "intro", "Welcome to verification planning", None, None),
    (1, "verif-plan-check", "lab", "Coverage / plan checklist", "verif-plan-check", "S"),
    (2, "test-taxonomy", "lab", "Test taxonomy", "test-taxonomy", "S"),
    (3, "feature-matrix", "lab", "Feature × scenario matrix", "feature-matrix", "S"),
    (4, "cover-bins", "lab", "Cover bins sketch", "cover-bins", "S"),
    (5, "coverage-closure", "lab", "Coverage closure", "coverage-closure", "S"),
    (6, "risk-plan", "lab", "Risk-based plan", "risk-plan", "S"),
    (7, "seed-tags", "lab", "Seed / config / tags", "seed-tags", "S"),
    (8, "regression-triage", "lab", "Regression triage", "regression-triage", "S"),
    (9, "verif-metrics", "lab", "Verification metrics", "verif-metrics", "S"),
    (10, "ci-farm-flow", "lab", "CI / farm flow", "ci-farm-flow", "S"),
    (11, "signoff-checklist", "lab", "Sign-off checklist", "signoff-checklist", "S"),
    (12, "vip-handoff", "lab", "VIP handoff", "vip-handoff", "S"),
    (13, "wrap", "wrap", "Planning path complete", None, None),
]


def mod_dir(num: int, slug: str) -> Path:
    return DST / f"module{num:02d}-{slug}"


def lab_urls(lab_id: str) -> tuple[str, str]:
    return (f"{LAB_BASE_LOCAL}/{lab_id}/index.html", f"{LAB_BASE_LIVE}/{lab_id}/")


def write_module_readme(
    num: int, slug: str, kind: str, title: str, lab_id: str | None, status: str | None
) -> None:
    d = mod_dir(num, slug)
    d.mkdir(parents=True, exist_ok=True)
    nn = f"{num:02d}"
    prev = next((m for m in MODULES if m[0] == num - 1), None)
    nxt = next((m for m in MODULES if m[0] == num + 1), None)

    nav = []
    if prev:
        nav.append(f"[← {prev[3]}](../module{prev[0]:02d}-{prev[1]}/README.md)")
    else:
        nav.append("← Start")
    nav.append("[Course README](../README.md)")
    if nxt:
        nav.append(f"[{nxt[3]} →](../module{nxt[0]:02d}-{nxt[1]}/README.md)")
    else:
        nav.append("End →")
    nav_line = " · ".join(nav)

    if kind == "intro":
        body = f"""# Module {nn}: {title}

**Kind:** `intro` · Dual-track course welcome

{nav_line}

## What this course is

**learn_verification_planning_management** covers **plan → coverage → regression → sign-off**.
Protocol and UVM courses point here for planning depth — do not re-teach full VIP engines here.

| Track | Where you practice | Best for |
|-------|--------------------|----------|
| **A — Planning docs / legacy** | Paper + templates under [`{LEGACY}/`]({LEGACY}/) | Plans you keep in a real project |
| **B — Browser lab** | Platform verification-planning tools | Checklists, matrices, triage boards |

Prereq helpful: a protocol course (**learn_uart** / **spi** / **i2c**) or **learn_uvm2017**.

## Setup (Track A)

1. Optional: open legacy docs under [`{LEGACY}/`]({LEGACY}/).
2. Editor for markdown / tables (feature matrix, risk plan).
3. Open this repo at `courses/learn_verification_planning_management`.

## Setup (Track B)

1. Serve the platform: `python -m http.server 8080 --directory platform` (from monorepo root).
2. Open http://127.0.0.1:8080/tools/index.html#verif-plan
3. Start with [`verif-plan-check`]({LAB_BASE_LOCAL}/verif-plan-check/index.html).

## How to move through modules

1. Read the module **README** (outcomes).
2. Prefer Track B for interactive boards; Track A for written plans.
3. Check off **CHECKLIST.md**.
4. Expand `transcript.md` / regenerate media with **module-slides** when recording.

## Media (module-slides ready)

| Artifact | Path |
|----------|------|
| Outline | [outline.yaml](outline.yaml) |
| Transcript | [transcript.md](transcript.md) |
| Slides / video | generate with **module-slides** |

## Next

→ [Module 01: Coverage / plan checklist](../module01-verif-plan-check/README.md)
"""
    elif kind == "wrap":
        body = f"""# Module {nn}: {title}

**Kind:** `wrap`

{nav_line}

## You can now

- Map features → scenarios → coverage ideas and close holes intentionally
- Classify tests (directed / random / stress / corner) and triage regressions
- Track seeds / tags, CI vs farm stages, and sign-off criteria
- Hand off a VIP-style package checklist (docs + API + self-test)

## Dual-track recap

If you mainly used **browser labs**, write one short plan doc offline using the same vocabulary.  
If you mainly used **Track A**, open the shipped boards for interactive challenges.

## Next courses

Back to protocol / UVM work with a clearer planning vocabulary — or deepen offline in [`{LEGACY}/`]({LEGACY}/).  
Syllabus ladder: [../../syllabus.md](../../syllabus.md#suggested-learning-ladder)

## Checklist

- [ ] I completed Track A and/or Track B for the modules I care about
- [ ] I can explain coverage closure vs “eyeballing waves”
- [ ] I know sign-off is criteria-driven, not “we ran overnight”
"""
    else:
        assert lab_id and status
        local, live = lab_urls(lab_id)
        body = f"""# Module {nn}: {title}

**Kind:** `lab` · Primary lab: `{lab_id}` · **Shipped**

{nav_line}

## Outcomes

After this module you can explain and practice the ideas taught by **`{lab_id}`**, in the browser and/or with a written plan sketch.

## Two tracks (pick one or both)

### Track A — Planning docs (hands-on)

1. Open [EXAMPLES.md](EXAMPLES.md) and work the prompts (paper / markdown tables).
2. Optional templates: [`{LEGACY}/`]({LEGACY}/).
3. Complete [CHECKLIST.md](CHECKLIST.md).
4. Optional: `./scripts/module.sh {nn} --check`.

### Track B — Browser lab (online)

1. Local: [{local}]({local})
2. Live: [{live}]({live})
3. Load the **starter example**, then work challenges.
4. Check off the Track B items in [CHECKLIST.md](CHECKLIST.md).

> Concept labs are literacy tools — they do not replace a real coverage DB or farm.

## Media (module-slides ready)

| Artifact | Path |
|----------|------|
| Outline | [outline.yaml](outline.yaml) |
| Transcript | [transcript.md](transcript.md) |
| Slides / video | generate with **module-slides** |

## Files

```
module{nn}-{slug}/
├── README.md
├── CHECKLIST.md
├── EXAMPLES.md
├── outline.yaml
├── transcript.md
└── (optional) assets/ examples/
```
"""
    (d / "README.md").write_text(body, encoding="utf-8")


def write_checklist(num: int, slug: str, kind: str, title: str, lab_id: str | None) -> None:
    d = mod_dir(num, slug)
    nn = f"{num:02d}"
    if kind == "intro":
        text = f"""# Module {nn} checklist — {title}

## Setup

- [ ] Opened this repo at `courses/learn_verification_planning_management`
- [ ] Opened the [tools index]({LAB_BASE_LOCAL}/index.html#verif-plan) once
- [ ] Optional: peeked at [`{LEGACY}/`]({LEGACY}/)

## Mindset

- [ ] I understand plan → coverage → regression → sign-off
- [ ] I know protocol/UVM courses hand planning depth to this course
"""
    elif kind == "wrap":
        text = f"""# Module {nn} checklist — {title}

- [ ] Reviewed outcomes in [README.md](README.md)
- [ ] Can name coverage closure, triage, and sign-off in my own words
"""
    else:
        text = f"""# Module {nn} checklist — {title}

## Track A — Planning docs

- [ ] Worked through at least one prompt in [EXAMPLES.md](EXAMPLES.md)
- [ ] Can explain the outcome in my own words

## Track B — Browser lab (`{lab_id}`)

- [ ] Opened the lab (local or live)
- [ ] Loaded starter + completed a few challenges

## Done when

- [ ] I can do the task offline **or** I finished the browser challenges (preferably both)
"""
    (d / "CHECKLIST.md").write_text(text, encoding="utf-8")


def write_examples_md(num: int, slug: str, kind: str, title: str) -> None:
    d = mod_dir(num, slug)
    nn = f"{num:02d}"
    if kind == "lab":
        text = f"""# Module {nn} examples — {title}

Track A (written planning literacy). Track B is the matching browser board.

## Prompts

1. Restate the core idea of **{title}** in one sentence.
2. Draw or tabulate one worked example (feature row, risk cell, triage bucket, …).
3. Optional: peek at templates under [`{LEGACY}/`]({LEGACY}/).

## Stretch

Redo the same idea in the browser lab starter challenges.
"""
    else:
        text = f"""# Module {nn} — no example trees

This is an `{kind}` module. See [README.md](README.md).
"""
    (d / "EXAMPLES.md").write_text(text, encoding="utf-8")


def write_outline_transcript(
    num: int, slug: str, kind: str, title: str, lab_id: str | None
) -> None:
    d = mod_dir(num, slug)
    nn = f"{num:02d}"
    lab_line = lab_id or "none"
    track_line = (
        "A (planning docs) · B (browser lab)"
        if kind == "lab"
        else ("recap only" if kind == "wrap" else "A · B intro")
    )

    (d / "outline.yaml").write_text(
        f"""# Module {nn} outline — stub for module-slides
title: "{title}"
kind: {kind}
lab: {lab_id or "null"}
footer: "learn_verification_planning_management — {slug}"
slides:
  - type: title
    title: "{title}"
    subtitle: "verification planning module {nn}"
    notes: "Welcome. This module is {title}."
  - type: bullets
    title: Core idea
    bullets:
      - One planning concept
      - Why it matters for sign-off
    notes: "Teach the core idea — expand spoken prose in transcript.md."
  - type: bullets
    title: Track B browser lab
    bullets:
      - Open the matching planning lab
      - Load starter · challenges
    notes: "Show the browser board starter when available."
  - type: bullets
    title: Track A written plan
    bullets:
      - Paper or markdown table
      - Optional legacy templates
    notes: "Point at EXAMPLES.md and legacy verification_planning_management."
  - type: bullets
    title: Your turn
    bullets:
      - Complete the checklist for at least one track
      - Optional short quiz
    notes: "Send learners to CHECKLIST.md, then the next module."
duration_minutes: 6
""",
        encoding="utf-8",
    )

    if lab_id:
        show_b = (
            f"Open the browser lab `{lab_id}`: load the starter example, "
            "then walk a couple of challenges so the board vocabulary sticks."
        )
        show_a = (
            "On paper or in markdown, sketch the same idea once. "
            f"Optional templates live under {LEGACY}/."
        )
    else:
        show_b = "Point at the tools verification-planning section."
        show_a = "Show the plan → coverage → regression → sign-off arc."

    (d / "transcript.md").write_text(
        f"""# Module {nn} — {title}

**Module id:** module{nn}-{slug}  
**Lab:** {lab_line}  
**Tracks:** {track_line}

## Slide 1 — {title}

Welcome to verification planning and management. This module focuses on **{title}**. Protocol and UVM courses teach how to build tests; this course teaches how to plan, measure, and sign off.

## Slide 2 — Why this matters

Without a plan, coverage holes and flaky regressions stay invisible until late. One clear planning skill here saves weeks of thrash later.

## Slide 3 — Track B browser lab

{show_b}

## Slide 4 — Track A written plan

{show_a}

## Slide 5 — Pitfalls

Do not confuse a coverage number with product quality. Do not treat overnight farm runs as sign-off without exit criteria. Prefer tagged, seed-reproducible failures over “it failed somehow.”

## Slide 6 — Your turn

Complete the checklist for at least one track — preferably both. When you finish, continue to the next module in docs/MODULES.md.
""",
        encoding="utf-8",
    )


def write_docs_index() -> None:
    docs = DST / "docs"
    docs.mkdir(exist_ok=True)
    rows = []
    for num, slug, kind, title, lab_id, status in MODULES:
        lab = f"`{lab_id}`" if lab_id else "—"
        st = status or "—"
        rows.append(
            f"| {num:02d} | `{kind}` | [{title}](../module{num:02d}-{slug}/README.md) | {lab} | {st} |"
        )
    (docs / "MODULES.md").write_text(
        f"""# learn_verification_planning_management — module index

Lab-driven syllabus (pass 3). Full product syllabus: [../../syllabus.md](../../syllabus.md#14-learn_verification_planning_management).

| # | Kind | Module | Lab | Status |
|---|------|--------|-----|--------|
{chr(10).join(rows)}

## Dual tracks

See [TWO_TRACKS.md](TWO_TRACKS.md). Legacy: [`{LEGACY}/`]({LEGACY}/).
""",
        encoding="utf-8",
    )
    (docs / "TWO_TRACKS.md").write_text(
        f"""# Two learning tracks

## Track A — Planning docs / legacy

Practice with paper + markdown plans (optional templates).

- Prompts under each `moduleNN-*/EXAMPLES.md`
- Optional examples in [`{LEGACY}/`]({LEGACY}/)
- Self-check: `./scripts/module.sh NN --check`

## Track B — Browser lab

- Local tools: {LAB_BASE_LOCAL}/#verif-plan
- Live: {LAB_BASE_LIVE}/
- **Shipped:** `verif-plan-check`, `test-taxonomy`, `feature-matrix`, `cover-bins`, `coverage-closure`, `risk-plan`, `seed-tags`, `regression-triage`, `verif-metrics`, `ci-farm-flow`, `signoff-checklist`, `vip-handoff`

## Recommended path

1. Intro + plan checklist
2. Taxonomy → feature matrix → cover bins → closure
3. Risk / seeds / triage / metrics
4. CI-farm → sign-off → VIP handoff
""",
        encoding="utf-8",
    )


def write_course_readme() -> None:
    landing = [
        f"| {num:02d} — {title} | [module{num:02d}-{slug}](module{num:02d}-{slug}/README.md) |"
        for num, slug, _k, title, *_ in MODULES
    ]
    shipped = sum(1 for m in MODULES if m[5] == "S")
    (DST / "README.md").write_text(
        "\n".join(
            [
                "# learn_verification_planning_management",
                "",
                "[![GitHub](https://img.shields.io/badge/GitHub-learn__verification__planning__management-181717?logo=github)](https://github.com/universal-verification-methodology/learn_verification_planning_management)",
                "[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-green?logo=creativecommons&logoColor=white)](LICENSE)",
                "[![Role](https://img.shields.io/badge/role-Git%20submodule-orange)](https://github.com/universal-verification-methodology/learning)",
                "[![Parent](https://img.shields.io/badge/parent-learning%20monorepo-0A9EDC)](https://github.com/universal-verification-methodology/learning)",
                "[![Labs](https://img.shields.io/badge/labs-GitHub%20Pages-222?logo=githubpages)](https://universal-verification-methodology.github.io/learning/tools/)",
                "[![Domain](https://img.shields.io/badge/domain-verification%20planning%20%7C%20coverage%20%7C%20sign--off-purple)](https://github.com/universal-verification-methodology/learn_verification_planning_management)",
                "",
                "**learn_verification_planning_management** is the open learning path for *plan → coverage → regression → sign-off*.",
                "",
                "Authors rebuild slides/audio with **module-slides** in the parent monorepo. Legacy materials: [`verification_planning_management`](../verification_planning_management/).",
                "",
                "## Table of contents",
                "",
                "- [Contents](#contents)",
                "- [Browse or clone](#browse-or-clone)",
                "- [Author: module-slides](#author-module-slides)",
                "- [Two learning tracks](#two-learning-tracks)",
                "- [Module landings](#module-landings)",
                "- [Browser labs](#browser-labs)",
                "- [License](#license)",
                "",
                "## Contents",
                "",
                "```text",
                "learn_verification_planning_management/",
                "├── README.md",
                "├── LICENSE",
                "├── docs/",
                "│   ├── MODULES.md",
                "│   └── TWO_TRACKS.md",
                "├── scripts/",
                "│   └── module.sh",
                "├── module00-intro/",
                "├── module01-verif-plan-check/",
                "├── …",
                "└── module13-wrap/",
                "```",
                "",
                "## Browse or clone",
                "",
                "- **Browser labs:** [tools/#verif-plan](https://universal-verification-methodology.github.io/learning/tools/#verif-plan)",
                "- **Legacy:** [`verification_planning_management`](https://github.com/universal-verification-methodology/verification_planning_management)",
                "- **Syllabus:** [`syllabus.md` § planning](https://github.com/universal-verification-methodology/learning/blob/main/syllabus.md#14-learn_verification_planning_management)",
                "",
                "```bash",
                "git clone --recurse-submodules \\",
                "  git@github.com:universal-verification-methodology/learning.git",
                "ls courses/learn_verification_planning_management",
                "./scripts/module.sh 01 --check",
                "```",
                "",
                "## Author: module-slides",
                "",
                "```bash",
                "cd ../..   # monorepo root",
                "python .cursor/skills/module-slides/scripts/transcript_to_outline.py \\",
                "  courses/learn_verification_planning_management/module01-verif-plan-check",
                "bash .cursor/skills/module-slides/scripts/narrate_clips.sh \\",
                "  courses/learn_verification_planning_management/module01-verif-plan-check",
                "```",
                "",
                "## Two learning tracks",
                "",
                "Details: [docs/TWO_TRACKS.md](docs/TWO_TRACKS.md).",
                "",
                "| Track | Practice surface | Start here |",
                "|-------|------------------|------------|",
                f"| **A — Planning docs** | Paper · [`{LEGACY}`]({LEGACY}/) | [docs/TWO_TRACKS.md](docs/TWO_TRACKS.md) |",
                f"| **B — Browser lab** | Planning boards | [verif-plan-check]({LAB_BASE_LIVE}/verif-plan-check/) |",
                "",
                f"Lab status snapshot: **{shipped} shipped** (see [docs/MODULES.md](docs/MODULES.md)).",
                "",
                "## Module landings",
                "",
                "Full status table: **[docs/MODULES.md](docs/MODULES.md)**.",
                "",
                "| Module | Landing |",
                "|--------|---------|",
                *landing,
                "",
                "## Browser labs",
                "",
                f"**Shipped:** [verif-plan-check]({LAB_BASE_LIVE}/verif-plan-check/) · [test-taxonomy]({LAB_BASE_LIVE}/test-taxonomy/) · [feature-matrix]({LAB_BASE_LIVE}/feature-matrix/) · [cover-bins]({LAB_BASE_LIVE}/cover-bins/) · [coverage-closure]({LAB_BASE_LIVE}/coverage-closure/) · [risk-plan]({LAB_BASE_LIVE}/risk-plan/) · [seed-tags]({LAB_BASE_LIVE}/seed-tags/) · [regression-triage]({LAB_BASE_LIVE}/regression-triage/) · [verif-metrics]({LAB_BASE_LIVE}/verif-metrics/) · [ci-farm-flow]({LAB_BASE_LIVE}/ci-farm-flow/) · [signoff-checklist]({LAB_BASE_LIVE}/signoff-checklist/) · [vip-handoff]({LAB_BASE_LIVE}/vip-handoff/).",
                "",
                "## License",
                "",
                "[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — see [`LICENSE`](LICENSE).",
                "",
            ]
        ),
        encoding="utf-8",
    )


def write_scripts() -> None:
    scripts = DST / "scripts"
    scripts.mkdir(exist_ok=True)
    (scripts / "module.sh").write_text(
        r"""#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
NN="${1:-}"
shift || true
if [[ -z "$NN" || "$NN" == "--help" ]]; then
  echo "Usage: $0 NN [--check|--demo|--help]"
  exit 0
fi
NN="$(printf '%02d' "$((10#$NN))")"
MOD_DIR="$(find "$ROOT" -maxdepth 1 -type d -name "module${NN}-*" | head -1)"
if [[ -z "$MOD_DIR" ]]; then
  echo "No module directory for $NN"
  exit 1
fi
ACTION="${1:---check}"
case "$ACTION" in
  --check)
    echo "Module $NN self-check (Track A environment)"
    echo "Module dir: $MOD_DIR"
    command -v bash >/dev/null && echo "[OK] bash"
    LEGACY="$(cd "$ROOT/.." && pwd)/verification_planning_management"
    if [[ -d "$LEGACY" ]]; then
      echo "[OK] legacy course present: $LEGACY"
    else
      echo "[INFO] legacy verification_planning_management not checked out"
    fi
    [[ -f "$MOD_DIR/EXAMPLES.md" ]] && echo "[OK] EXAMPLES.md"
    [[ -f "$MOD_DIR/CHECKLIST.md" ]] && echo "[OK] CHECKLIST.md"
    [[ -f "$MOD_DIR/transcript.md" ]] && echo "[OK] transcript.md (module-slides)"
    ;;
  --demo)
    echo "Demo: open $MOD_DIR/EXAMPLES.md and README.md"
    ;;
  *)
    echo "Unknown option: $ACTION"
    exit 1
    ;;
esac
""",
        encoding="utf-8",
    )
    (scripts / "README.md").write_text(
        """# Scripts

| Script | Purpose |
|--------|---------|
| `module.sh NN` | `--check` / `--demo` for module number `NN` |
| `_scaffold_course.py` | Regenerate course stubs from syllabus (authors) |

```bash
chmod +x scripts/*.sh
./scripts/module.sh 01 --check
```
""",
        encoding="utf-8",
    )


def write_license() -> None:
    src = COURSES / "learn_unix" / "LICENSE"
    dst = DST / "LICENSE"
    name = "learn_verification_planning_management"
    if src.exists():
        dst.write_text(
            src.read_text(encoding="utf-8").replace("learn_unix", name),
            encoding="utf-8",
        )
    else:
        dst.write_text(
            "Creative Commons Attribution 4.0 International (CC BY 4.0)\n\n"
            f"Copyright (c) The {name} contributors.\n\n"
            "https://creativecommons.org/licenses/by/4.0/\n",
            encoding="utf-8",
        )


def main() -> None:
    DST.mkdir(parents=True, exist_ok=True)
    write_license()
    write_course_readme()
    write_docs_index()
    write_scripts()
    for num, slug, kind, title, lab_id, status in MODULES:
        print(f"module{num:02d}-{slug} …")
        write_module_readme(num, slug, kind, title, lab_id, status)
        write_checklist(num, slug, kind, title, lab_id)
        write_examples_md(num, slug, kind, title)
        write_outline_transcript(num, slug, kind, title, lab_id)
    print(f"scaffolded {DST}")


if __name__ == "__main__":
    main()
