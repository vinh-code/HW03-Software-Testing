# AI Audit — Agent Skill

I use AI tools for the following tasks.



- Ngày: 11/11/2026; video bắt đầu 14:38:25 UTC (21:38:25 Asia/Ho_Chi_Minh); timestamp từng phép đo trong JSON.
- Prompt sinh viên: “làm tiếp phần agent skill giúp tôi”. Khi được hỏi về tài khoản YouTube, sinh viên chọn “Tôi tự tải lên và gửi link”.
- Công cụ: OpenAI Codex; skill-creator, Playwright CLI, skill mới gui-usability-evaluator; Python stdlib, gh CLI; FFmpeg đi kèm Playwright để kiểm tra/giải mã video; plugin-management để tìm kết nối YouTube.
- Output AI: skill với metadata và tài liệu tham chiếu, hai helper kiểm tra/tổng hợp dữ liệu, adapter Login và chú thích video, báo cáo và nội dung tải YouTube. Skill được cài vào ~/.codex/skills và dùng trong chính phiên này.
- Thực thi: backend bản sao riêng trên cổng 3000; frontend 5173; Chrome có cửa sổ. Chạy đủ 16 tiêu chí Login, 6 Passed/10 Failed, 10 ảnh thật. Đối chiếu hash SQLite gốc không đổi. Không sửa source SUT, không đăng issue trùng.
- Video: bản ghi trình duyệt gốc 123,32 giây, VP9/WebM 1366×900/25 fps, không lời thoại. Thẻ giải thích và dải chú thích là nội dung do AI tạo, có nhãn riêng; phần giao diện và thao tác SUT được quay thật. Ảnh lỗi chụp sau phép đo và sau khi thêm dải metadata, không sửa nội dung form.
- Phân tích usability: chạy helper mới trên bộ mô phỏng Task 2, không tạo thêm phản hồi hoặc người tham gia. SUS 58,93; 4 tự hoàn thành, 2 hỗ trợ, 1 chưa hoàn thành; pilot không nằm trong mẫu.
- Kiểm tra: quick_validate của skill-creator; 11 nhóm điều kiện kiểm chứng helper, bao gồm SUS 0/50/100, dữ liệu thiếu, lẫn nguồn, pilot lẫn mẫu, ID trùng và thiếu ảnh Failed; kiểm tra video giải mã được, xem khung hình thao tác và metadata.
- Điều chỉnh trong phiên: wrapper Playwright không có quyền chạy trực tiếp nên gọi qua bash; helper được sửa để chấp nhận pilot=null. Không có lần chạy GUI lỗi bị ghi thành lỗi ứng dụng.
- Giới hạn: video quay workflow GUI và kết quả phân tích dữ liệu mô phỏng, không quay một phiên usability với người thật. YouTube Studio yêu cầu đăng nhập; sinh viên chọn tự upload. Chưa có URL và chưa xuất bản lên YouTube. Sinh viên chưa xác nhận duyệt riêng phần Agent Skill mới này.
- Bằng chứng: [skill và README](agent_skills/README.md), [JSON thực thi](agent_skills/demo/results.json), [video và metadata](agent_skills/demo/recording.json), [helper verification](agent_skills/demo/helper_verification.json).

- Tính tái lập: sau khi chạy helper, phát hiện `usability/data/simulation.json` và `usability/sus_scoring.py` được thay đổi từ bên ngoài. Giữ nguyên các thay đổi đó ở working tree, không đưa vào commit này. Demo lưu bản nguồn mô phỏng tại `agent_skills/demo/usability_input.json` từ commit `31df3d9`, đúng dữ liệu đã dùng khi ghi video; kiểm chứng chạy lại trên bản này.
