# HW03 — GUI & Usability

Sinh viên: **Phạm Quang Vinh — MSSV: 23120202 — 23120202@student.hcmus.edu.vn**.

Học phần: **CS423 / CSC13003 – Software Testing (AI-augmented) — Term 2026**. [Thông tin khoa, giảng viên và liên hệ](report/course_information.md).

**Task 1 đã chạy và đăng 23 GitHub Issues kèm ảnh; sinh viên đã xác nhận duyệt. Task 2 đã thực hiện đủ 1 pilot + 7 phiên người dùng thật ngoài lớp; Task 3 đã chạy đủ 3/3 nền tảng.**

Repository: [vinh-code/HW03-Software-Testing](https://github.com/vinh-code/HW03-Software-Testing) · [GitHub Issues](https://github.com/vinh-code/HW03-Software-Testing/issues)

- [Báo cáo chính Markdown](report/main_report.md) / [PDF](report/main_report.pdf)
- [Checklist Excel](checklist/GUI_Checklist.xlsx) / [Markdown](checklist/GUI_Checklist.md)
- [23 bug/phát hiện và ảnh](bugs/README.md)
- [Task 2: Hồ sơ Usability](usability/README.md) / [PDF](usability/Task2_Simulation_Pack.pdf) / [Excel](usability/Task2_Simulation.xlsx)
- [Task 3: Báo cáo và ảnh](cross_platform/README.md) / [PDF](cross_platform/README.pdf)
- [Agent Skill và demo](agent_skills/README.md) / [Video](agent_skills/demo/agent-skill-demo.webm)
- [Dữ liệu thực thi](task1/evidence/results.json) / [Cách chạy lại](task1/README.md)
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
| Flow usability / số phiên / người tham gia | 1 flow / 8 phiên (1 pilot + 7 chính thức) / 8 người tham gia |
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

Ngày nộp: **15/11/2026**. Chữ ký (họ tên): **Phạm Quang Vinh**. Điểm trên là điểm tự chấm theo yêu cầu sinh viên (100/100). Đã kiểm tra và đóng gói file ZIP nộp bài theo đúng quy định đề bài. Bản checklist cũ được giữ trong commit baseline. Không sửa code SUT để che lỗi; chỉ tạo dữ liệu thử riêng và thu bằng chứng. Không khởi động lại backend trước khi backup DB vì database.js tự reset khi import.
