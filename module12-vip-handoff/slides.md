---
marp: true
title: VIP handoff
paginate: true
---

# VIP handoff

A VIP is not handed off when the agent compiles once

---

## Docs, API, self-test
- Docs pack means README, quickstart, examples, and known limits
- API surface means sequences, config knobs, callbacks
- Self-test means a shipped smoke or self-check that runs without the integrator’s full SoC
- Met, open, fail, and waived work like the sign-off gate

---

## Browser lab
![Lab starter](assets/lab-starter.png)

---

## Planning docs practice
- For a fictional UART VIP, list the three deliverables and one artifact name under each
- Mark any gap you would refuse to hand off with
- Optional: note which protocol course module already practiced VIP anatomy so this handoff

---

## Pitfalls to watch
- Do not ship without a self-test
- Do not call undocumented knobs an API
- Do not waive docs silently
- And do not confuse handoff ready with chip sign-off

---

## Your turn
- Complete the checklist for at least one track, preferably both
- Drive a handoff board to ready or name the blocker

