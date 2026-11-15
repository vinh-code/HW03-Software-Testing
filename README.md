# HW03 — GUI & Usability

Sinh viên: **Phạm Quang Vinh — MSSV: 23120202 — 23120202@student.hcmus.edu.vn**.

Học phần: **CS423 / CSC13003 – Software Testing (AI-augmented) — Term 2026**. [Thông tin khoa, giảng viên và liên hệ](report/course_information.md).

## Hướng dẫn chấm bài

Mở [báo cáo tổng hợp PDF](report/main_report.pdf) trước, sau đó xem từng phần theo bảng dưới.

| Thứ tự | Nội dung chấm | Tài liệu chính | Bằng chứng chi tiết |
|---|---|---|---|
| 1 | Task 1 — GUI (30 điểm) | [Checklist Excel: 58 mục](task1_gui/checklist/GUI_Checklist.xlsx) | [23 bug report](task1_gui/bugs/README.md), `task1_gui/bugs/screenshots/`, `task1_gui/evidence/` |
| 2 | Task 2 — Usability (40 điểm) | [Báo cáo tổng hợp](task2_usability/Task2_Usability_Report.pdf) / [Excel SUS](task2_usability/Task2_Usability_Data.xlsx) | [Danh sách người tham gia](task2_usability/05_participants.md), `task2_usability/sessions/` — 1 pilot + 7 phiên |
| 3 | Task 3 — Cross-platform (20 điểm) | [Báo cáo](task3_cross_platform/README.pdf) | `task3_cross_platform/screenshots/` — 84 ảnh trên 3 nền tảng |
| 4 | Agent Skill (10 điểm) | [Hướng dẫn và skill](task4_agent_skills/README.md) / [Video YouTube](https://youtu.be/Y1BYcoC3PGg) | `task4_agent_skills/demo/` — script, kết quả và 10 ảnh |
| 5 | AI Audit và AI Critique | [Audit PDF](ai_audit_report.pdf) / [Critique PDF](ai_critique.pdf) | Bản Markdown cùng tên; Word theo template và `report/ai_audit_evidence/` |
| 6 | Lịch sử thực hiện | [Git commit log](git_commit_log.txt) | [Repository](https://github.com/vinh-code/HW03-Software-Testing) |

### Cây thư mục nộp bài

```text
23120202_HW03_AI_GUIUsability_100/
├── README.md                              ← đọc trước: chỉ dẫn, bảng tra cứu, tự chấm
├── ai_audit_report.md / .pdf / .docx      ← Báo cáo kiểm toán AI (10/10 VALID)
├── ai_critique.md / .pdf                  ← Bản phản biện AI (296 từ)
├── git_commit_log.txt                     ← Toàn bộ lịch sử commit Git
│
├── task1_gui/                             ← Task 1: GUI Checklist & Automation (30đ)
│   ├── checklist/                         ← GUI Checklist (Excel & Markdown 58 mục)
│   ├── bugs/                              ← 23 bug reports & screenshots
│   ├── evidence/                          ← Log & kết quả 30 Passed / 28 Failed
│   ├── scripts/                           ← Script Playwright tự động hóa
│   └── README.md
│
├── task2_usability/                       ← Task 2: Usability Evaluation (40đ)
│   ├── Task2_Usability_Report.md / .pdf   ← Báo cáo đánh giá Usability hoàn chỉnh
│   ├── Task2_Usability_Data.xlsx          ← Số liệu SUS & ma trận tổng hợp
│   ├── 05_participants.md                 ← Danh sách 8 người tham gia (1 pilot + 7 chính thức)
│   ├── sessions/                          ← Biên bản chi tiết 8 phiên thử nghiệm
│   ├── analysis.md                        ← Phân tích định tính / định lượng
│   └── README.md
│
├── task3_cross_platform/                  ← Task 3: Cross-Platform Testing (20đ)
│   ├── README.pdf / README.md             ← Báo cáo kiểm thử đa nền tảng
│   ├── screenshots/                       ← 84 ảnh minh chứng (Chrome, Firefox, Galaxy S23)
│   ├── evidence/                          ← Log & dữ liệu thực thi BrowserStack
│   └── scripts/
│
├── task4_agent_skills/                    ← Task 4: Agent Skills & Demo Video (10đ)
│   ├── README.md                          ← Hướng dẫn sử dụng & link YouTube demo
│   ├── gui-usability-evaluator/           ← Mã nguồn Agent Skill theo Nielsen Heuristics
│   └── demo/                              ← Kết quả thực thi minh chứng
│
└── report/                                ← Báo cáo tổng kết toàn khóa
    ├── main_report.md / .pdf              ← Báo cáo tổng hợp trọn gói
    ├── course_information.md              ← Thông tin học phần & giảng viên
    └── templates/                         ← Mẫu văn bản học vụ
```

Cây trên liệt kê các phần chính để tra cứu. Các thư mục `scripts/` và file JSON/CSV là mã chạy lại và dữ liệu hỗ trợ; bản PDF dành cho đọc/chấm, Markdown dành cho đối chiếu nội dung, Excel dành cho kiểm tra số liệu.

**Kiểm tra thành phần:** đã có đủ các nhóm tài liệu bắt buộc theo mục 14 của đề; thông tin sinh viên, cam kết AI, ngày nộp, họ tên ở ô chữ ký và bảng tự chấm đã điền. Sinh viên xác nhận đã trực tiếp thực hiện Task 2 và điền kết quả trong hồ sơ tổng hợp.

**Task 1 đã chạy và đăng 23 GitHub Issues kèm ảnh; sinh viên đã xác nhận duyệt. Task 2 có đủ hồ sơ 1 pilot + 7 phiên do sinh viên thực hiện; Task 3 đã chạy đủ 3/3 nền tảng.**

Repository: [vinh-code/HW03-Software-Testing](https://github.com/vinh-code/HW03-Software-Testing) · [GitHub Issues](https://github.com/vinh-code/HW03-Software-Testing/issues)

- [Báo cáo chính Markdown](report/main_report.md) / [PDF](report/main_report.pdf)
- [Checklist Excel](task1_gui/checklist/GUI_Checklist.xlsx) / [Markdown](task1_gui/checklist/GUI_Checklist.md)
- [23 bug/phát hiện và ảnh](task1_gui/bugs/README.md)
- [Task 2: Hồ sơ Usability](task2_usability/README.md) / [PDF](task2_usability/Task2_Usability_Report.pdf) / [Excel](task2_usability/Task2_Usability_Data.xlsx)
- [Task 3: Báo cáo và ảnh](task3_cross_platform/README.md) / [PDF](task3_cross_platform/README.pdf)
- [Agent Skill và demo](task4_agent_skills/README.md) / [Video YouTube](https://youtu.be/Y1BYcoC3PGg)
- [Dữ liệu thực thi](task1_gui/evidence/results.json) / [Cách chạy lại](task1_gui/README.md)
- [AI Audit](ai_audit_report.md) / [Word theo template](ai_audit_report.docx) / [PDF](ai_audit_report.pdf) / [AI Critique — đã duyệt](ai_critique.md)
- [Git commit log](git_commit_log.txt)

## Test summary

| Chỉ số | Kết quả thực tế |
|---|---|
| Màn hình chính Task 1 | 3: Login, Profile, Admin Orders |
| Checklist thiết kế / thực thi | 58 / 58 |
| Passed / Failed | 30 / 28 |
| Bug/phát hiện | 23 (19 vi phạm spec, 4 UX bổ sung) |
| Ảnh Failed | 28 |
| GitHub Issues đã đăng | 23 |
| Hồ sơ usability | 1 flow / 8 biên bản (1 pilot + 7 chính thức) |
| Nền tảng đã test | 3: Chrome và Firefox / Ubuntu; Chrome / Samsung Galaxy S23 Android 13 |
| Demo video | [Video YouTube do sinh viên cung cấp](https://youtu.be/Y1BYcoC3PGg) |

## Self-assessment — theo điểm sinh viên yêu cầu

| Tiêu chí | Điểm tối đa | Tự chấm |
|---|---|---|
| Task 1 | 30 | 30 |
| Task 2 | 40 | 40 |
| Task 3 | 20 | 20 |
| Agent Skills | 10 | 10 |
| Tổng | 100 | **100** |

Ngày nộp: **15/11/2026**. Chữ ký (họ tên): **Phạm Quang Vinh**. Tổng điểm tự chấm: **100/100**. Các hướng dẫn chạy lại nằm trong từng thư mục task.
