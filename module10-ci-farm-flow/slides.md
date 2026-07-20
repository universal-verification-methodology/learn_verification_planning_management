---
marp: true
title: CI / farm flow
paginate: true
---

# CI / farm flow

Verification scales in stages

---

## Local, CI, farm
- Local is fast sanity before push
- CI is the agent gate, pull request or nightly slice
- Farm is where long regressions and stress live
- Pass advances; fail blocks; open means not run; skip gaps the chain
- A green farm with a failed local or skipped CI is not an honest ready flow

---

## Browser lab
![Lab starter](assets/lab-starter.png)

---

## Planning docs practice
- Draw three boxes, local, CI, farm, and write what runs in each for your team
- Mark yesterday’s real or fictional status pass, fail, open, or skip
- If any is fail or skip, write the promotion rule you would enforce

---

## Pitfalls to watch
- Do not skip CI because the farm is “more complete.” Do not ignore local reds
- Do not treat one green farm night as a full flow
- And do not forget that seed and triage habits feed every stage

---

## Your turn
- Complete the checklist for at least one track, preferably both
- Describe or set a clean local-to-farm chain, then take the quiz and continue to sign-off

