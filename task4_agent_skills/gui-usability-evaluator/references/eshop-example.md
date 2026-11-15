# EShop coursework adapter

This is an example mapping, not a universal screen model.

- Assignment: `2026.HW03.GUI Usability_En.md` in HW03 root.
- Reviewed checklist: `submission/checklist/task1_design.json`.
- Login-specific executable steps: `submission/task1/scripts/login.body.js` (GUI-001…016). Adapt credentials and output paths; do not import previously recorded outcomes as a new execution.
- Original SUT backend binds :3000 and imports `database.js`, which drops/reseeds tables. Source and old SQLite evidence must be preserved when restarting for a demo.
- Frontend uses localhost :3000 directly; if using an isolated backend copy, ensure that port is free. Serve the original frontend at :5173 without modifying application behaviour.
- Use a dedicated `skill-demo-*` account in the isolated database; UI screenshots may include only this demo password.
- Existing Task 1 issues may be linked from `submission/task1/evidence/issues.json`. A new demo should not create another copy of an already reported defect.
- Task 2's `submission/usability/data/simulation.json` is explicitly simulated. It is suitable for demonstrating the analysis helper, not evidence of seven real people.

For reuse on another screen, retain the evidence schema and analysis rules, but select relevant requirements, selectors and fixtures for that screen. Do not replay the Login adapter unchanged on an unrelated form.
