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
