---
name: gui-usability-evaluator
description: Design and execute GUI checklists with browser evidence, or prepare and analyse moderated usability studies for a selected screen or flow. Use for GUI testing coursework or evidence-based usability evaluation; keep simulated sessions distinct from observed sessions.
---

# GUI & Usability Evaluator

Produce a traceable evaluation of the user's chosen screen or flow. Select GUI execution, usability preparation/analysis, or both from the request; do not redesign the application as part of an evaluation.

## Establish scope and evidence

Read the supplied specification and existing checklist before adding criteria. Record the screen/flow, source revision, environment and evidence type. Keep specification violations separate from additional UX suggestions. Split compound assertions that could disagree. Cover layout/general standards, forms, navigation, and feedback/state where relevant; the assignment's count applies to the complete checklist, not every individual screen.

Discover existing servers and fixtures before starting anything. Check startup code for destructive database initialisation. If startup resets data, use an isolated copy or an already-authorized backup/restore approach; do not reset a database containing earlier evidence just to demonstrate this skill.

Read [evidence-contract.md](references/evidence-contract.md) when preparing results for the helpers. Read [eshop-example.md](references/eshop-example.md) only when working on this coursework's EShop.

## GUI execution

1. Review each criterion's expected behaviour, requirement/UX basis, origin and observable measurement. Do not turn common design preferences into mandatory specification requirements.
2. Use a real browser through the available Playwright CLI or browser automation tool. Record the actual browser/OS/device; a narrow viewport is not a separate physical mobile platform.
3. Run interactions and inspect resulting UI/DOM. Wait for rendering/navigation before measuring. Use dedicated demo accounts, never real passwords in screenshots/video.
4. Mark measured results Passed or Failed. Missing setup, selector errors, interrupted navigation and automation timeouts are Blocked or Not run, not application failures. Retry once after diagnosing an automation issue; if still unresolved, preserve the failure and report incomplete coverage.
5. For each Failed result, record the actual observation, UTC time, URL and screenshot. Add identifying metadata after measuring and remove it afterwards. Record native dialog text separately if screenshots show only the page after dismissal. Identify any injected latency/network errors.
6. Save structured results under a new run directory, then run `scripts/summarize_gui.py results.json --output <new-directory>`. The helper validates files and structure, not the truth of observations.
7. Group common root causes into issue drafts with steps, expected/actual behaviour and evidence. Link existing issues instead of duplicating them. Publish only within the user's authorized scope.

## Usability preparation and analysis

Choose one end-to-end flow and write a realistic goal without giving button-by-button instructions. Define success, assisted completion, stopping rules and timing boundaries before collecting data. Prepare a pilot, neutral moderator prompts, SUS or another justified instrument, and probes covering clarity, recovery, speed and trust.

Use only supplied or actually collected observations for real sessions. If the user requests simulation, label the dataset, individual session notes and summaries as simulated; do not create names, contacts, consent, interview dates or recordings as if collected. Keep pilot data separate from main-session statistics. Do not merge real and simulated responses into one reported sample.

For the supported ten-item SUS input, run `scripts/summarize_usability.py dataset.json --output <new-directory>`. Missing answers stay missing; do not fill them with neutral values. Distinguish time-out duration from completion time, and distinguish an incomplete task from one not reached. Synthesise themes with session/time references; simulated reactions are hypotheses, not newly verified bugs.

## Demo and delivery

When a demo is requested, record the actual browser workflow for one complete screen or flow. Show the loaded skill, chosen checks, real interactions and generated summary. Label explanatory title cards separately from the SUT. Preserve the original recording; do not construct a fake execution from screenshots. Provide local video, recording metadata and a concise description for upload. A missing YouTube URL remains pending rather than being invented.

Report what ran, what is incomplete, artifact paths and the limitations that affect interpretation. Preserve existing evidence rather than replacing it with a newer run.
