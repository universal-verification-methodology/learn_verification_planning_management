---
marp: true
title: Regression triage
paginate: true
---

# Regression triage

Nightly noise without buckets wastes the morning

---

## Fail, flake, new, env
- Fail means reproducible design, VIP, or scoreboard breakage, own and fix
- Flake means intermittent or seed-sensitive, quarantine and stabilize, do not bury
- New means first appearance this run, escalate; do not assume known
- Env means license, disk, tool, or farm crash, infra, not RTL

---

## Browser lab
![Lab starter](assets/lab-starter.png)

---

## Planning docs practice
- Take three fictional nightly lines and assign fail
- Mark which one you would debug first and why
- Optional: note which seed-tag fields you would demand on the flake

---

## Pitfalls to watch
- Do not mark everything flake to clear the board
- Do not treat env red as a DUT bug
- Do not ignore new fails because the night was busy
- And do not close triage without an owner on real fails

---

## Your turn
- Complete the checklist for at least one track, preferably both
- Bucket a small board to clean, then take the quiz and continue to verification metrics

