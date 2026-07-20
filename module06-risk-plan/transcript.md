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
