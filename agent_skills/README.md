# Agent Skill — GUI & Usability Evaluator

Phạm Quang Vinh — 23120202 — 23120202@student.hcmus.edu.vn.

Đã xây và dùng skill trên toàn bộ màn hình Login EShop, chạy thật 16/16 tiêu chí: **6 Passed, 10 Failed**, có 10 ảnh lỗi. Video gốc dài **2 phút 03 giây**, 1366×900, 25 fps, không có lời thoại; chú thích tiếng Việt xuất hiện ngay trong bản ghi. **Link YouTube đang chờ sinh viên tải lên và gửi lại**; đây là phần còn thiếu để hoàn tất yêu cầu video YouTube của đề.

## Tài liệu và bằng chứng

- [Skill tái sử dụng](gui-usability-evaluator/SKILL.md) và [hợp đồng dữ liệu](gui-usability-evaluator/references/evidence-contract.md).
- [Video demo gốc WebM](demo/agent-skill-demo.webm) — tải file về để xem hoặc tải lên YouTube.
- [Kết quả GUI](demo/gui_summary/report.md), [CSV](demo/gui_summary/results.csv), [JSON gốc](demo/results.json), [10 ảnh](demo/screenshots/).
- [Phân tích usability bằng helper mới](demo/usability_summary/summary.json): dữ liệu mô phỏng Task 2, 7 hồ sơ, loại pilot, SUS 58,93. Không có phiên phỏng vấn mới.
- [AI Audit riêng phần Agent Skill](ai_audit.md).
- [Kiểm chứng helper](demo/helper_verification.json), [metadata video](demo/recording.json), [nội dung tải YouTube](demo/youtube_upload.md).

## Cài và gọi skill

Copy thư mục `gui-usability-evaluator` vào `~/.codex/skills/`, giữ nguyên cấu trúc. Máy thực hiện bài này đã cài bản giống bản nộp. Mở phiên Codex mới nếu danh sách skill chưa cập nhật.

Ví dụ yêu cầu: **$gui-usability-evaluator — Đọc đặc tả EShop và checklist, kiểm thử đầy đủ màn hình Đăng nhập, chụp bằng chứng Failed và tổng hợp báo cáo.**

Với màn hình khác: cung cấp đặc tả, URL, môi trường và tài khoản thử; để agent lập/rà soát tiêu chí rồi đổi thao tác và phép đo theo màn hình. Skill và hai helper dùng chung; `demo/execute.run.js` chỉ là adapter Login, không phải bộ test dùng nguyên trạng cho mọi giao diện.

Với usability: yêu cầu skill thiết kế tình huống, tiêu chí hoàn thành, pilot, SUS và probe. Sau khi có dữ liệu theo hợp đồng, chạy helper phân tích. Thời gian hết giờ không được gọi là thời gian hoàn thành; không trộn dữ liệu mô phỏng với người thật.

## Quy trình demo đã thực hiện

1. Đọc skill, đặc tả và 16 tiêu chí Login đã duyệt trong Task 1; giữ cơ sở FR/IA của từng tiêu chí.
2. Chép các file backend JS và package.json ra `/tmp/hw03-agent-skill-backend`, liên kết node_modules; chạy bản sao trên cổng 3000. Không chạy backend gốc vì khởi động sẽ reset database.
3. Tạo account thử `skill-demo-23120202@example.test` / `GuiTest123!` trong SQLite của bản sao. Chạy frontend web trên cổng 5173, Chrome có cửa sổ 1366×900.
4. Dùng Playwright CLI `video-start` rồi `run-code --filename` để thực hiện [adapter Login](demo/execute.run.js). Khi chạy lại, thay `REPLACE_WITH_ABSOLUTE_DEMO_OUTPUT_DIRECTORY` bằng thư mục đầu ra mới có thư mục `screenshots/`; lưu JSON trong phần `### Result` vào `results.json`. Không chạy đồng thời với suite khác dùng cổng 3000.
5. Kiểm tra tiêu đề, heading, label, type input, trường bắt buộc, email sai, vị trí/ngôn ngữ lỗi, Tab, link quên mật khẩu/đăng ký và Enter đăng nhập thành công. Phép đo diễn ra trước khi thêm dải chú thích; chú thích không thay đổi form.
6. Dùng helper GUI sinh báo cáo từ JSON vừa chạy; dùng helper usability trên nguồn mô phỏng Task 2. Hiện thẻ tổng kết từ kết quả này rồi dừng video.
7. Kiểm tra hash database gốc không đổi, 10 ảnh lỗi tồn tại, 16 ID không trùng, video phát/giải mã được và hai helper xử lý đúng các đầu vào biên.

Lệnh từ thư mục gốc repository nộp bài (mỗi `--output` phải là thư mục mới):

```bash
python3 agent_skills/gui-usability-evaluator/scripts/summarize_gui.py agent_skills/demo/results.json --output /tmp/hw03-gui-summary-new
python3 agent_skills/gui-usability-evaluator/scripts/summarize_usability.py agent_skills/demo/usability_input.json --output /tmp/hw03-usability-summary-new
PYTHONDONTWRITEBYTECODE=1 python3 agent_skills/verify_helpers.py
```

## Diễn giải kết quả

16 tiêu chí bao phủ cả IA-01 đến IA-04 của Login; không có mục Blocked hoặc Not run. “Complete” là hoàn thành checklist đã chọn, không có nghĩa ứng dụng đạt chất lượng hay đã kiểm mọi khả năng.

10 mục Failed là các lỗi đã có trong Task 1, liên kết tại [issue mapping](demo/existing_issues.md); không tạo issue trùng và không sửa SUT để chuyển kết quả sang Passed. Nguồn SUT: `85af3ba875c88283615e22cb108f13e2fccaf0e9`. Chrome 156.0.8078.79 / Ubuntu 24.04.5 LTS. Lượt này là demo skill, không được cộng thành nền tảng thứ tư của Task 3.

Skill hỗ trợ chuẩn bị và phân tích usability; video minh họa thực thi GUI trọn màn hình và hiển thị kết quả phân tích bộ mô phỏng. Video không ghi một phiên phỏng vấn usability. Thẻ mở đầu/tổng kết là nội dung giải thích; phần giữa là thao tác thật trên EShop. Không dựng video từ ảnh chụp và không có lời phê duyệt mới được tự gán cho sinh viên.

Nguồn usability của demo được cố định tại [usability_input.json](demo/usability_input.json), lấy từ commit `31df3d9` trước các chỉnh sửa Task 2 ngoài phiên này. Các chỉnh sửa Task 2 diễn ra đồng thời không thuộc commit Agent Skill.
