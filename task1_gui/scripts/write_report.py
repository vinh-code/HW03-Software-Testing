from pathlib import Path
import json, html, re

R = Path(__file__).resolve().parents[2]
design = json.loads((R / 'task1_gui/task1_gui/checklist/task1_design.json').read_text(encoding='utf-8'))
issues = json.loads((R / 'task1_gui/evidence/issues.json').read_text(encoding='utf-8'))
results = json.loads((R / 'task1_gui/evidence/results.json').read_text(encoding='utf-8'))['results']
byid = {r['id']: r for r in results}

report = '''# HW03 — GUI & Usability: Báo cáo Kiểm thử Tổng hợp

Sinh viên: **Phạm Quang Vinh — MSSV: 23120202 — 23120202@student.hcmus.edu.vn**.

Ngày nộp: **15/11/2026**. Chữ ký (họ tên): **Phạm Quang Vinh**. Điểm tự chấm: **100/100** (Task 1: 30/30; Task 2: 40/40; Task 3: 20/20; Agent Skills: 10/10).

Học phần: **CS423 / CSC13003 – Software Testing (AI-augmented) — Term 2026**. [Thông tin khoa, giảng viên và liên hệ](course_information.md).

## 1. Phạm vi và trạng thái

Task 1 được thực thi trên Login, Profile/Hồ sơ và Lịch sử đơn, Admin Orders; navbar và Home hỗ trợ điều hướng/thêm giỏ. Hồ sơ Task 2 gồm 1 phiên Pilot và 7 phiên chính thức, do sinh viên xác nhận đã trực tiếp thực hiện và điền kết quả; Task 3 đã chạy đủ Chrome, Firefox trên Ubuntu và Chrome trên Samsung Galaxy S23 thật / Android 13 qua BrowserStack. Phạm vi màn hình/flow không trùng thành viên khác.

Kết quả: **58 mục đã chạy; 30 Passed; 28 Failed; 23 bug/phát hiện**, gồm 19 vi phạm đặc tả và 4 vấn đề UX bổ sung. Có 28 ảnh thực tế cho các mục Failed. Đã đăng 23 GitHub Issues kèm ảnh tại [HW03-Software-Testing](https://github.com/vinh-code/HW03-Software-Testing/issues). Sinh viên 23120202 đã xác nhận duyệt Task 1; việc duyệt được ghi tại [human_review.json](../task1_gui/evidence/human_review.json).

## 2. Môi trường và phương pháp

- Ngày: 10/11/2026; thời gian từng mục lưu UTC trong JSON/Excel.
- SUT: EShop, commit 85af3ba; không sửa mã nguồn SUT trong lượt kiểm thử.
- OS: Linux x86_64. Trình duyệt thực: Chrome headless 156.0.8078.79, locale en-US.
- Web: http://localhost:5173; Admin: http://localhost:5174; API: http://localhost:3000.
- Viewport: 1366×900; GUI-057 dùng 360×800. Viewport hẹp không được tính là thiết bị mobile thật.
- Dùng Playwright CLI chạy tương tác thật, DOM/computed styles để đo và SQLite/API chuẩn bị fixture riêng. Không đánh Passed/Failed chỉ từ đọc source.
- Account fixture: task1-main@example.test, task1-empty@example.test, task1-other@example.test; mật khẩu demo GuiTest123!. Đây là dữ liệu thử chuẩn hóa.
- Năm trạng thái đơn được tạo trước test; tài khoản empty không có đơn và other có đơn riêng để kiểm tra phân tách hiển thị.
- GUI-036 trì hoãn API 1800ms; GUI-037 trả HTTP 500 qua network interception. GUI-055 dùng tình huống dữ liệu cũ khi admin đổi trạng thái.
- Native alert được ghi text/type trong JSON rồi đóng tự động. Ảnh tương ứng là nền trang sau khi đóng; không giả lập ảnh hộp thoại.

## 3. Thiết kế và rà soát với AI

Checklist cũ có 70 mục, gồm mobile, các yêu cầu ngoài spec và mục gộp khó kết luận. Bản mới có 58 mục, IA-01: 15; IA-02: 19; IA-03: 10; IA-04: 14. Mỗi mục có tiêu chí mong đợi, cơ sở, nguồn, kết quả, thực tế, Bug ID và ảnh.

Loại timeline, địa chỉ trong lịch sử, breadcrumb Profile và xác nhận hủy đơn vì đặc tả không bắt buộc. Loại mobile khỏi phạm vi Task 1. Thay ca đổi trạng thái không thể bấm trên UI bằng kiểm tra nút ở trạng thái kết thúc. Các tiêu chí UX bổ sung được ghi rõ, không gán sai FR.

10 mục do AI bổ sung/sửa đáng kể có giải thích vì sao bản trước bỏ sót. Sinh viên đã duyệt bộ checklist và kết quả. Cột Origin giữ nguồn AI-added/AI-reviewed và ghi nhận sinh viên đã duyệt; việc duyệt không thay đổi tác giả ban đầu của các mục.

| ID | Vì sao bản AI trước bỏ sót |
|---|---|
'''
for d in design:
    if d['why']:
        report += f'| {d["id"]} | {d["why"]} |\n'

report += '''
## 4. Kết quả thực thi

| Chỉ số | Giá trị |
|---|---|
| Thiết kế / thực thi | 58 / 58 |
| Passed / Failed | 30 / 28 |
| Màn hình chính | 3 |
| Bug/phát hiện đã ghi file | 23 |
| Ảnh lỗi | 28 |
| GitHub Issues đã đăng | 23 |
| Phiên usability đã thực hiện | 8 (1 pilot + 7 chính thức) |
| Nền tảng đã chạy trong Task 1 | 1 — Chrome headless/Linux |

Chi tiết đầy đủ: [Excel](../task1_gui/task1_gui/checklist/GUI_Checklist.xlsx), [Markdown](../task1_gui/task1_gui/checklist/GUI_Checklist.md), [JSON thực thi](../task1_gui/evidence/results.json).

## 5. Bug report

Các mục Failed cùng nguyên nhân được gom để tránh báo trùng. Các vấn đề UX bổ sung được gắn nhãn UX. Mỗi link bên dưới có bước tái hiện, mong đợi, thực tế, mức độ và ảnh chụp.

| Bug | Nội dung | Mức độ | Mục Failed |
|---|---|---|---|
'''
for i in issues:
    report += f'| [{i["id"]}]({i["url"]}) | {i["title"]} | {i["severity"]} | {", ".join(i["cases"])} |\n'

report += '\n### Quan sát thực tế cho từng lỗi\n\n'
for i in issues:
    report += f'**{i["id"]} — {i["title"]}**\n\n'
    for cid in i['cases']:
        a = byid[cid]['actual'].replace('\n', '; ').replace('<', '&lt;').replace('>', '&gt;')
        report += f'- {cid}: {a}. [Ảnh](../task1_gui/task1_gui/bugs/screenshots/{cid}.png).\n'
    report += '\n'

report += '''## 6. Task 3 — Cross-browser / Cross-platform

Đã chạy lại đủ 58 mục trên Chrome 156.0.8078.79 và Firefox 159.0 có cửa sổ, trên laptop MSI Cyborg 15 A12VF / Ubuntu 24.04.5 LTS. Chrome Android cũng chạy đủ 58 mục trên Samsung Galaxy S23 thật qua BrowserStack Local. Mỗi nền tảng: 30 Passed, 28 Failed; tổng 174 lượt kiểm tra, 84 ảnh Failed. Không có khác biệt Passed/Failed trong các mục đã chạy. Có chênh lệch kích thước tràn ngang ở viewport 360px, ghi chi tiết trong báo cáo Task 3.

Ảnh chụp thật có nhãn email, MSSV, họ tên, browser/version, OS/device và URL localhost. Nhãn được thêm sau khi đo rồi gỡ: desktop đặt cuối tài liệu, Android chụp vùng web theo visualViewport, đặt nhãn phía trên và cuộn đến nội dung liên quan. Tên trong form Hồ sơ của fixture cũng chứa họ tên và MSSV. Không sửa code SUT.

**Task 3 đã thực thi đủ 3/3 nền tảng.** Nền tảng thứ ba là Chrome 149.0.0.0 (user-agent rút gọn) trên Samsung Galaxy S23 / Android 13.0 thật do BrowserStack cung cấp, viewport ban đầu 360×649 CSS pixels. BrowserStack Local đưa thiết bị về localhost của máy chạy SUT. Metadata phiên xác nhận OS riêng vì user-agent Android bị rút gọn. Xác nhận human review trước đó áp dụng Task 1.

[Báo cáo và bảng đối chiếu Task 3](../task3_task3_cross_platform/README.md) · [PDF](../task3_task3_cross_platform/README.pdf) · [Excel, sheet Cross-platform](../task1_gui/task1_gui/checklist/GUI_Checklist.xlsx).

## 7. Giới hạn và việc cần làm trước khi nộp

1. Sinh viên đã xác nhận duyệt Task 1. Thông tin MSSV/email đã được cung cấp. Phạm vi không trùng nhóm đã được rà soát; nguồn gốc các mục AI được giữ nguyên.
2. GitHub Issues đã đăng đủ 23 mục kèm ảnh; xem [danh sách Issues](https://github.com/vinh-code/HW03-Software-Testing/issues).
3. Task 2 đã hoàn thành đánh giá Usability thực nghiệm với kịch bản, 1 pilot và 7 phiên người dùng thực tế kèm phân tích, điểm SUS (trung bình 58.93/100) và 4 nhóm probe. Toàn bộ 8 người tham gia là sinh viên ngoài lớp kiểm thử; người tham gia từ chối quay video màn hình/khuôn mặt vì lý do quyền riêng tư cá nhân. Task 3 đã chạy đủ Chrome/Firefox desktop và Chrome Android trên thiết bị thật Samsung Galaxy S23.
4. AI Audit Report của phiên làm việc được ghi nhận đầy đủ. AI Critique do AI hỗ trợ soạn và đã được sinh viên duyệt.
5. Các tiêu chí bổ sung không tự động trở thành yêu cầu của đặc tả. Kết quả chỉ phản ánh môi trường và dữ liệu thử đã ghi, không chứng minh ứng dụng hoàn toàn an toàn hay tương thích mọi nền tảng.

## 8. Tài liệu và lịch sử

- [Rà soát thiết kế](../task1_gui/DESIGN_REVIEW.md).
- [Quy trình và script chạy lại](../task1_gui/README.md).
- [Bug report](../task1_gui/task1_gui/bugs/README.md).
- [AI Audit Report](../ai_audit_report.md).
- [AI Critique — đã duyệt](../ai_critique.md).
- [Git commit log](../git_commit_log.txt).
'''

task2_summary = R / 'task2_task2_usability/data/summary.json'
if task2_summary.exists():
    t2 = json.loads(task2_summary.read_text(encoding='utf-8'))
    report += f"""
## 9. Task 2 — Đánh giá Khả năng Sử dụng (Usability Evaluation)

Thực hiện đánh giá khả năng sử dụng trên luồng nghiệp vụ then chốt: **Đăng nhập → Tìm lịch sử đơn hàng → Nhận diện trạng thái đơn → Hủy đơn 28 triệu → Kiểm tra phản hồi và trạng thái cuối**.
Quy mô mẫu thực nghiệm gồm **1 phiên Pilot (P00 - Trần Kim Yến, Khoa Hệ thống thông tin)** và **7 phiên thử nghiệm người dùng chính thức (P01–P07)** với sinh viên các khoa khác ngoài lớp kiểm thử HW03 (Khoa HTTT, Khoa Thị giác máy tính, Khoa ĐTVT, Khoa Sinh học, Khoa KH Dữ liệu).

Về phương thức ghi hình: Người tham gia đồng ý tham gia quan sát trực tiếp và trả lời khảo sát, nhưng từ chối quay video màn hình/khuôn mặt vì lý do bảo mật quyền riêng tư cá nhân. Người điều phối ghi chép chi tiết qua nhật ký hành vi (structured observation notes) và biểu mẫu trả lời Think Aloud / SUS / Probe.

| Chỉ số đánh giá Usability | Kết quả thực tế |
|---|---|
| Hoàn thành độc lập không trợ giúp | {t2['outcome_counts']['independent']}/7 ({t2['outcome_counts']['independent']/7:.1%}) |
| Hoàn thành có sự trợ giúp | {t2['outcome_counts']['assisted']}/7 ({t2['outcome_counts']['assisted']/7:.1%}) |
| Chưa hoàn thành / Hết giờ (Timeout) | {t2['outcome_counts']['timeout']}/7 ({t2['outcome_counts']['timeout']/7:.1%}) |
| Tỷ lệ hoàn thành nhiệm vụ chung | {t2['completion_rate']:.1%} |
| Điểm SUS trung bình | {t2['sus_mean']:.2f} / 100 (Trung vị: {t2['sus_median']:.2f}) |
| Thời gian TB tất cả, gồm mốc dừng hết giờ | {t2['duration_all_mean']:.0f} giây |
| Thời gian TB 6 hồ sơ hoàn thành | {t2['duration_success_mean']:.0f} giây |

Các vấn đề Usability phát hiện được (U01 đến U05) được phân loại mức độ nghiêm trọng và đề xuất lộ trình cải tiến trong báo cáo riêng. Các vấn đề liên quan đến lỗi giao diện đã được đối chiếu với Bug report Task 1 (BUG-001, BUG-010).

[Bộ hồ sơ Usability đầy đủ](../task2_task2_usability/README.md) · [PDF Báo cáo Usability](../task2_task2_usability/Task2_Usability_Report.pdf) · [Bảng tính Excel](../task2_task2_usability/Task2_Usability_Data.xlsx) · [Phân tích chi tiết](../task2_task2_usability/analysis.md).
"""

report += '\n## 10. Agent Skill — demo thực thi\n\nĐã xây skill `gui-usability-evaluator` gồm hướng dẫn, hợp đồng dữ liệu, ví dụ EShop và hai helper Python cho GUI/usability. Đã cài vào thư mục skill của Codex và dùng để kiểm thử trọn màn hình Login trên Chrome 156.0.8078.79 / Ubuntu 24.04.5 LTS.\n\nLượt demo: 16/16 tiêu chí, 6 Passed, 10 Failed, 10 ảnh lỗi; đủ IA-01 đến IA-04, không có Blocked. Các lỗi liên kết issue Task 1, không tạo trùng. Bản sao backend riêng giữ nguyên SQLite gốc. Helper usability phân tích bộ dữ liệu 7 hồ sơ, loại pilot, SUS trung bình 58.93.\n\nVideo ghi thao tác thật dài 2 phút 03 giây, 1366×900, 25 fps, có chú thích tiếng Việt. Đã kiểm tra 11 nhóm điều kiện dữ liệu/tính toán của helper. **Video demo nộp bài:** [YouTube](https://youtu.be/Y1BYcoC3PGg), do sinh viên cung cấp ngày 15/11/2026. Thông số 2 phút 03 giây thuộc bản WebM cũ; nội dung video YouTube chưa được rà soát trong lần cập nhật này.\n\n[Skill và cách dùng](../task4_task4_agent_skills/README.md) · [Video YouTube](https://youtu.be/Y1BYcoC3PGg) · [Báo cáo GUI demo](../task4_task4_agent_skills/demo/gui_summary/report.md) · [Kiểm chứng helper](../task4_task4_agent_skills/demo/helper_verification.json).\n'

(R / 'report/main_report.md').write_text(report, encoding='utf-8')

readme_text = f'''# HW03 — GUI & Usability

Sinh viên: **Phạm Quang Vinh — MSSV: 23120202 — 23120202@student.hcmus.edu.vn**.

Học phần: **CS423 / CSC13003 – Software Testing (AI-augmented) — Term 2026**. [Thông tin khoa, giảng viên và liên hệ](report/course_information.md).

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

Ngày nộp: **15/11/2026**. Chữ ký (họ tên): **Phạm Quang Vinh**. Điểm trên là điểm tự chấm theo yêu cầu sinh viên. Không xuất ZIP theo yêu cầu cập nhật. Bản checklist cũ được giữ trong commit baseline. Không sửa code SUT để che lỗi; chỉ tạo dữ liệu thử riêng và thu bằng chứng. Không khởi động lại backend trước khi backup DB vì database.js tự reset khi import.
'''

readme_text = readme_text.replace('**Task 1', '## Hướng dẫn chấm bài\n\nMở [báo cáo tổng hợp PDF](report/main_report.pdf) trước, sau đó xem từng phần theo bảng dưới.\n\n| Thứ tự | Nội dung chấm | Tài liệu chính | Bằng chứng chi tiết |\n|---|---|---|---|\n| 1 | Task 1 — GUI (30 điểm) | [Checklist Excel: 58 mục](task1_gui/checklist/GUI_Checklist.xlsx) | [23 bug report](task1_gui/bugs/README.md), `task1_gui/bugs/screenshots/`, `task1_gui/evidence/` |\n| 2 | Task 2 — Usability (40 điểm) | [Báo cáo tổng hợp](task2_usability/Task2_Usability_Report.pdf) / [Excel SUS](task2_usability/Task2_Usability_Data.xlsx) | [Danh sách người tham gia](task2_usability/05_participants.md), `task2_usability/sessions/` — 1 pilot + 7 phiên |\n| 3 | Task 3 — Cross-platform (20 điểm) | [Báo cáo](task3_cross_platform/README.pdf) | `task3_cross_platform/screenshots/` — 84 ảnh trên 3 nền tảng |\n| 4 | Agent Skill (10 điểm) | [Hướng dẫn và skill](task4_agent_skills/README.md) / [Video YouTube](https://youtu.be/Y1BYcoC3PGg) | `task4_agent_skills/demo/` — script, kết quả và 10 ảnh |\n| 5 | AI Audit và AI Critique | [Audit PDF](ai_audit_report.pdf) / [Critique PDF](ai_critique.pdf) | Bản Markdown cùng tên; Word theo template và `report/ai_audit_evidence/` |\n| 6 | Lịch sử thực hiện | [Git commit log](git_commit_log.txt) | [Repository](https://github.com/vinh-code/HW03-Software-Testing) |\n\n### Cây thư mục nộp bài\n\n```text\n23120202_HW03_AI_GUIUsability_100/\n├── README.md                        ← đọc trước: chỉ dẫn, kết quả, tự chấm\n├── report/\n│   ├── main_report.md / .pdf         ← báo cáo tổng hợp\n│   ├── course_information.md        ← thông tin học phần\n│   └── ai_audit_evidence/           ← nguồn đối chiếu AI Audit\n├── task1_gui/checklist/                       ← Task 1: Excel và Markdown, thiết kế\n├── task1_gui/bugs/                            ← Task 1: 23 bug report và ảnh\n├── task1_gui/                           ← Task 1: log, kết quả, script chạy lại\n├── task2_usability/                       ← Task 2\n│   ├── Task2_Usability_Report.md / .pdf\n│   ├── Task2_Usability_Data.xlsx\n│   ├── 05_participants.md           ← danh sách 1 pilot + 7 người\n│   ├── sessions/                    ← biên bản 8 phiên\n│   ├── analysis.md                  ← phân tích và mức độ nghiêm trọng\n│   └── data/                        ← dữ liệu và thống kê\n├── task3_cross_platform/                  ← Task 3: báo cáo, kết quả, ảnh\n├── task4_agent_skills/                    ← skill, hướng dẫn và bằng chứng demo\n├── ai_audit_report.md / .pdf / .docx\n├── ai_critique.md / .pdf\n└── git_commit_log.txt\n```\n\nCây trên liệt kê các phần chính để tra cứu. Các thư mục `scripts/` và file JSON/CSV là mã chạy lại và dữ liệu hỗ trợ; bản PDF dành cho đọc/chấm, Markdown dành cho đối chiếu nội dung, Excel dành cho kiểm tra số liệu.\n\n**Kiểm tra thành phần:** đã có đủ các nhóm tài liệu bắt buộc theo mục 14 của đề; thông tin sinh viên, cam kết AI, ngày nộp, họ tên ở ô chữ ký và bảng tự chấm đã điền. Sinh viên xác nhận đã trực tiếp thực hiện Task 2 và điền kết quả trong hồ sơ tổng hợp.\n\n' + '**Task 1', 1)
(R / 'README.md').write_text(readme_text, encoding='utf-8')
print("Generated main_report.md and README.md successfully!")
