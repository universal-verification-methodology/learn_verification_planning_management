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
