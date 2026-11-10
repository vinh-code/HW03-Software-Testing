# Task 1 — execution and reproduction

## Verified results

58 checks executed: 30 Passed, 28 Failed, grouped into 23 findings (19 specification violations, 4 additional UX findings). Actual browser runs on 2026-11-10 UTC, Linux x86_64, Chrome headless 156.0.8078.79. Browser locale en-US; default viewport 1366x900; responsive check 360x800. No physical mobile or three-platform completion is claimed.

## Files

- `../checklist/task1_design.json`: reviewed criteria and reasons for AI additions.
- `evidence/results.json`: per-check timestamps, actual observations, alert messages, browser version.
- `evidence/fixture.json`: test-only user/order IDs.
- `../bugs/`: 23 reproducible issue bodies and 28 genuine screenshots of failed items.
- `scripts/`: executable Playwright CLI snippets and report generator.

## Safe setup and replay

Run from HW03 root. Existing servers at localhost:3000, :5173, :5174 were reused. Source code was not patched. Do not use `sut/run_servers.sh` (hardcoded unrelated paths and killall node). Do not restart backend without preserving database: its imported database.js resets data on startup.

1. Back up `sut/backend/database.sqlite` with SQLite backup API. The first-run backup is `/tmp/hw03-task1-before/database.sqlite` (machine-local, outside submission).
2. `python3 submission/task1/scripts/seed_fixture.py` creates/resets only task1-* fixture accounts/orders. It never represents real usability participants.
3. `bash /home/pham-quang-vinh/.codex/skills/playwright/scripts/playwright_cli.sh -s=hw03 open http://localhost:5173/login`
4. Use `scripts/run_suite.py` for a complete replay. It reseeds fixtures, assembles CLI scripts with current fixture IDs, and collects actual returned JSON. It explicitly resets the two fixture orders between profile and admin phases.
5. `python3 submission/checklist/build_checklist.py` rebuilds Excel/Markdown/bug bodies from recorded results; it does not rerun tests.

## Evidence limitations

- Screenshots are captured only for Failed checklist items. Native alerts are recorded in JSON and accepted by the automation; screenshots show the underlying page after alert dismissal. No synthetic dialog is drawn.
- Loading and HTTP 500 checks use controlled network interception. Other runs use the real local API/database.
- Benign `<b>` payloads show HTML rendering only; no script execution or broader exploit is claimed.
- Date/currency formatting was observed under en-US locale. Currency criterion checks separators and ₫; it does not falsely assert Vietnamese date formatting.
- Failed automation attempts (a selector matching an unopened admin heading, and a Tab action before render) were corrected before accepting final results. No timeout was counted as an application bug.
- Git history begins with preserved templates and records this actual testing session. It does not reconstruct earlier work.

## Remaining student/external actions

Human review is mandatory. AI-added criteria must not be represented as student-authored without actual student changes. 23 findings have been published with screenshot links at https://github.com/vinh-code/HW03-Software-Testing/issues. Student ID: 23120202; email: 23120202@student.hcmus.edu.vn. Task 2 and Task 3 remain separate unfinished tasks.
