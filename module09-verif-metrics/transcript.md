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
