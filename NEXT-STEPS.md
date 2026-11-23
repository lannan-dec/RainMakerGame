# NEXT-STEPS

Rewritten at every `harness-close`. Assume the next session knows nothing that is not written here. Read this after `docs/memory/MEMORY.md` and `docs/ARCHITECTURE.md`. Plans in `docs/plans/` are dated snapshots of intent; this file is the current state. If they disagree, this file is right.

## What is true now (measured 2026-11-23)

- Harness bootstrap steps 0 to 9 are done locally; the proof is the pull request from branch `bootstrap-harness` into `main`. Proof: `gh pr list` and `docs/sessions/session_2611231441.md`.
- `python scripts/harness_lint.py` reports 0 errors and 2 third-party size warnings (`bmad-facilitate`, `bmad-spec`).
- `main` on lannan-dec/RainMakerGame is protected: required check `gates`, admins included, so every change goes through a pull request. Proof: `gh api repos/lannan-dec/RainMakerGame/branches/main/protection`.
- One test exists (`tests/test_smoke.py`); `coverage_baseline.json` has null floors until the first green CI run, then `--ratchet --update-baseline` sets them.
- Eight retired BMAD skills remain in `.agents/skills/` (listed in the session log); the person chose to keep them.

## Step 0: re-verify before acting on anything above

1. `python scripts/harness_lint.py`
2. `git status --short && git log --oneline -3`
3. `git config core.hooksPath && ls -l .githooks` (want `.githooks`, both hooks executable)

## Open threads

- Coverage baseline: after the bootstrap pull request merges, run `python scripts/harness_lint.py --ratchet --update-baseline` against a fresh `coverage.xml` and commit `coverage_baseline.json` through a pull request.
- Stack choice: undecided; run the BMAD brief, PRD and architecture skills before cutting stories.
- Retired BMAD skills: remove with `setup.py --remove-retired` only on the person's approval.
- CI pins: pin `pytest` and `pytest-cov` once a requirements file exists.

## Traps, in the order they will bite

1. `.githooks/*` must stay executable; git silently skips a non-executable hook.
2. `python scripts/prepush_check.py --self-test` fails falsely in a sandbox and has one expected FAIL (`logo.png` fixture) outside it.
3. Non-interactive shells need `/opt/homebrew/opt/python@3.15/libexec/bin` on PATH for `python`; pytest runs locally only through `uv run --with pytest --with pytest-cov`.

## Kickoff text (paste into the next session)

> Read NEXT-STEPS.md in full, then AGENTS.md, then docs/memory/MEMORY.md, then docs/ARCHITECTURE.md. Run harness-open. Then: confirm the bootstrap pull request merged, set the coverage baseline, and start the BMAD product brief for Rainmaker: The Campaign.
