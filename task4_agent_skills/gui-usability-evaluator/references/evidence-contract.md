# Helper input contracts

## GUI

`summarize_gui.py INPUT.json --output NEW_DIRECTORY`

Required root fields: `data_kind` (`real` or `simulated`), `screen`, nonempty `environment` object and nonempty `results` array. Each result requires unique `id`, `ia` (IA-01 through IA-04), `expected`, `basis`, `origin`, `status` (Passed, Failed, Blocked, Not run), and `actual`. Executed rows require `url` and timezone-aware ISO `time`. Failed rows require a `screenshot` relative to the input file's directory; it must exist within that directory tree. This containment makes a run portable. A real run must not reference a fabricated screenshot.

Example shape (illustrative only, not a measured result):

```json
{"data_kind":"real","screen":"Login","environment":{"browser":"actual version","os":"actual OS"},"results":[{"id":"GUI-001","ia":"IA-01","expected":"Sign-in heading matches its function","basis":"Supplied specification, section ...","origin":"AI-reviewed","status":"Not run","actual":"Awaiting execution","screenshot":""}]}
```

Outputs: `summary.json`, `results.csv`, `report.md`. No fixed result counts or pre-populated pass/fail decisions. `complete` means every supplied criterion was executed; it does not certify coverage of the whole specification. The output includes aspects missing from the supplied set.

## Usability

`summarize_usability.py INPUT.json --output NEW_DIRECTORY`

Root: `data_kind` (`real` or `simulated`), `sessions` list; optional `pilot` is excluded from all main-session metrics. Each main session has unique `id`, the same `data_kind`, `sus_answers` (10 integer ratings 1–5, or null if missing), `task_time_seconds` (positive numeric), `tasks` (map from task ID to independent/assisted/failed/not_reached), and `assistance` list. Optional events have relative `seconds`, `finding` and notes for later qualitative synthesis. Real sessions additionally require a recorded `interview_datetime`; the helper cannot verify that an interview occurred.

Outputs: `summary.json`, `scores.csv`. Mixed sources, duplicate IDs, invalid ratings and malformed durations are rejected. Mean SUS uses only complete responses and reports its denominator. Time-outs are included in elapsed-time metrics but excluded from completed-task time metrics. The helper does not invent responses or perform statistical generalisation.

SUS scoring reference: [John Brooke, SUS — A quick and dirty usability scale](https://digital.ahrq.gov/sites/default/files/docs/survey/systemusabilityscale%2528sus%2529_comp%255B1%255D.pdf). Odd positions contribute answer minus one; even positions contribute five minus answer; multiply the sum by 2.5. This is a score, not a percentage.
