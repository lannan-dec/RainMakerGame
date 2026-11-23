# Plan (feature): bootstrap proof, first smoke test
Status: done 2026-11-23. Departures: the plan file lists tests/test_smoke.py as the only new file, and one workflow edit (`permissions: contents: read`, from the security check) was added inside the declared Surface. The person's "go" in the step 9 question stood in for the plan approval and the grill-me pass.

Acceptance criteria: CI job `gates` goes green on the bootstrap pull request, and `coverage.xml` exists so `python scripts/harness_lint.py --ratchet --update-baseline` can set the first floors. Verified by `gh pr checks` and a non-null `coverage_baseline.json`.
Surface: tests/test_smoke.py, plus the whole harness bootstrap (AGENTS.md, CLAUDE.md, GEMINI.md, NEXT-STEPS.md, coverage_baseline.json, skills-lock.json, .agents/, .agent, .claude, .githooks/, .github/, .gitattributes, .gitignore, _bmad/, docs/, scripts/) copied or written by BOOTSTRAP.md steps 2 to 8.
Design: one pytest file asserting that the concept document `docs/Rainmaker_The_Campaign.txt` exists and is non-empty. No new module, dependency or abstraction: pytest and pytest-cov are already named by the CI step.
Test plan: unit `tests/test_smoke.py::test_concept_document_present`; e2e n/a: no application exists; regression test n/a: not a bugfix, but the test is seen red by temporarily moving the document.
Architecture map delta: yes, add `tests/` to the layout table. ADR: no (ADR-0001 already records adopting the harness).
Cross-repo impact: none.
Open questions: grill-me was satisfied by the person approving push, pull request and merge in the step 9 question; recommended answer taken: proceed.
BACKLOG: the eight retired BMAD skills remain in `.agents/skills/` (person chose to keep them); `prepush_check.py --self-test` has one expected FAIL (`logo.png` fixture) because image extensions are in `SKIP`; pin `pytest` and `pytest-cov` in CI once a requirements file exists.
