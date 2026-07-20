#!/usr/bin/env python3
"""Generate pass-1 transcript.md + quiz.json for learn_verification_planning_management."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def write(module: str, transcript: str, quiz: dict) -> None:
    d = ROOT / module
    d.mkdir(parents=True, exist_ok=True)
    (d / "transcript.md").write_text(transcript.strip() + "\n", encoding="utf-8")
    (d / "quiz.json").write_text(
        json.dumps(quiz, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print("wrote", module)


def q(module: str, title: str, items: list) -> dict:
    return {
        "module": module,
        "title": title,
        "passing_score": 0.67,
        "items": items,
    }


def mc(qid: str, prompt: str, choices: list[str], answer: int, explain: str) -> dict:
    return {
        "id": qid,
        "type": "multiple_choice",
        "prompt": prompt,
        "choices": choices,
        "answer": answer,
        "explain": explain,
    }


def tf(qid: str, prompt: str, answer: bool, explain: str) -> dict:
    return {
        "id": qid,
        "type": "true_false",
        "prompt": prompt,
        "answer": answer,
        "explain": explain,
    }


MODULES: list[tuple[str, str, dict]] = []

MODULES.append(
    (
        "module00-intro",
        """
# Module 00 — Welcome to verification planning

**Module id:** module00-intro
**Lab:** none (intro)
**Tracks:** A (planning docs) · B (browser lab)

## Slide 1 — Welcome to verification planning

Welcome to verification planning and management. Protocol and UVM courses teach how to build tests and VIP. This path teaches the other half: how to plan what to verify, measure coverage and risk, triage regressions, and decide when you are ready to sign off.

## Slide 2 — What you’ll build toward

The arc is plan, coverage, regression, sign-off. You’ll practice a feature-to-scenario-to-coverage checklist, test taxonomy, a feature-by-scenario matrix, cover bins and closure ideas, risk priority, seed and tag replay cards, triage buckets, metrics bars, CI-to-farm flow, a sign-off gate, and VIP handoff deliverables. Deep VIP engines stay in protocol and UVM courses—here you learn the planning layer those courses point to.

## Slide 3 — Two tracks, one idea

Track A is planning docs you keep: paper or markdown tables, optional templates in the legacy verification planning materials. Track B is the platform’s verification-planning boards—interactive checklists and matrices with challenges. You may do either track, or both. A good rhythm is browser board first for vocabulary, then a short written table you could paste into a real project plan.

## Slide 4 — Set up Track A

Open this course folder and skim the module READMEs. Keep a notebook or markdown file ready for small tables. Optional: browse the legacy planning materials for templates. From the course root, self-check scripts can grade checklist items when you want them. Helpful prereq: one protocol course or basic UVM literacy—so the plan words map to tests you already understand.

## Slide 5 — Set up Track B

![Tools index](assets/tools-index.png)

From the monorepo, serve the platform folder with a simple local web server, then open the tools index and jump to the verification-planning section. All twelve planning labs ship—from plan checklist through VIP handoff. If you prefer, use the published tools site instead. Confirm you can reach the index; the next module opens the coverage and plan checklist lab.

## Slide 6 — How to move through modules

For each module, read the README for the outcome, pick a track—or both—then work the checklist. Prefer Track B for graded board challenges; prefer Track A for artifacts you can reuse at work. When you finish this intro checklist, continue to the coverage and plan checklist.
""",
        q(
            "module00-intro",
            "Welcome to verification planning",
            [
                mc(
                    "q1",
                    "This course’s main arc is…",
                    [
                        "Plan → coverage → regression → sign-off",
                        "Only RTL synthesis and place-and-route",
                        "Only Git branching strategies",
                        "Only writing UVM agents from scratch",
                    ],
                    0,
                    "Planning and management path, not VIP engines.",
                ),
                mc(
                    "q2",
                    "Track A practice means…",
                    [
                        "Paper or markdown planning docs / templates",
                        "Only forcing clocks in a wave window",
                        "Only PCB silkscreen review",
                        "Browser labs forever with no written plan",
                    ],
                    0,
                    "Track A is lasting planning artifacts.",
                ),
                mc(
                    "q3",
                    "Protocol and UVM courses typically…",
                    [
                        "Teach how to build tests/VIP; this course teaches plan, measure, and sign-off",
                        "Replace the need for any coverage plan",
                        "Are identical to this planning course",
                        "Forbid triage and metrics",
                    ],
                    0,
                    "Planning depth lives here; engines elsewhere.",
                ),
                tf(
                    "q4",
                    "Browser planning boards are literacy tools—they do not replace a real project’s coverage database or farm.",
                    True,
                    "Concept boards teach vocabulary and habits.",
                ),
            ],
        ),
    )
)

MODULES.append(
    (
        "module01-verif-plan-check",
        """
# Module 01 — Coverage / plan checklist

**Module id:** module01-verif-plan-check
**Lab:** verif-plan-check
**Tracks:** A (planning docs) · B (browser lab)

## Slide 1 — Coverage / plan checklist

A verification plan is not a pile of test names. It is a traceability chain: a feature the product must do, a scenario that exercises it, and a coverage item that proves the scenario ran. If any link is missing, you cannot measure completion.

## Slide 2 — Feature, scenario, coverage

Feature means requirement or capability—say UART transmit. Scenario is the test story—send one byte. Coverage is the measurable proof—a bin, coverpoint, or checklist item such as transmit-byte-done. Complete means all three layers link. Incomplete means a gap: a scenario with no coverage, or coverage with no owning feature.

## Slide 3 — Browser lab

![Lab starter](assets/lab-starter.png)

In the plan-check lab, load the starter: UART TX, send one byte, and transmit-byte-done linked—status complete. Try presets that drop coverage or orphan a bin, then rebuild the chain. Challenges quiz each layer and force you to restore a complete plan from gaps.

## Slide 4 — Planning docs practice

On paper or markdown, write one row with three columns: feature, scenario, coverage item. Use a tiny UART or SPI capability you know. Then deliberately delete the coverage cell and ask: how would I know this scenario ran? That question is the whole module.

## Slide 5 — Pitfalls to watch

Do not treat the board as a live coverage database. Do not list coverage items with no feature owner—orphans lie. Do not stop at scenarios without a measurable proof. And do not confuse “we have a test file” with “we have a coverable claim.”

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, reach a complete three-layer chain. On paper, write one feature-scenario-coverage row you could paste into a real plan. When you are ready, take the short quiz, then continue to test taxonomy.
""",
        q(
            "module01-verif-plan-check",
            "Coverage / plan checklist",
            [
                mc(
                    "q1",
                    "The planning chain in this lab is…",
                    [
                        "Feature → scenario → coverage item",
                        "Only seed → farm → waiver",
                        "Only compile → elaborate → wave",
                        "Only git commit → push → merge",
                    ],
                    0,
                    "Traceability: feature, scenario, measurable coverage.",
                ),
                mc(
                    "q2",
                    "A scenario without a coverage item is…",
                    [
                        "Unmeasurable—you cannot prove it ran",
                        "Automatically signed off",
                        "The same as a P0 risk",
                        "A VIP handoff deliverable",
                    ],
                    0,
                    "No coverage link means no proof.",
                ),
                mc(
                    "q3",
                    "Coverage without a feature or scenario is…",
                    [
                        "An orphan measurement—hard to own or close",
                        "Always better than a full chain",
                        "Required before naming any feature",
                        "Proof the farm is healthy",
                    ],
                    0,
                    "Orphan bins lack planning ownership.",
                ),
                tf(
                    "q4",
                    "COMPLETE in the lab means feature, scenario, and coverage are linked for the row.",
                    True,
                    "Starter UART TX chain is the exemplar.",
                ),
            ],
        ),
    )
)

MODULES.append(
    (
        "module02-test-taxonomy",
        """
# Module 02 — Test taxonomy

**Module id:** module02-test-taxonomy
**Lab:** test-taxonomy
**Tracks:** A (planning docs) · B (browser lab)

## Slide 1 — Test taxonomy

Not every test should be the same shape. Taxonomy sorts intent: directed checks for known requirements, constrained-random for breadth, stress for long pressure, and corner or negative cases for illegal and boundary behavior. A balanced plan mixes tiers on purpose.

## Slide 2 — Four tiers

Directed means hand-crafted stimulus for a known scenario. Random means constrained-legal traffic to explore space. Stress means long-run, backlog, or concurrent pressure. Corner means illegal, framing, or rare edges. Open rows are untyped; skewed means one tier dominates; balanced means each tier has intentional coverage.

## Slide 3 — Browser lab

![Lab starter](assets/lab-starter.png)

In the taxonomy lab, load the starter with one test per tier until status reads balanced. Try an all-directed preset and watch skewed appear. Classify an open row, then scan the plan. Challenges lock in what each tier is for—not just cute names.

## Slide 4 — Planning docs practice

List four short test names for a UART-like block and tag each directed, random, stress, or corner. If everything is directed, rewrite one as random and one as corner. Say in one sentence why the mix reduces escape risk.

## Slide 5 — Pitfalls to watch

Do not equate balanced taxonomy with one-hundred percent functional coverage. Do not leave tests untyped on a living plan. Do not hide negative cases because they are “hard.” And do not confuse a green CI job with a thoughtfully tiered suite.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. Classify a small set until it looks balanced, then take the quiz and continue to the feature-by-scenario matrix.
""",
        q(
            "module02-test-taxonomy",
            "Test taxonomy",
            [
                mc(
                    "q1",
                    "Directed tests are mainly for…",
                    [
                        "Hand-crafted stimulus for a known scenario or requirement",
                        "Only farm license recovery",
                        "Only waiver documents",
                        "Only random plusarg soup with no intent",
                    ],
                    0,
                    "Directed = known scenario checks.",
                ),
                mc(
                    "q2",
                    "Corner / negative tests target…",
                    [
                        "Illegal, boundary, or rare sequences",
                        "Only happy-path one-byte smoke",
                        "Only documentation typos",
                        "Only CI agent installers",
                    ],
                    0,
                    "Corner = edges and illegal cases.",
                ),
                mc(
                    "q3",
                    "An all-directed suite with no corner tests is typically…",
                    [
                        "Skewed—missing intentional tier mix",
                        "Automatically BALANCED",
                        "A sign-off READY gate",
                        "Proof of zero bug escapes",
                    ],
                    0,
                    "Missing tiers → SKEWED.",
                ),
                tf(
                    "q4",
                    "BALANCED taxonomy means each tier has intentional tests—not that coverage percent is 100.",
                    True,
                    "Taxonomy ≠ coverage closure number.",
                ),
            ],
        ),
    )
)

MODULES.append(
    (
        "module03-feature-matrix",
        """
# Module 03 — Feature × scenario matrix

**Module id:** module03-feature-matrix
**Lab:** feature-matrix
**Tracks:** A (planning docs) · B (browser lab)

## Slide 1 — Feature × scenario matrix

A matrix makes intersections visible. Rows are features; columns are scenarios. Each cell is empty, planned, or covered. Empty means you never decided; planned means intent without proof; covered means evidence exists. Scanning gaps is how plans stop lying to you.

## Slide 2 — Planned versus covered

Mark P when you intend a test or story for that intersection. Mark C when a bin, checklist, or passing directed check proves it. A board with no empty cells can still be weak if everything is only P—intent without evidence. Closing gaps means either plan the empty cell or produce coverage for a planned one.

## Slide 3 — Browser lab

![Lab starter](assets/lab-starter.png)

In the feature-matrix lab, load the starter UART transmit and receive against byte, idle, and error scenarios with no empty cells. Cycle cells between empty, P, and C. Load a one-gap or many-gaps preset and scan until you can name every hole.

## Slide 4 — Planning docs practice

Draw a two-by-three grid for one block: two features, three scenarios. Fill each cell with dash, P, or C. Leave one empty on purpose, then write the next action that would fill it. That next-action habit is the point of the matrix.

## Slide 5 — Pitfalls to watch

Do not conflate P with C. Do not celebrate zero empty cells when nothing is covered. Do not hide rare scenarios off the grid. And do not grow the matrix so huge that nobody maintains it—start small and real.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. Scan one matrix for gaps, fix or name them, then take the quiz and continue to cover bins.
""",
        q(
            "module03-feature-matrix",
            "Feature × scenario matrix",
            [
                mc(
                    "q1",
                    "In this lab, P on a cell means…",
                    [
                        "Planned intent for that feature×scenario intersection",
                        "Proven coverage evidence already exists",
                        "Priority P0 only",
                        "Pass rate on the farm",
                    ],
                    0,
                    "P = planned, not yet proof.",
                ),
                mc(
                    "q2",
                    "C on a cell means…",
                    [
                        "Covered—evidence or bin hit for that intersection",
                        "Compile-only with no test",
                        "Config plusargs missing",
                        "Corner taxonomy only",
                    ],
                    0,
                    "C = covered / evidence.",
                ),
                mc(
                    "q3",
                    "An empty matrix cell is…",
                    [
                        "A gap—unplanned intersection",
                        "Automatically waived",
                        "The same as HEALTHY metrics",
                        "Proof of VIP handoff",
                    ],
                    0,
                    "Empty = gap to plan or cover.",
                ),
                tf(
                    "q4",
                    "A matrix with no empty cells can still be weak if every cell is only P and never C.",
                    True,
                    "Intent without evidence is not closure.",
                ),
            ],
        ),
    )
)

MODULES.append(
    (
        "module04-cover-bins",
        """
# Module 04 — Cover bins sketch

**Module id:** module04-cover-bins
**Lab:** cover-bins
**Tracks:** A (planning docs) · B (browser lab)

## Slide 1 — Cover bins sketch

Coverage closes when defined bins get hits. A coverpoint names what you sample; bins partition the interesting space. A hole is a defined bin with zero hits. Sketching bins before you code them keeps random stimulus honest about what “done” means.

## Slide 2 — Sample, hit, hole

You sample a value into the coverpoint; matching bins increment. Coverage percent is bins hit over bins defined. Hitting mid once on a four-bin nibble point is twenty-five percent with three holes left—not “mostly done.” Values outside named bins are a modeling question, not an automatic hole.

## Slide 3 — Browser lab

![Lab starter](assets/lab-starter.png)

In the cover-bins lab, load the starter nibble point with low, mid, high, and top; mid already hit from sample five. Sample into other bins, switch opcode or FIFO presets, and close holes on purpose. Challenges ask you to hit a named hole and to finish all bins—not to spam random blindly.

## Slide 4 — Planning docs practice

Sketch one coverpoint with four named bins for a data nibble or opcode set. Mark which bin you would hit with a directed sample first. Note one value that sits outside your bins and decide whether to add a bin or ignore it deliberately.

## Slide 5 — Pitfalls to watch

Do not confuse “more random” with hole closure. Do not redefine holes as every unseen number in nature—only defined bins count. Do not skip naming bins because cross coverage feels advanced; start with clear singles. And remember the lab is a sketch, not your simulator’s coverage DB.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. Close or name holes on a small bin sketch, then take the quiz and continue to coverage closure.
""",
        q(
            "module04-cover-bins",
            "Cover bins sketch",
            [
                mc(
                    "q1",
                    "A coverage hole in this lab means…",
                    [
                        "A defined bin with zero hits",
                        "Any integer the DUT never saw in nature",
                        "A failing CI agent only",
                        "A missing git tag",
                    ],
                    0,
                    "Hole = defined bin, zero hits.",
                ),
                mc(
                    "q2",
                    "Coverage percent here is roughly…",
                    [
                        "Bins hit divided by bins defined",
                        "Farm CPU hours only",
                        "Number of plusargs",
                        "Lines of UVM code",
                    ],
                    0,
                    "Hit bins / total bins.",
                ),
                mc(
                    "q3",
                    "The best first move on a stubborn hole is often…",
                    [
                        "A targeted sample or directed test into that bin",
                        "Forcing the clock permanently",
                        "Deleting the coverpoint",
                        "Marking sign-off READY immediately",
                    ],
                    0,
                    "Target the hole; don’t only add noise.",
                ),
                tf(
                    "q4",
                    "A value outside named bins is a modeling choice—not automatically the same as a hole.",
                    True,
                    "Holes are about defined bins.",
                ),
            ],
        ),
    )
)

MODULES.append(
    (
        "module05-coverage-closure",
        """
# Module 05 — Coverage closure

**Module id:** module05-coverage-closure
**Lab:** coverage-closure
**Tracks:** A (planning docs) · B (browser lab)

## Slide 1 — Coverage closure

Finding holes is not closing them. Closure means pairing each open bin with a next-test idea, running or planning that idea, then marking the hole closed when evidence lands. Without the pair, status meetings turn into wishful percentages.

## Slide 2 — Hole plus next-test idea

A good idea names how you will hit the hole—directed mid samples, drive an error opcode once, push FIFO until full. Generic “more random” is weak when the hole needs a directed hit. Mismatch means the idea targets the wrong hole. Need-idea means you have not planned the next move.

## Slide 3 — Browser lab

![Lab starter](assets/lab-starter.png)

In the coverage-closure lab, load the starter where mid is open and the idea is directed mid samples—ready. Try mismatch and orphan presets. Plan a next test, then mark a hole closed only when the story matches. Challenges punish vague random and reward targeted plans.

## Slide 4 — Planning docs practice

Pick three holes from a tiny cover sketch. Write one next-test idea per hole in a table. Star any idea that is only “run more random” and rewrite it to name the bin or corner you will force.

## Slide 5 — Pitfalls to watch

Do not mark closed without evidence. Do not paste one generic idea onto every hole. Do not ignore mismatch between idea and hole. And do not confuse board ready with silicon sign-off—this is closure hygiene, not a tapeout stamp.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. Pair one hole with a concrete next-test idea, then take the quiz and continue to risk-based planning.
""",
        q(
            "module05-coverage-closure",
            "Coverage closure",
            [
                mc(
                    "q1",
                    "Coverage closure pairs…",
                    [
                        "Each hole with a next-test idea, then evidence before marking closed",
                        "Only seeds with farm hostnames",
                        "Only waivers with git blame",
                        "Only P cells with C cells automatically",
                    ],
                    0,
                    "Hole + idea + evidence.",
                ),
                mc(
                    "q2",
                    "Generic “more random” against a directed hole is…",
                    [
                        "Weak—often needs a targeted hit",
                        "Always the strongest closure plan",
                        "Identical to a P0 risk score",
                        "A VIP docs pack",
                    ],
                    0,
                    "WEAK when the hole needs directed stimulus.",
                ),
                mc(
                    "q3",
                    "MISMATCH in this lab means…",
                    [
                        "The next-test idea targets the wrong hole",
                        "The farm is out of licenses",
                        "Taxonomy is BALANCED",
                        "Sign-off is READY",
                    ],
                    0,
                    "Idea and hole must align.",
                ),
                tf(
                    "q4",
                    "You should mark a hole closed only when evidence matches the planned idea.",
                    True,
                    "Closure without evidence is theater.",
                ),
            ],
        ),
    )
)

MODULES.append(
    (
        "module06-risk-plan",
        """
# Module 06 — Risk-based plan

**Module id:** module06-risk-plan
**Lab:** risk-plan
**Tracks:** A (planning docs) · B (browser lab)

## Slide 1 — Risk-based plan

Bandwidth is finite. Risk-based planning scores how likely a bug class is and how bad it is if it escapes, then assigns priority: must-test now, next wave, later, or defer. Without that matrix, everything becomes P0 and nothing is.

## Slide 2 — Risk times impact

Risk is likelihood; impact is severity if it escapes silicon or a customer. High-high and medium-high often land as P0. Low-medium may be P2. Low-low can defer. Aligned means your labels match the matrix suggestion; mismatch means you called high-high a defer or left rows open.

## Slide 3 — Browser lab

![Lab starter](assets/lab-starter.png)

In the risk-plan lab, load the starter four items correctly prioritized—aligned. Reorder a high-impact UART parity item versus cosmetic idle noise. Scan the matrix when priorities fight the risk-impact product. Challenges force you to prioritize the last open row honestly.

## Slide 4 — Planning docs practice

List four bug concerns for a block you know. Score each likelihood and impact low, medium, or high, then assign P0, P1, P2, or defer. If more than half are P0, demote two with a written reason.

## Slide 5 — Pitfalls to watch

Do not mark everything P0. Do not defer high-likelihood, high-impact items because they are hard. Do not confuse taxonomy tiers with risk scores—they cooperate but are not the same. And do not skip owners on deferred items.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. Produce a small aligned priority list, then take the quiz and continue to seeds, config, and tags.
""",
        q(
            "module06-risk-plan",
            "Risk-based plan",
            [
                mc(
                    "q1",
                    "Risk in this lab means…",
                    [
                        "Likelihood a bug class appears",
                        "Only the coverage percent bar",
                        "Only the git remote name",
                        "Only VIP README length",
                    ],
                    0,
                    "Risk = likelihood.",
                ),
                mc(
                    "q2",
                    "Impact means…",
                    [
                        "Severity if the bug escapes",
                        "Number of random seeds only",
                        "Wave cursor count",
                        "Farm disk free space only",
                    ],
                    0,
                    "Impact = escape severity.",
                ),
                mc(
                    "q3",
                    "Marking every item P0 usually…",
                    [
                        "Destroys triage—nothing is prioritized",
                        "Guarantees sign-off READY",
                        "Makes taxonomy BALANCED",
                        "Fixes all flakes",
                    ],
                    0,
                    "Everything-P0 is not a plan.",
                ),
                tf(
                    "q4",
                    "High likelihood × high impact items should not be casually deferred.",
                    True,
                    "Those belong in the must-test wave.",
                ),
            ],
        ),
    )
)

MODULES.append(
    (
        "module07-seed-tags",
        """
# Module 07 — Seed / config / tags

**Module id:** module07-seed-tags
**Lab:** seed-tags
**Tracks:** A (planning docs) · B (browser lab)

## Slide 1 — Seed / config / tags

A failing random test is useless if you cannot replay it. A run card needs a seed, enough config to relaunch the same mode, and tags that place the fail on triage boards. Replayable means those fields are filled on purpose.

## Slide 2 — What belongs on the card

Seed fixes the RNG so stimulus can return. Config holds plusargs and knobs—test name, baud, modes—not seed alone. Tags label slices: smoke, nightly, flake, quarantine. Weak means you recorded a seed but not enough config to relaunch. Missing any field blocks a clean replay story.

## Slide 3 — Browser lab

![Lab starter](assets/lab-starter.png)

In the seed-tags lab, load the starter with seed forty-two, a named UART test and baud, and smoke plus nightly tags—replayable. Try a seed-only config and watch weak. Attach missing fields, then scan the card. Challenges drill what “enough config” means.

## Slide 4 — Planning docs practice

Write one run card for an imaginary fail: seed, two plusargs, and two tags. Then rewrite a bad card that only says “seed seven” and explain why a teammate could not replay it.

## Slide 5 — Pitfalls to watch

Do not file fails with seed only. Do not skip tags so flakes vanish from boards. Do not change knobs while claiming the same seed replay. And do not treat the literacy board as your company’s database—copy the habit into real tickets.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. Build one replayable run card, then take the quiz and continue to regression triage.
""",
        q(
            "module07-seed-tags",
            "Seed / config / tags",
            [
                mc(
                    "q1",
                    "A fixed seed mainly helps you…",
                    [
                        "Replay the failing stimulus",
                        "Skip writing a testbench",
                        "Auto-sign off silicon",
                        "Delete coverage holes",
                    ],
                    0,
                    "Seed → replay.",
                ),
                mc(
                    "q2",
                    "Config on the run card should include…",
                    [
                        "Plusargs / knobs that select test and DUT mode",
                        "Only the hostname of the coffee machine",
                        "Only the slide theme color",
                        "Only the waiver expiry year",
                    ],
                    0,
                    "Config relaunches the same mode.",
                ),
                mc(
                    "q3",
                    "Seed-only with no testname/config is…",
                    [
                        "WEAK for replay",
                        "Always REPLAYABLE",
                        "A sign-off criterion",
                        "A feature-matrix C cell",
                    ],
                    0,
                    "Need seed + usable config (+ tags).",
                ),
                tf(
                    "q4",
                    "Tags like smoke, nightly, or flake help triage boards bucket the fail.",
                    True,
                    "Tags place the fail in the right slice.",
                ),
            ],
        ),
    )
)

MODULES.append(
    (
        "module08-regression-triage",
        """
# Module 08 — Regression triage

**Module id:** module08-regression-triage
**Lab:** regression-triage
**Tracks:** A (planning docs) · B (browser lab)

## Slide 1 — Regression triage

Nightly noise without buckets wastes the morning. Triage sorts fails into reproducible DUT or VIP fails, flakes, first-seen new issues, and environment or infra problems. A clean board means every row has a bucket—not that bugs vanished.

## Slide 2 — Fail, flake, new, env

Fail means reproducible design, VIP, or scoreboard breakage—own and fix. Flake means intermittent or seed-sensitive—quarantine and stabilize, do not bury. New means first appearance this run—escalate; do not assume known. Env means license, disk, tool, or farm crash—infra, not RTL.

## Slide 3 — Browser lab

![Lab starter](assets/lab-starter.png)

In the regression-triage lab, load the starter with three fails already bucketed—board clean. Open a row, triage it, and scan until open count is zero. Try an environment hit preset. Challenges stop you from leaving rows unlabeled.

## Slide 4 — Planning docs practice

Take three fictional nightly lines and assign fail, flake, new, or env with one-line reasons. Mark which one you would debug first and why. Optional: note which seed-tag fields you would demand on the flake.

## Slide 5 — Pitfalls to watch

Do not mark everything flake to clear the board. Do not treat env red as a DUT bug. Do not ignore new fails because the night was busy. And do not close triage without an owner on real fails.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. Bucket a small board to clean, then take the quiz and continue to verification metrics.
""",
        q(
            "module08-regression-triage",
            "Regression triage",
            [
                mc(
                    "q1",
                    "A reproducible DUT/VIP/scoreboard break should be bucketed as…",
                    [
                        "fail",
                        "env only",
                        "always waive",
                        "feature-matrix P",
                    ],
                    0,
                    "Reproducible design/VIP issues → fail.",
                ),
                mc(
                    "q2",
                    "Intermittent seed-sensitive timeouts are often…",
                    [
                        "flake — quarantine and stabilize",
                        "automatic sign-off READY",
                        "proof of 100% coverage",
                        "VIP docs_pack complete",
                    ],
                    0,
                    "Flakes need quarantine, not burial.",
                ),
                mc(
                    "q3",
                    "Farm license or tool crashes belong in…",
                    [
                        "env — infrastructure, not design",
                        "corner taxonomy only",
                        "cover bins mid",
                        "P0 risk forever without looking",
                    ],
                    0,
                    "Env ≠ DUT fail.",
                ),
                tf(
                    "q4",
                    "A CLEAN triage board means every row is bucketed—not that all bugs are fixed.",
                    True,
                    "Clean = labeled; fix work still follows.",
                ),
            ],
        ),
    )
)

MODULES.append(
    (
        "module09-verif-metrics",
        """
# Module 09 — Verification metrics

**Module id:** module09-verif-metrics
**Lab:** verif-metrics
**Tracks:** A (planning docs) · B (browser lab)

## Slide 1 — Verification metrics

Plans need numbers that leadership and engineers share. Common bars: regression pass rate, plan or functional coverage percent, and severe bug escapes. Healthy means every metric meets its bar. Blocked means an escape bar was broken. Open means you are under on pass or coverage.

## Slide 2 — Bars that matter

Pass rate below the bar means instability—you cannot trust green stories. Coverage percent below goal means unfinished plan risk. Bug escapes above zero at a sev-one bar usually stop the gate. Levels good, warn, and bad are how you talk without drowning in raw dumps.

## Slide 3 — Browser lab

![Lab starter](assets/lab-starter.png)

In the metrics lab, load the starter with strong pass rate, coverage, and zero escapes—healthy. Drop pass rate or raise escapes and scan the board. Challenges show how one escape can block the story even if coverage looks fine.

## Slide 4 — Planning docs practice

Write three metric names with a numeric bar each for a fictional milestone. Mark today’s sample good, warn, or bad. If any is bad, write the first action you would take this week.

## Slide 5 — Pitfalls to watch

Do not call the program healthy because CI ran once. Do not ignore escape counts when coverage is high. Do not change bars silently mid-milestone. And do not track twenty vanity metrics—three honest bars beat a dashboard museum.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. Set or interpret three bars, then take the quiz and continue to CI and farm flow.
""",
        q(
            "module09-verif-metrics",
            "Verification metrics",
            [
                mc(
                    "q1",
                    "A typical sev-1 bug-escape bar is…",
                    [
                        "Zero escapes for the milestone",
                        "At least ten escapes to prove testing",
                        "Identical to taxonomy BALANCED",
                        "Only the number of wave cursors",
                    ],
                    0,
                    "Escapes bar is usually zero.",
                ),
                mc(
                    "q2",
                    "Low regression pass rate mainly signals…",
                    [
                        "Instability—hard to trust results",
                        "Automatic VIP handoff READY",
                        "That seeds are unnecessary",
                        "That risk planning is done",
                    ],
                    0,
                    "Pass rate = stability of the suite.",
                ),
                mc(
                    "q3",
                    "HEALTHY in this lab means…",
                    [
                        "Pass rate, coverage, and escapes all meet their bars",
                        "One local smoke passed once",
                        "All cells are P only",
                        "All fails marked flake",
                    ],
                    0,
                    "All tracked bars met.",
                ),
                tf(
                    "q4",
                    "A bug-escape breach can BLOCK the metrics board even if coverage percent looks high.",
                    True,
                    "Escapes are a hard gate in the lab model.",
                ),
            ],
        ),
    )
)

MODULES.append(
    (
        "module10-ci-farm-flow",
        """
# Module 10 — CI / farm flow

**Module id:** module10-ci-farm-flow
**Lab:** ci-farm-flow
**Tracks:** A (planning docs) · B (browser lab)

## Slide 1 — CI / farm flow

Verification scales in stages: local smoke on a laptop, CI as the merge or scheduled gate, then the farm for scale-out regression and soak. Ready means each stage you claim is green in order. Skipping a stage or promoting past a red gate breaks trust.

## Slide 2 — Local, CI, farm

Local is fast sanity before push. CI is the agent gate—pull request or nightly slice. Farm is where long regressions and stress live. Pass advances; fail blocks; open means not run; skip gaps the chain. A green farm with a failed local or skipped CI is not an honest ready flow.

## Slide 3 — Browser lab

![Lab starter](assets/lab-starter.png)

In the CI-farm lab, load the starter with local, CI, and farm all pass—ready. Try local fail or skip CI presets and watch blocked or gapped. Set stages deliberately, then scan the flow. Challenges punish promoting past red.

## Slide 4 — Planning docs practice

Draw three boxes—local, CI, farm—and write what runs in each for your team. Mark yesterday’s real or fictional status pass, fail, open, or skip. If any is fail or skip, write the promotion rule you would enforce.

## Slide 5 — Pitfalls to watch

Do not skip CI because the farm is “more complete.” Do not ignore local reds. Do not treat one green farm night as a full flow. And do not forget that seed and triage habits feed every stage—flow without replay is archaeology.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. Describe or set a clean local-to-farm chain, then take the quiz and continue to sign-off.
""",
        q(
            "module10-ci-farm-flow",
            "CI / farm flow",
            [
                mc(
                    "q1",
                    "The staged flow in this lab is…",
                    [
                        "Local → CI → farm",
                        "Only wave → force → waive",
                        "Only docs → API → self-test",
                        "Only feature → scenario without coverage",
                    ],
                    0,
                    "Local smoke, CI gate, farm scale-out.",
                ),
                mc(
                    "q2",
                    "Skipping CI while claiming farm green typically…",
                    [
                        "Gaps the chain — not a full READY flow",
                        "Is required for sign-off",
                        "Makes metrics HEALTHY automatically",
                        "Replaces triage buckets",
                    ],
                    0,
                    "Skip → GAPPED.",
                ),
                mc(
                    "q3",
                    "A failed local stage should…",
                    [
                        "Block promotion to later stages",
                        "Be ignored if farm is green",
                        "Delete coverage holes",
                        "Auto-waive sev-1 bugs",
                    ],
                    0,
                    "Fail → BLOCKED promotion.",
                ),
                tf(
                    "q4",
                    "Local is for fast sanity before push; farm is for scale-out regression and soak.",
                    True,
                    "Different stages, different jobs.",
                ),
            ],
        ),
    )
)

MODULES.append(
    (
        "module11-signoff-checklist",
        """
# Module 11 — Sign-off checklist

**Module id:** module11-signoff-checklist
**Lab:** signoff-checklist
**Tracks:** A (planning docs) · B (browser lab)

## Slide 1 — Sign-off checklist

Sign-off is a gate, not a vibe. Typical criteria: coverage goal met with no open P0 holes, bug bar clear—often zero sev-one blockers—and a stability window of green nights or an agreed flake bar. Ready means evidence for each criterion, or a documented waiver with owner and expiry.

## Slide 2 — Met, open, fail, waived

Met means evidence exists. Open means not demonstrated yet. Fail means the criterion is broken—such as a sev-one still open—and the gate is blocked. Waived means a written exception with owner; it can count as closed for ready, but it is not invisible.

## Slide 3 — Browser lab

![Lab starter](assets/lab-starter.png)

In the sign-off lab, load the starter with coverage goal, bug bar, and stability all met—gate ready. Try coverage gap or bug fail presets. Check items off only with a story of evidence. Challenges show that a waived stability line can still be ready when policy allows.

## Slide 4 — Planning docs practice

Write three exit criteria for a milestone. For each, note what evidence you would attach and who owns a waiver if needed. If any criterion is fail, write what would unblock the gate.

## Slide 5 — Pitfalls to watch

Do not silent-skip failed criteria. Do not waive without owner, reason, and expiry. Do not sign off on coverage percent alone while sev-ones remain. And do not confuse this literacy checklist with your company’s legal release process—map the ideas, then use the real form.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. Walk one gate to ready or name what blocks it, then take the quiz and continue to VIP handoff.
""",
        q(
            "module11-signoff-checklist",
            "Sign-off checklist",
            [
                mc(
                    "q1",
                    "Common sign-off criteria in this lab include…",
                    [
                        "Coverage goal, bug bar, and stability window",
                        "Only font choice on slides",
                        "Only number of hierarchy panes",
                        "Only taxonomy skew",
                    ],
                    0,
                    "Coverage, bugs, stability.",
                ),
                mc(
                    "q2",
                    "An open sev-1 against the DUT typically…",
                    [
                        "Fails the bug bar and BLOCKS the gate",
                        "Is ignored if coverage is high",
                        "Makes CI skip required",
                        "Counts as VIP self-test",
                    ],
                    0,
                    "Bug bar breach → BLOCKED.",
                ),
                mc(
                    "q3",
                    "A waiver at sign-off should include…",
                    [
                        "Owner, reason, and expiry—not a silent skip",
                        "Only a thumbs-up emoji",
                        "Only a random seed",
                        "Only a feature-matrix dash",
                    ],
                    0,
                    "Documented waiver with ownership.",
                ),
                tf(
                    "q4",
                    "READY means each criterion is met or properly waived with evidence.",
                    True,
                    "Gate hygiene, not vibes.",
                ),
            ],
        ),
    )
)

MODULES.append(
    (
        "module12-vip-handoff",
        """
# Module 12 — VIP handoff

**Module id:** module12-vip-handoff
**Lab:** vip-handoff
**Tracks:** A (planning docs) · B (browser lab)

## Slide 1 — VIP handoff

A VIP is not handed off when the agent compiles once. Handoff readiness means consumers can onboard: a docs pack, a clear API surface, and a standalone self-test that proves the VIP runs. Missing any piece blocks a responsible transfer.

## Slide 2 — Docs, API, self-test

Docs pack means README, quickstart, examples, and known limits. API surface means sequences, config knobs, callbacks, and the interface contract are documented. Self-test means a shipped smoke or self-check that runs without the integrator’s full SoC. Met, open, fail, and waived work like the sign-off gate.

## Slide 3 — Browser lab

![Lab starter](assets/lab-starter.png)

In the VIP-handoff lab, load the starter with docs, API, and self-test met—handoff ready. Try docs gap or self-test fail presets. Check off the last open deliverable only when you can point to evidence. Challenges show a red self-test blocks ready.

## Slide 4 — Planning docs practice

For a fictional UART VIP, list the three deliverables and one artifact name under each. Mark any gap you would refuse to hand off with. Optional: note which protocol course module already practiced VIP anatomy so this handoff checklist has teeth.

## Slide 5 — Pitfalls to watch

Do not ship without a self-test. Do not call undocumented knobs an API. Do not waive docs silently. And do not confuse handoff ready with chip sign-off—the VIP can be ready while the SoC gate is still open.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. Drive a handoff board to ready or name the blocker, then take the quiz and continue to the wrap.
""",
        q(
            "module12-vip-handoff",
            "VIP handoff",
            [
                mc(
                    "q1",
                    "VIP handoff deliverables in this lab are…",
                    [
                        "Docs pack, API surface, and self-test",
                        "Only local → CI → farm",
                        "Only cover bins low/mid/high",
                        "Only flake quarantine tags",
                    ],
                    0,
                    "Docs, API, self-test.",
                ),
                mc(
                    "q2",
                    "A docs pack should help consumers…",
                    [
                        "Onboard via README, quickstart, examples, and known limits",
                        "Force clocks in production silicon",
                        "Skip all coverage goals",
                        "Ignore triage forever",
                    ],
                    0,
                    "Docs enable onboarding.",
                ),
                mc(
                    "q3",
                    "A failing standalone self-test…",
                    [
                        "BLOCKS handoff READY",
                        "Is required for READY",
                        "Replaces the need for API docs",
                        "Means taxonomy is SKEWED only",
                    ],
                    0,
                    "Self-test red → BLOCKED.",
                ),
                tf(
                    "q4",
                    "VIP handoff READY is not the same thing as full chip sign-off.",
                    True,
                    "Different gates; VIP can be ready earlier.",
                ),
            ],
        ),
    )
)

MODULES.append(
    (
        "module13-wrap",
        """
# Module 13 — Planning path complete

**Module id:** module13-wrap
**Lab:** none (wrap)
**Tracks:** A · B recap

## Slide 1 — Planning path complete

You now have a working map of verification planning and management: traceability from feature to coverage, taxonomy and matrices, bins and closure, risk and replay cards, triage and metrics, CI-to-farm flow, sign-off criteria, and VIP handoff. Protocol and UVM courses build engines; you learned how to plan, measure, and gate them.

## Slide 2 — Skills you can reuse

Write plans others can audit. Prefer measurable coverage claims over test-name lists. Mix test tiers on purpose. Close holes with next-test ideas. Prioritize by risk and impact. File fails with seed, config, and tags. Bucket nightly noise. Track a few honest bars. Promote only through honest stages. Sign off with evidence or owned waivers.

## Slide 3 — Dual-track recap

![Tools index](assets/tools-index.png)

If you mainly used browser boards, take one checklist or matrix into markdown for a real block. If you mainly wrote docs, revisit any planning lab for graded challenges. Either way, keep the vocabulary shared with your team.

## Slide 4 — Where to go next

Return to UART, SPI, or I²C to attach plans to protocol work. Deepen UVM and pyuvm when you need stronger TB engines. Use HDL simulator, Icarus, or Verilator courses when execution fidelity is the bottleneck. Climb the syllabus ladder for the gap you feel most.

## Slide 5 — Mindset to keep

Plans without coverage claims are theater. Coverage without closure actions stalls. Metrics without triage lie. Sign-off without evidence is hope. Small, maintained artifacts beat giant unread spreadsheets.

## Slide 6 — Closing

Check off the wrap checklist. You finished the verification planning and management path. Pick one real project artifact to improve this week—a matrix row, a run card, or a sign-off line—then continue to the next course that matches your goal.
""",
        q(
            "module13-wrap",
            "Planning path complete",
            [
                mc(
                    "q1",
                    "After this course you should be able to…",
                    [
                        "Plan, measure, triage, and gate verification with shared vocabulary",
                        "Skip all coverage and only wave poke",
                        "Replace every protocol course",
                        "Ignore seeds and tags forever",
                    ],
                    0,
                    "Planning/management literacy outcomes.",
                ),
                mc(
                    "q2",
                    "A durable habit from this path is…",
                    [
                        "Feature→scenario→coverage traceability and evidence-based gates",
                        "Marking every fail as flake",
                        "Skipping CI always",
                        "Waiving without owners",
                    ],
                    0,
                    "Traceability + evidence.",
                ),
                mc(
                    "q3",
                    "If you mostly used browser labs, a good wrap action is…",
                    [
                        "Turn one board into a markdown artifact for a real block",
                        "Delete all metrics bars",
                        "Force-clock every net",
                        "Avoid VIP docs",
                    ],
                    0,
                    "Transfer literacy into lasting docs.",
                ),
                tf(
                    "q4",
                    "Sign-off without evidence is hope—not a gate.",
                    True,
                    "Evidence or owned waiver.",
                ),
            ],
        ),
    )
)


def main() -> None:
    for module, transcript, quiz in MODULES:
        write(module, transcript, quiz)
    print("done", len(MODULES), "modules")


if __name__ == "__main__":
    main()
