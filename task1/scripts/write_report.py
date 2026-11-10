from pathlib import Path
import json,html,re
R=Path(__file__).resolve().parents[2]
design=json.loads((R/'checklist/task1_design.json').read_text());issues=json.loads((R/'task1/evidence/issues.json').read_text());results=json.loads((R/'task1/evidence/results.json').read_text())['results'];byid={r['id']:r for r in results}
report='''# HW03 — GUI & Usability: báo cáo thực thi Task 1

Sinh viên: Phạm Quang Vinh — 23120202 — 23120202@student.hcmus.edu.vn.

## 1. Phạm vi và trạng thái

Task 1 được thực thi trên Login, Profile/Hồ sơ và Lịch sử đơn, Admin Orders; navbar và Home hỗ trợ điều hướng/thêm giỏ. Task 2 và Task 3 chưa thực thi trong báo cáo này. Phạm vi màn hình/flow không trùng thành viên khác vẫn cần sinh viên xác nhận.

Kết quả: **58 mục đã chạy; 30 Passed; 28 Failed; 23 bug/phát hiện**, gồm 19 vi phạm đặc tả và 4 vấn đề UX bổ sung. Có 28 ảnh thực tế cho các mục Failed. Đã đăng 23 GitHub Issues kèm ảnh tại [HW03-Software-Testing](https://github.com/vinh-code/HW03-Software-Testing/issues). Sinh viên 23120202 đã xác nhận duyệt Task 1; việc duyệt được ghi tại [human_review.json](../task1/evidence/human_review.json).

## 2. Môi trường và phương pháp

- Ngày: 10/11/2026; thời gian từng mục lưu UTC trong JSON/Excel.
- SUT: EShop, commit 85af3ba; không sửa mã nguồn SUT trong lượt kiểm thử.
- OS: Linux x86_64. Trình duyệt thực: Chrome headless 156.0.8078.79, locale en-US.
- Web: http://localhost:5173; Admin: http://localhost:5174; API: http://localhost:3000.
- Viewport: 1366×900; GUI-057 dùng 360×800. Viewport hẹp không được tính là thiết bị mobile thật.
- Dùng Playwright CLI chạy tương tác thật, DOM/computed styles để đo và SQLite/API chuẩn bị fixture riêng. Không đánh Passed/Failed chỉ từ đọc source.
- Account fixture: task1-main@example.test, task1-empty@example.test, task1-other@example.test; mật khẩu demo GuiTest123!. Đây là dữ liệu thử, không phải participants Task 2.
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
 if d['why']:report+=f'| {d["id"]} | {d["why"]} |\n'
report+='''
## 4. Kết quả thực thi

| Chỉ số | Giá trị |
|---|---|
| Thiết kế / thực thi | 58 / 58 |
| Passed / Failed | 30 / 28 |
| Màn hình chính | 3 |
| Bug/phát hiện đã ghi file | 23 |
| Ảnh lỗi | 28 |
| GitHub Issues đã đăng | 23 |
| Phiên usability đã thực hiện | 0 |
| Nền tảng đã chạy trong Task 1 | 1 — Chrome headless/Linux |

Chi tiết đầy đủ: [Excel](../checklist/GUI_Checklist.xlsx), [Markdown](../checklist/GUI_Checklist.md), [JSON thực thi](../task1/evidence/results.json).

## 5. Bug report

Các mục Failed cùng nguyên nhân được gom để tránh báo trùng. Các vấn đề UX bổ sung được gắn nhãn UX. Mỗi link bên dưới có bước tái hiện, mong đợi, thực tế, mức độ và ảnh chụp.

| Bug | Nội dung | Mức độ | Mục Failed |
|---|---|---|---|
'''
for i in issues:report+=f'| [{i["id"]}]({i["url"]}) | {i["title"]} | {i["severity"]} | {", ".join(i["cases"])} |\n'
report+='\n### Quan sát thực tế cho từng lỗi\n\n'
for i in issues:
 report+=f'**{i["id"]} — {i["title"]}**\n\n'
 for cid in i['cases']:
  a=byid[cid]['actual'].replace('\n','; ').replace('<','&lt;').replace('>','&gt;')
  report+=f'- {cid}: {a}. [Ảnh](../bugs/screenshots/{cid}.png).\n'
 report+='\n'
report+='''## 6. Giới hạn và việc cần làm trước khi nộp

1. Sinh viên đã xác nhận duyệt Task 1. Thông tin MSSV/email đã được cung cấp. Phạm vi không trùng nhóm vẫn cần đối chiếu với các thành viên; nguồn gốc các mục AI được giữ nguyên.
2. GitHub Issues đã đăng đủ 23 mục kèm ảnh; xem [danh sách Issues](https://github.com/vinh-code/HW03-Software-Testing/issues).
3. Task 2 (pilot, 7 người thật, phân tích) và Task 3 (ít nhất ba nền tảng) chưa hoàn thành. Không dùng số lượng dự kiến trong template làm kết quả thực tế.
4. AI Audit Report của phiên hiện tại được lưu; lịch sử sinh checklist trước phiên này chưa có log đầy đủ. AI Critique do AI hỗ trợ soạn và đã được sinh viên duyệt.
5. Các tiêu chí bổ sung không tự động trở thành yêu cầu của đặc tả. Kết quả chỉ phản ánh môi trường và dữ liệu thử đã ghi, không chứng minh ứng dụng hoàn toàn an toàn hay tương thích mọi nền tảng.

## 7. Tài liệu và lịch sử

- [Rà soát thiết kế](../task1/DESIGN_REVIEW.md).
- [Quy trình và script chạy lại](../task1/README.md).
- [Bug report](../bugs/README.md).
- [AI Audit Report](../ai_audit_report.md).
- [AI Critique — đã duyệt](../ai_critique.md).
- [Git commit log](../git_commit_log.txt).
'''
(R/'report/main_report.md').write_text(report)
(R/'README.md').write_text('''# HW03 — GUI & Usability

Sinh viên: Phạm Quang Vinh — 23120202 — 23120202@student.hcmus.edu.vn.

**Task 1 đã chạy và đăng 23 GitHub Issues kèm ảnh; sinh viên đã xác nhận duyệt. Task 2/3 chưa thực hiện.**

Repository: [vinh-code/HW03-Software-Testing](https://github.com/vinh-code/HW03-Software-Testing) · [GitHub Issues](https://github.com/vinh-code/HW03-Software-Testing/issues)

- [Báo cáo chính Markdown](report/main_report.md) / [PDF](report/main_report.pdf)
- [Checklist Excel](checklist/GUI_Checklist.xlsx) / [Markdown](checklist/GUI_Checklist.md)
- [23 bug/phát hiện và ảnh](bugs/README.md)
- [Dữ liệu thực thi](task1/evidence/results.json) / [Cách chạy lại](task1/README.md)
- [AI Audit](ai_audit_report.md) / [AI Critique — đã duyệt](ai_critique.md)
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
| Flow usability / phiên / người tham gia thực tế | 0 / 0 / 0 |
| Nền tảng đã test | 1: Chrome headless / Linux |
| Demo video | Chưa thực hiện |

## Self-assessment — sinh viên tự điền sau khi hoàn thiện

| Tiêu chí | Điểm tối đa | Tự chấm |
|---|---|---|
| Task 1 | 30 | Đã duyệt; chưa tự chấm điểm |
| Task 2 | 40 | Chưa thực hiện |
| Task 3 | 20 | Chưa đủ ba nền tảng |
| Agent Skills | 10 | Chưa xây skill riêng |
| Tổng | 100 | Chưa chốt |

Chưa đóng gói ZIP nộp cuối vì các phần bắt buộc của toàn bài còn thiếu. Bản checklist cũ được giữ trong commit baseline. Không sửa code SUT để che lỗi; chỉ tạo dữ liệu thử riêng và thu bằng chứng. Không khởi động lại backend trước khi backup DB vì database.js tự reset khi import.
''')
