# learn_verification_planning_management

[![GitHub](https://img.shields.io/badge/GitHub-learn__verification__planning__management-181717?logo=github)](https://github.com/universal-verification-methodology/learn_verification_planning_management)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-green?logo=creativecommons&logoColor=white)](LICENSE)
[![Role](https://img.shields.io/badge/role-Git%20submodule-orange)](https://github.com/universal-verification-methodology/learning)
[![Parent](https://img.shields.io/badge/parent-learning%20monorepo-0A9EDC)](https://github.com/universal-verification-methodology/learning)
[![Labs](https://img.shields.io/badge/labs-GitHub%20Pages-222?logo=githubpages)](https://universal-verification-methodology.github.io/learning/tools/)
[![Domain](https://img.shields.io/badge/domain-verification%20planning%20%7C%20coverage%20%7C%20sign--off-purple)](https://github.com/universal-verification-methodology/learn_verification_planning_management)

**learn_verification_planning_management** is the open learning path for *plan → coverage → regression → sign-off*.

Authors rebuild slides/audio with **module-slides** in the parent monorepo. Reference materials: [`verification_planning_management`](./).

## Table of contents

- [Contents](#contents)
- [Browse or clone](#browse-or-clone)
- [Author: module-slides](#author-module-slides)
- [Two learning tracks](#two-learning-tracks)
- [Module landings](#module-landings)
- [Browser labs](#browser-labs)
- [License](#license)

## Contents

```text
learn_verification_planning_management/
├── README.md
├── LICENSE
├── docs/
│   ├── MODULES.md
│   └── TWO_TRACKS.md
├── scripts/
│   └── module.sh
├── module00-intro/
├── module01-verif-plan-check/
├── …
└── module13-wrap/
```

## Browse or clone

- **Browser labs:** [tools/#verif-plan](https://universal-verification-methodology.github.io/learning/tools/#verif-plan)
- **Syllabus:** [`syllabus.md` § planning](https://github.com/universal-verification-methodology/learning/blob/main/syllabus.md#14-learn_verification_planning_management)

```bash
git clone --recurse-submodules \
  git@github.com:universal-verification-methodology/learning.git
ls courses/learn_verification_planning_management
./scripts/module.sh 01 --check
```

## Author: module-slides

```bash
cd ../..   # monorepo root
python .cursor/skills/module-slides/scripts/transcript_to_outline.py \
  courses/learn_verification_planning_management/module01-verif-plan-check
bash .cursor/skills/module-slides/scripts/narrate_clips.sh \
  courses/learn_verification_planning_management/module01-verif-plan-check
```

## Two learning tracks

Details: [docs/TWO_TRACKS.md](docs/TWO_TRACKS.md).

| Track | Practice surface | Start here |
|-------|------------------|------------|
| **A — Planning docs** | Paper · [`../verification_planning_management`](./) | [docs/TWO_TRACKS.md](docs/TWO_TRACKS.md) |
| **B — Browser lab** | Planning boards | [verif-plan-check](https://universal-verification-methodology.github.io/learning/tools/verif-plan-check/) |

Lab status snapshot: **12 shipped** (see [docs/MODULES.md](docs/MODULES.md)).

## Module landings

Full status table: **[docs/MODULES.md](docs/MODULES.md)**.

| Module | Landing |
|--------|---------|
| 00 — Welcome to verification planning | [module00-intro](module00-intro/README.md) |
| 01 — Coverage / plan checklist | [module01-verif-plan-check](module01-verif-plan-check/README.md) |
| 02 — Test taxonomy | [module02-test-taxonomy](module02-test-taxonomy/README.md) |
| 03 — Feature × scenario matrix | [module03-feature-matrix](module03-feature-matrix/README.md) |
| 04 — Cover bins sketch | [module04-cover-bins](module04-cover-bins/README.md) |
| 05 — Coverage closure | [module05-coverage-closure](module05-coverage-closure/README.md) |
| 06 — Risk-based plan | [module06-risk-plan](module06-risk-plan/README.md) |
| 07 — Seed / config / tags | [module07-seed-tags](module07-seed-tags/README.md) |
| 08 — Regression triage | [module08-regression-triage](module08-regression-triage/README.md) |
| 09 — Verification metrics | [module09-verif-metrics](module09-verif-metrics/README.md) |
| 10 — CI / farm flow | [module10-ci-farm-flow](module10-ci-farm-flow/README.md) |
| 11 — Sign-off checklist | [module11-signoff-checklist](module11-signoff-checklist/README.md) |
| 12 — VIP handoff | [module12-vip-handoff](module12-vip-handoff/README.md) |
| 13 — Planning path complete | [module13-wrap](module13-wrap/README.md) |

## Browser labs

**Shipped:** [verif-plan-check](https://universal-verification-methodology.github.io/learning/tools/verif-plan-check/) · [test-taxonomy](https://universal-verification-methodology.github.io/learning/tools/test-taxonomy/) · [feature-matrix](https://universal-verification-methodology.github.io/learning/tools/feature-matrix/) · [cover-bins](https://universal-verification-methodology.github.io/learning/tools/cover-bins/) · [coverage-closure](https://universal-verification-methodology.github.io/learning/tools/coverage-closure/) · [risk-plan](https://universal-verification-methodology.github.io/learning/tools/risk-plan/) · [seed-tags](https://universal-verification-methodology.github.io/learning/tools/seed-tags/) · [regression-triage](https://universal-verification-methodology.github.io/learning/tools/regression-triage/) · [verif-metrics](https://universal-verification-methodology.github.io/learning/tools/verif-metrics/) · [ci-farm-flow](https://universal-verification-methodology.github.io/learning/tools/ci-farm-flow/) · [signoff-checklist](https://universal-verification-methodology.github.io/learning/tools/signoff-checklist/) · [vip-handoff](https://universal-verification-methodology.github.io/learning/tools/vip-handoff/).

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — see [`LICENSE`](LICENSE).
