# Architecture map

last_reviewed: 2026-11-23

The one living map of this repository: components, flows, boundaries and invariants. Read it before touching unfamiliar code; update it in the same change that moves structure (`harness-close` step 3). It describes this repository only. Each invariant cites the defect or decision that bought it. Factual claims carry a `verify:` line so the lint fails on the commit that makes them false.

## What this repository is

Rainmaker: The Campaign is a facilitated tabletop business simulation, with an AI coach and fictional-client engine, that develops consultants' rainmaking judgement. It is for a Campaign Director running four to six participant-consultants through a persistent campaign; today the repository holds the concept document and the agentic harness only.

## Layout

| Path | Holds | Owner doc or skill |
|---|---|---|
| `docs/` | Concept document for the game | `docs/Rainmaker_The_Campaign.txt` |
| `tests/` | Smoke test proving CI, coverage and the ratchet work | `AGENTS.md` Part B (test command) |
| `scripts/` | Harness lint, transcript saver and push guard | `AGENTS.md` Part A section 6 |
| `.agents/skills/` | Installed skills, pinned in `skills-lock.json` | `AGENTS.md` Part A section 1 |
| `_bmad/` | BMAD configuration and overrides | `AGENTS.md` Part A section 1 |

## Flows

1. Harness loop: `harness-open` -> `harness-plan` -> implement -> `harness-close`. Files: `.agents/skills/`.

## Boundaries and invariants

- **Concept before code.** No application stack is chosen; the game design lives in `docs/Rainmaker_The_Campaign.txt` and its mechanics are unverified against the book. Bought by: the concept document's own note that framework labels need author verification.
  <!-- verify: exists docs/Rainmaker_The_Campaign.txt -->
  <!-- verify: exists tests/test_smoke.py -->
  <!-- verify: exists AGENTS.md -->
  <!-- verify: exists docs/adr/README.md -->
  <!-- verify: exists docs/memory/MEMORY.md -->
  <!-- verify: exists docs/sessions/README.md -->
  <!-- verify: exists scripts/harness_lint.py -->
  <!-- verify: exists scripts/save_transcript.py -->
  <!-- verify: exists .githooks/pre-commit -->
  <!-- verify: exists .githooks/pre-push -->
  <!-- verify: exists .github/workflows/harness-gates.yml -->

## Deliberately not built yet

- Application code and a test suite: add when a stack is chosen and the first feature is planned.
- AI coach and client-profile engine: add when the BMAD brief and architecture for the game are written.
