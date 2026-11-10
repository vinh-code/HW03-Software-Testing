# AI Audit Report — Task 1

I use AI tools for the following tasks.

- Công cụ: OpenAI Codex; skill Playwright CLI; Python/openpyxl để xuất báo cáo.
- Ngày: 10/11/2026, timezone Asia/Ho_Chi_Minh; thời gian máy trong kết quả lưu UTC.
- Phạm vi AI: đọc đề, review source/checklist, sửa thiết kế, tạo dữ liệu thử, chạy 58 mục trên browser, chụp 28 ảnh, tổng hợp 23 bug/phát hiện, xuất tài liệu.
- Prompt và output hội thoại hiện có: [bản trích xuất](task1/evidence/ai_conversation.md).
- Output có cấu trúc: [thiết kế](checklist/task1_design.json), [thực thi](task1/evidence/results.json), [bug](bugs/README.md), [scripts](task1/scripts/).
- Quy trình: 70 mục ban đầu -> rà soát phạm vi -> 58 tiêu chí đo được -> thực thi browser -> kiểm tra kết quả/ảnh -> gom lỗi -> Excel/Markdown/PDF.
- Sai sót AI được sửa: tiêu chí ngoài spec; nhãn Student chưa có bằng chứng; Tab trước render; nhãn menu Admin bị nhầm. Chi tiết trong Task 1 README và design review.
- Human review: chưa xác nhận. AI không tự nhận đã có phần sinh viên bổ sung; cột Origin ghi đúng AI-reviewed/AI-added.
- Giới hạn log: lịch sử tạo bộ 70 mục trước phiên này không có trong transcript hiện có. Cần bổ sung log gốc nếu sử dụng nó làm bằng chứng quá trình. Đây không phải tuyên bố đã có toàn bộ lịch sử AI của bài HW03.
- Chưa thực hiện: 7 phiên usability thật, ba nền tảng, video demo.

## Bổ sung: xuất bản GitHub theo yêu cầu sinh viên

- Công cụ: Codex + gh CLI.
- Ngày: 10/11/2026.
- Prompt: “một dùng gh cli để tạo repo luôn giúp tôi đặt tên hợp lí là được MSSV tôi 23120202 email 23120202@student.hcmus.edu.vn”.
- Đầu ra: repository public [HW03-Software-Testing](https://github.com/vinh-code/HW03-Software-Testing), 23 Issues kèm ảnh chụp thật, cập nhật thông tin sinh viên và đường dẫn báo cáo.
- Tạo Issues bằng `gh issue create --body-file`; ảnh được nhúng bằng URL raw gắn với commit để giữ bằng chứng ổn định. Danh sách URL lưu trong `task1/evidence/issues.json`.
- Sinh viên vẫn cần tự rà soát checklist và bản nháp AI Critique; việc xuất bản không thay thế human review.
