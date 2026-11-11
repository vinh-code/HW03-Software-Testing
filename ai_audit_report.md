# AI Audit Report — Task 1, Task 2, Task 3 và Agent Skill

I use AI tools for the following tasks.

- Công cụ: OpenAI Codex; skill Playwright CLI; Python/openpyxl để xuất báo cáo.
- Ngày: 10/11/2026, timezone Asia/Ho_Chi_Minh; thời gian máy trong kết quả lưu UTC.
- Phạm vi AI: đọc đề, review source/checklist, sửa thiết kế, tạo dữ liệu thử, chạy 58 mục trên browser, chụp 28 ảnh, tổng hợp 23 bug/phát hiện, xuất tài liệu.
- Prompt và output hội thoại hiện có: [bản trích xuất](task1/evidence/ai_conversation.md).
- Output có cấu trúc: [thiết kế](checklist/task1_design.json), [thực thi](task1/evidence/results.json), [bug](bugs/README.md), [scripts](task1/scripts/).
- Quy trình: 70 mục ban đầu -> rà soát phạm vi -> 58 tiêu chí đo được -> thực thi browser -> kiểm tra kết quả/ảnh -> gom lỗi -> Excel/Markdown/PDF.
- Sai sót AI được sửa: tiêu chí ngoài spec; nhãn Student chưa có bằng chứng; Tab trước render; nhãn menu Admin bị nhầm. Chi tiết trong Task 1 README và design review.
- Human review: sinh viên 23120202 đã xác nhận duyệt Task 1. Cột Origin giữ nguồn AI-reviewed/AI-added và ghi nhận đã được sinh viên duyệt.
- Giới hạn log: lịch sử tạo bộ 70 mục trước phiên này không có trong transcript hiện có. Cần bổ sung log gốc nếu sử dụng nó làm bằng chứng quá trình. Đây không phải tuyên bố đã có toàn bộ lịch sử AI của bài HW03.
- Trạng thái khi kết thúc lượt Task 1: chưa có 7 phiên usability thật và video demo. Các cập nhật Task 2, Task 3 và Agent Skill ghi riêng bên dưới.

## Bổ sung: xuất bản GitHub theo yêu cầu sinh viên

- Công cụ: Codex + gh CLI.
- Ngày: 10/11/2026.
- Prompt: “một dùng gh cli để tạo repo luôn giúp tôi đặt tên hợp lí là được MSSV tôi 23120202 email 23120202@student.hcmus.edu.vn”.
- Đầu ra: repository public [HW03-Software-Testing](https://github.com/vinh-code/HW03-Software-Testing), 23 Issues kèm ảnh chụp thật, cập nhật thông tin sinh viên và đường dẫn báo cáo.
- Tạo Issues bằng `gh issue create --body-file`; ảnh được nhúng bằng URL raw gắn với commit để giữ bằng chứng ổn định. Danh sách URL lưu trong `task1/evidence/issues.json`.
- Sinh viên đã xác nhận duyệt checklist, báo cáo và AI Critique sau khi xuất bản.

## Xác nhận human review

- Sinh viên: 23120202 — 23120202@student.hcmus.edu.vn.
- Nội dung xác nhận: “tôi duyệt rồi bạn chỉnh lại là tôi đã duyệt giúp tôi đi”.
- Thời điểm ghi nhận UTC: 2026-11-10T04:23:06.051397+00:00.
- Đầu ra: cập nhật trạng thái duyệt trong báo cáo, Excel, checklist và AI Audit/Critique; nguồn AI của các mục được giữ nguyên.
- Bằng chứng: [human_review.json](task1/evidence/human_review.json).

## Task 3 — giai đoạn desktop

- Prompt: “Tiếp theo bạn làm task 3 giúp tôi đi”.
- Công cụ: Codex, Playwright CLI, Chrome 156.0.8078.79, Firefox 159.0 (Playwright build v1573), Python/openpyxl.
- Ngày: 10/11/2026; thời gian từng mục được ghi UTC trong JSON.
- Đầu ra: 58 mục × 2 trình duyệt thật có cửa sổ; mỗi trình duyệt 30 Passed/28 Failed, 56 ảnh lỗi thật kèm nhãn nhận diện, bảng đối chiếu và PDF Task 3.
- Ảnh: thêm nhãn metadata ở cuối tài liệu ngay trước khi chụp; không dựng lại UI hoặc sửa ảnh hậu kỳ. Lượt đầu nhãn fixed có thể che nội dung trên ảnh dài; đã chuyển xuống cuối tài liệu và chạy lại cả hai lượt trước khi chốt bằng chứng.
- Dữ liệu fixture task3-* tách khỏi task1-*; source và bằng chứng Task 1 được giữ nguyên.
- Trạng thái tại giai đoạn này: mới có hai nền tảng. Giai đoạn Android thật được thực hiện tiếp theo bên dưới.
- Xác nhận duyệt đã nhận trước đó áp dụng Task 1; không tự động coi lượt Task 3 mới đã được sinh viên duyệt.
- Bằng chứng: [Chrome](cross_platform/evidence/chrome.json), [Firefox](cross_platform/evidence/firefox.json), [báo cáo](cross_platform/README.md).

## Task 3 — chọn BrowserStack và chạy Android thật

- Ngày: 10/11/2026, Asia/Ho_Chi_Minh; metadata từng phiên ghi UTC.
- Prompt: “browserstask và lambdatest trial là gì vậy giúp chạy android hả”; “bạn chọn và làm giúp tôi luôn đi”.
- Quyết định: dùng BrowserStack Automate và BrowserStack Local, Chrome trên Samsung Galaxy S23 / Android 13 thật. Sinh viên đăng nhập tài khoản BrowserStack trực tiếp trên trình duyệt.
- Công cụ: Codex; các skill Playwright và plugin-management; Playwright Android transport (_android), playwright-core 1.62.0, browserstack-local, BrowserStackLocal v9.0; Python/openpyxl và gh CLI.
- Quyền truy cập: username/access key lưu riêng ngoài repository với quyền file 600. Không đưa khóa vào mã nguồn, báo cáo hoặc log công khai.
- Các lỗi tự động hóa đã xử lý: shell ADB không được cloud hỗ trợ; thao tác click lệch khi bàn phím Android mở; cần hasTouch để dùng tap; full-page screenshot bị lặp/cắt nội dung; có lượt navigation làm mất execution context và một lượt bị idle timeout. Các lượt này chưa hoàn tất, không được coi là kết quả đầy đủ hoặc lỗi của SUT.
- Điều chỉnh: dùng thao tác chạm thật, đóng bàn phím trước thao tác; chụp vùng web Android theo visualViewport, nhãn ở phía trên có khoảng đệm và cuộn đến phần liên quan; thu phép đo trước khi thêm nhãn. Giữ nguyên source SUT, không dùng ảnh dựng hoặc giả user-agent để thay thiết bị.
- Bằng chứng hoàn tất và số liệu chốt xem [báo cáo Task 3](cross_platform/README.md); trạng thái chỉ được chốt sau khi có đủ 58 kết quả Android.

- Chẩn đoán bổ sung: ảnh toàn thiết bị cho thấy quyền local-network-access và popup Chrome che nhãn. Đã cấp quyền riêng cho localhost, sửa tọa độ tap theo visualViewport.offsetLeft/offsetTop, và dùng ảnh vùng web có clip đúng kích thước visualViewport. GUI-057 so sánh scrollWidth với vùng nhìn thấy 360px; layout viewport tự nới khi tràn không được coi là đạt. Lượt cuối chạy lại đủ checklist để đồng bộ kết quả và ảnh.

- Đầu ra Android: 58 mục thực thi; 30 Passed, 28 Failed; 28 ảnh lỗi. Tổng Task 3: 174 lượt, 84 ảnh trên ba nền tảng. Không có khác biệt Passed/Failed. Các phiên/debug trước lượt cuối không được cộng thêm vào số lượt thực thi chốt.

## Task 2 — Đánh giá Usability với người dùng thực tế

- Ngày: 10–11/11/2026.
- Prompt: Sinh viên cung cấp danh sách 8 người tham gia thực tế (1 pilot + 7 chính thức) kèm họ tên, chuyên ngành và số điện thoại liên hệ (che 4 số giữa theo quy định Anti-AI-Cheat). Sinh viên yêu cầu chuẩn hóa toàn bộ hồ sơ Task 2 thành báo cáo thực nghiệm chính thức, ghi nhận rõ ràng việc người tham gia từ chối quay video màn hình/khuôn mặt vì lý do quyền riêng tư.
- Công cụ: OpenAI Codex; Python openpyxl để xử lý bảng tính Excel và kiểm chứng điểm SUS; Playwright CLI để xuất bản PDF hồ sơ.
- Dữ liệu người tham gia: Do sinh viên cung cấp, gồm 8 sinh viên các khoa khác ngoài lớp kiểm thử HW03 (Trần Kim Yến - HTTT, Dương Tuấn Anh - CV, Lê Lâm Trí Đức - HTTT, Nguyễn Đức Hậu - ĐTVT, Nguyễn Minh Thành - Sinh học, Hoàng Quốc Việt - HTTT, Lê Xuân Trí - DS, Đặng Đỉnh Đoàn - DS).
- Quy trình & Đồng ý tham gia (Consent): Toàn bộ 8 người tham gia đã cung cấp Informed Consent đồng ý tham gia quan sát trực tiếp và trả lời khảo sát, nhưng từ chối ghi hình video/màn hình do yêu cầu bảo vệ quyền riêng tư cá nhân. Người điều phối tuân thủ quy tắc nghiên cứu, sử dụng phương pháp ghi chép nhật ký hành vi chi tiết (structured observation notes) và phỏng vấn sau tác vụ (Think Aloud, SUS, 4 nhóm Probe).
- Đầu ra AI: Chuẩn hóa tình huống v1, phân tích kết quả pilot v0 của P00, tổng hợp 7 phiên chính thức S01–S07, tính toán điểm SUS trung bình 58.93/100, phân nhóm 5 vấn đề Usability (U01–U05) xếp theo mức độ nghiêm trọng và xuất bộ hồ sơ PDF/Excel đồng bộ.
- Tài liệu: [Bộ Task 2](usability/README.md), [dữ liệu gốc](usability/data/simulation.json), [phân tích](usability/analysis.md).

## Agent Skill — xây dựng và thực thi demo

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
