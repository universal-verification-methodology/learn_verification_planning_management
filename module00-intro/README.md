# Module 00: Welcome to verification planning

**Kind:** `intro` · Dual-track course welcome

← Start · [Course README](../README.md) · [Coverage / plan checklist →](../module01-verif-plan-check/README.md)

## What this course is

**learn_verification_planning_management** covers **plan → coverage → regression → sign-off**.
Protocol and UVM courses point here for planning depth — do not re-teach full VIP engines here.

| Track | Where you practice | Best for |
|-------|--------------------|----------|
| **A — Planning docs / legacy** | Paper + templates under [`../verification_planning_management/`](../verification_planning_management/) | Plans you keep in a real project |
| **B — Browser lab** | Platform verification-planning tools | Checklists, matrices, triage boards |

Prereq helpful: a protocol course (**learn_uart** / **spi** / **i2c**) or **learn_uvm2017**.

## Setup (Track A)

1. Optional: open legacy docs under [`../verification_planning_management/`](../verification_planning_management/).
2. Editor for markdown / tables (feature matrix, risk plan).
3. Open this repo at `courses/learn_verification_planning_management`.

## Setup (Track B)

1. Serve the platform: `python -m http.server 8080 --directory platform` (from monorepo root).
2. Open http://127.0.0.1:8080/tools/index.html#verif-plan
3. Start with [`verif-plan-check`](http://127.0.0.1:8080/tools/verif-plan-check/index.html).

## How to move through modules

1. Read the module **README** (outcomes).
2. Prefer Track B for interactive boards; Track A for written plans.
3. Check off **CHECKLIST.md**.
4. Expand `transcript.md` / regenerate media with **module-slides** when recording.

## Media

| Artifact | Path |
|----------|------|
| Transcript | [transcript.md](transcript.md) |
| Outline | [outline.yaml](outline.yaml) |
| Slides | [slides.pptx](slides.pptx) · [slides.pdf](slides.pdf) |
| Video | [video.mp4](video.mp4) |
| Quiz | [quiz.json](quiz.json) |

## Next

→ [Module 01: Coverage / plan checklist](../module01-verif-plan-check/README.md)
