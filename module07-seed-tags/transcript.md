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
