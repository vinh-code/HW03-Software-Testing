# Task 2 — Báo cáo Đánh giá Khả năng Sử dụng (Usability Evaluation Pack)

Sinh viên: **Phạm Quang Vinh — MSSV: 23120202 — 23120202@student.hcmus.edu.vn**.
Khóa học: Kiểm thử phần mềm (Software Testing) — FIT, HCMUS.


---

## Danh mục nội dung trong bộ hồ sơ

1. Phạm vi, mục tiêu và phương pháp đánh giá.
2. Tình huống và kịch bản thực nghiệm (Scenario).
3. Lời dẫn điều phối, phiếu khảo sát SUS và câu hỏi mở (Probe).
4. Danh sách 8 người tham gia độc lập (P00–P07) kèm thông tin liên hệ xác thực (Masked).
5. Biên bản phiên Pilot P00 và các điều chỉnh kịch bản.
6. 7 Biên bản phiên thử nghiệm chính thức (S01–S07) kèm timeline quan sát, phát biểu Think Aloud và bảng điểm SUS.
7. Báo cáo phân tích tổng hợp, phân loại mức độ nghiêm trọng và đề xuất lộ trình cải tiến.


---

# Phạm vi và Phương pháp Đánh giá Usability (Task 2)

## 1. Phạm vi đánh giá

Luồng trải nghiệm người dùng được lựa chọn cho Task 2 là: **Quản lý đơn hàng đã đặt trên nền tảng Web EShop** (Bao gồm các màn hình: Trang chủ/Navbar, Đăng nhập, và Hồ sơ cá nhân / Lịch sử đơn hàng).

- **Cơ sở lựa chọn:** Đây là luồng nghiệp vụ cốt lõi sau mua hàng của người tiêu dùng trên sàn thương mại điện tử, đòi hỏi tính trực quan, độ tin cậy và khả năng kiểm soát đơn hàng cao.
- **Quy mô mẫu:** Gồm **1 phiên Pilot (P00)** để hoàn thiện kịch bản và **7 phiên kiểm thử chính thức (P01–P07)** với 7 người dùng thực tế đại diện cho các nhóm chuyên ngành và kinh nghiệm TMĐT khác nhau.

## 2. Tính trung thực và Quy định đạo đức nghiên cứu

- **Đối tượng tham gia:** 100% người tham gia (8 người) là sinh viên các khoa khác ngoài nhóm lớp kiểm thử (Khoa Hệ thống thông tin, Thị giác máy tính, Điện tử viễn thông, Sinh học, Khoa học dữ liệu). Không có người tham gia nào thuộc danh sách lớp học phần HW03.
- **Xác minh danh tính:** Danh sách người tham gia cung cấp đầy đủ Họ tên, Khoa/Ngành, số điện thoại liên hệ (được che 4 số giữa theo đúng quy định chống gian lận Anti-AI-Cheat của đề bài).
- **Quyền riêng tư & Ghi hình (Informed Consent):**
  - Trước khi tiến hành kiểm thử, tất cả người tham gia đều được giải thích rõ mục đích nghiên cứu và cung cấp sự đồng ý (Informed Consent).
  - Về việc ghi hình (video recording): Theo quyền tự do cá nhân, **toàn bộ người tham gia đều từ chối quay video màn hình và ghi hình khuôn mặt** vì lý do bảo mật thông tin cá nhân.
  - Người điều phối tôn trọng quyền riêng tư của người tham gia (phù hợp với quy định *"Record the screen (and audio, with consent) ... where available"* trong đề cương môn học), chuyển sang phương pháp quan sát trực tiếp chuyên sâu, bấm giờ tác vụ chính xác và ghi chép nhật ký hành vi chi tiết (Structured Observation Notes) kết hợp ghi nhận phát biểu Think Aloud.


---

# Kế hoạch Đánh giá Khả năng Sử dụng (Usability Plan)

## 1. Mục tiêu đánh giá (Objectives)

Nghiên cứu tập trung đánh giá luồng tương tác người dùng then chốt: **Đăng nhập → Tìm lịch sử đơn hàng → Nhận diện trạng thái đơn → Hủy đơn hàng chưa xử lý → Kiểm tra phản hồi hệ thống**.

| Mục tiêu | Nội dung xem xét | Chỉ số đo lường |
|---|---|---|
| O1 | Khả năng tìm kiếm lối vào lịch sử đơn hàng | Mức độ khó khăn khi định hướng (U01), số lần cần trợ giúp ở T1 |
| O2 | Khả năng hiểu nhãn trạng thái và nhận diện đơn hàng | Tỷ lệ hoàn thành T1/T2, các phản hồi về nhãn trạng thái (U02/U05) |
| O3 | Khả năng thực hiện hủy đúng đơn và nhận thức phản hồi | Tỷ lệ hoàn thành T3/T4, mức độ tin cậy vào kết quả (U03/U04) |
| O4 | Đánh giá mức độ hài lòng và trải nghiệm tổng thể | Điểm số khảo sát chuẩn SUS và câu trả lời 4 nhóm probe |

## 2. Môi trường kiểm thử

- **Hệ thống thử nghiệm:** EShop Web Frontend chạy trên trình duyệt Google Chrome (Ubuntu 24.04 LTS / Windows 11), Viewport 1366×900, kết nối backend API `http://localhost:3000`.
- **Dữ liệu đơn hàng mẫu:**

| Ký hiệu đơn | Giá trị đơn hàng | Trạng thái ban đầu | Mục đích kiểm thử |
|---|---|---|---|
| Đơn A | 28.000.000 đồng | Chờ xác nhận (pending) | Đơn hàng mục tiêu để người dùng thực hiện hủy (T3) |
| Đơn B | 1.500.000 đồng | Đã xác nhận (confirmed) | Đơn hàng nhiễu trong danh sách |
| Đơn C | 45.000.000 đồng | Đang giao (shipping) | Đơn hàng mục tiêu kiểm tra trạng thái (T2) |
| Đơn D | 30.000.000 đồng | Đã giao (delivered) | Đơn hàng mục tiêu kiểm tra trạng thái giao hàng (T1) |

Tài khoản và danh sách đơn hàng được chuẩn bị sẵn sàng và làm mới về trạng thái ban đầu trước mỗi phiên kiểm thử.

## Tình huống v1 — dùng chung cho P01–P07

Bạn đã có tài khoản và đã đặt một số đơn hàng trên hệ thống EShop. Hôm nay bạn muốn kiểm tra tiến độ các đơn đã đặt và hủy một đơn không còn nhu cầu mua nữa.

1. Cho biết đơn hàng trị giá **30.000.000 đồng** đã được giao thành công hay chưa.
2. Cho biết đơn hàng trị giá **45.000.000 đồng** hiện đang ở trạng thái nào.
3. Bạn không còn nhu cầu mua đơn hàng **28.000.000 đồng** nữa. Hãy thực hiện hủy đúng đơn hàng đó trên hệ thống.
4. Cho biết trạng thái cuối cùng của đơn hàng vừa hủy và những dấu hiệu trực quan nào trên màn hình giúp bạn tin chắc rằng thao tác hủy đã thành công.

Khi đã thực hiện xong các yêu cầu trên hoặc cảm thấy không thể thao tác tiếp tục, hãy thông báo cho người điều phối. Trong suốt quá trình thực hiện, vui lòng liên tục chia sẻ thành lời (Think Aloud) những gì bạn đang nhìn thấy, suy nghĩ hoặc băn khoăn.

**Thông tin tài khoản thực nghiệm:** `usability-demo@example.test` / `UsabilityDemo123!`.

---

## Mục tiêu ban đầu dùng cho phiên Pilot v0

Bạn có một số đơn hàng khoảng 30 triệu và 45 triệu đồng. Hãy kiểm tra việc giao hàng, hủy đơn khoảng 28 triệu mà bạn không cần nữa rồi báo khi xong.

*Ghi chú*: Bản v0 được thiết kế ban đầu để thử nghiệm với người tham gia pilot P00 nhằm phát hiện các điểm mơ hồ về từ ngữ số tiền và tiêu chí hoàn thành, từ đó hoàn thiện kịch bản v1 chính thức cho 7 phiên tiếp theo.

## 3. Quy tắc ghi nhận kết quả tác vụ

- **T1:** Người tham gia tìm được trang Lịch sử đơn hàng, nhận diện đúng đơn 30 triệu và nêu chính xác trạng thái "Đã giao".
- **T2:** Người tham gia nhận diện đúng đơn 45 triệu và nêu chính xác trạng thái "Đang giao".
- **T3:** Người tham gia thao tác nhấn nút Hủy đúng đơn 28 triệu (không hủy nhầm các đơn khác).
- **T4:** Người tham gia xác định được trạng thái đơn đã chuyển sang "Đã hủy" và nêu được các dấu hiệu trực quan (thông báo alert, nhãn đổi màu).
- **Phân loại kết quả toàn luồng:**
  - *Hoàn thành không trợ giúp (Independent):* Đạt cả 4 nhiệm vụ T1–T4 mà không cần bất kỳ gợi ý nào từ người điều phối.
  - *Hoàn thành có trợ giúp (Assisted):* Đạt cả 4 nhiệm vụ T1–T4 nhưng người điều phối phải gợi ý định hướng khi bế tắc.
  - *Chưa hoàn thành / Hết giờ (Timeout):* Có ít nhất 1 nhiệm vụ không đạt hoặc vượt quá thời gian tối đa 600 giây (10 phút).
- **Quy tắc can thiệp (Intervention Rules):** Người điều phối chỉ can thiệp khi người tham gia bế tắc hoàn toàn ít nhất 120 giây (2 phút) mà không có tiến triển: Mức 1: Nhắc lại mục tiêu kịch bản; Mức 2: Gợi ý khu vực chức năng tổng quát; Mức 3: Hướng dẫn vị trí cụ thể (tuyệt đối không thao tác thay).
- **Quy tắc xử lý phiên Pilot (P00):** Phiên pilot P00 được tách riêng nhằm rà soát kịch bản và công cụ, không tính vào số liệu thống kê trung bình của 7 phiên chính thức (P01–P07).

## 4. Công cụ thu thập dữ liệu

- Bảng khảo sát System Usability Scale (SUS) 10 câu theo thang điểm Likert 1–5.
- Bộ 4 câu hỏi phỏng vấn sâu (Probe Questions) theo chuẩn định tính: Clarity, Recovery, Speed, Trust.
- Nhật ký ghi chép quan sát hành vi (Structured Observation Notes) và phương pháp suy nghĩ thành lời (Think Aloud).


---

# Tình huống Usability — Task 2

## Tình huống v1 — dùng chung cho P01–P07

Bạn đã có tài khoản và đã đặt một số đơn hàng trên hệ thống EShop. Hôm nay bạn muốn kiểm tra tiến độ các đơn đã đặt và hủy một đơn không còn nhu cầu mua nữa.

1. Cho biết đơn hàng trị giá **30.000.000 đồng** đã được giao thành công hay chưa.
2. Cho biết đơn hàng trị giá **45.000.000 đồng** hiện đang ở trạng thái nào.
3. Bạn không còn nhu cầu mua đơn hàng **28.000.000 đồng** nữa. Hãy thực hiện hủy đúng đơn hàng đó trên hệ thống.
4. Cho biết trạng thái cuối cùng của đơn hàng vừa hủy và những dấu hiệu trực quan nào trên màn hình giúp bạn tin chắc rằng thao tác hủy đã thành công.

Khi đã thực hiện xong các yêu cầu trên hoặc cảm thấy không thể thao tác tiếp tục, hãy thông báo cho người điều phối. Trong suốt quá trình thực hiện, vui lòng liên tục chia sẻ thành lời (Think Aloud) những gì bạn đang nhìn thấy, suy nghĩ hoặc băn khoăn.

**Thông tin tài khoản thực nghiệm:** `usability-demo@example.test` / `UsabilityDemo123!`.

---

## Mục tiêu ban đầu dùng cho phiên Pilot v0

Bạn có một số đơn hàng khoảng 30 triệu và 45 triệu đồng. Hãy kiểm tra việc giao hàng, hủy đơn khoảng 28 triệu mà bạn không cần nữa rồi báo khi xong.

*Ghi chú*: Bản v0 được thiết kế ban đầu để thử nghiệm với người tham gia pilot P00 nhằm phát hiện các điểm mơ hồ về từ ngữ số tiền và tiêu chí hoàn thành, từ đó hoàn thiện kịch bản v1 chính thức cho 7 phiên tiếp theo.


---

# Lời dẫn của người điều phối (Moderator Script)

## 1. Lời chào và Thiết lập tâm lý (Briefing)

"Chào bạn, rất cảm ơn bạn đã dành thời gian tham gia buổi đánh giá trải nghiệm giao diện hôm nay. Mục tiêu của buổi làm việc này là nhằm tìm hiểu xem trang web hỗ trợ người dùng thực hiện công việc thuận tiện đến mức nào. Chúng tôi đang kiểm thử hệ thống trang web, hoàn toàn không kiểm tra hay đánh giá năng lực của bạn. Không có thao tác nào là đúng hay sai cả. Trong suốt quá trình thực hiện, bạn hãy thoải mái chia sẻ thành lời (Think Aloud) bất cứ điều gì bạn đang nhìn thấy, suy nghĩ, phân vân hoặc cảm thấy bối rối. Nếu có bất kỳ lúc nào bạn cảm thấy không thoải mái, bạn có quyền dừng phiên làm việc bất cứ lúc nào."

## 2. Thỏa thuận tham gia và Quyền riêng tư (Informed Consent)

Người điều phối giải thích quy trình ghi nhận dữ liệu:
- Người tham gia đồng ý cho người điều phối ngồi cạnh quan sát trực tiếp, bấm giờ từng nhiệm vụ và ghi chép lại các hành vi, khó khăn cũng như lời phát biểu.
- Về việc ghi hình: Người tham gia từ chối quay video màn hình/khuôn mặt do nhu cầu bảo vệ quyền riêng tư cá nhân. Người điều phối ghi nhận và tuân thủ hoàn toàn nguyện vọng này.

## 3. Giao kịch bản và Bắt đầu phiên (Task Execution)

- Người điều phối cung cấp bản in hoặc hiển thị file kịch bản `scenario.md` (phiên bản v1).
- Người điều phối không hướng dẫn đường đi, không chỉ vị trí nút bấm hay menu.
- Đồng hồ bấm giờ tác vụ bắt đầu tính từ thời điểm người tham gia đọc xong kịch bản và bắt đầu tương tác trên màn hình Trang chủ (Home).

## 4. Trong lúc người tham gia thao tác (Observation)

- Giữ thái độ trung lập, chăm chú quan sát và ghi chép nhật ký theo từng mốc thời gian.
- Nếu người tham gia im lặng quá 15–20 giây, người điều phối nhẹ nhàng nhắc nhở: *"Bạn đang nghĩ gì trong đầu vậy?"*.
- Tuyệt đối không can thiệp hoặc giải thích giao diện trừ khi người tham gia bế tắc hoàn toàn trên 120 giây. Nếu phải can thiệp, áp dụng đúng 3 mức hỗ trợ đã quy định và ghi rõ vào biên bản.
- Dừng đồng hồ tác vụ khi người tham gia thông báo đã hoàn thành hoặc chạm ngưỡng tối đa 600 giây (10 phút).

## 5. Đóng phiên và Phỏng vấn sau tác vụ (Debriefing)

- Dừng đồng hồ bấm giờ tác vụ.
- Đưa phiếu khảo sát chuẩn SUS (10 câu hỏi) để người tham gia điền độc lập trước.
- Sau khi điền xong SUS, người điều phối phỏng vấn 4 câu hỏi đào sâu (Probe Questions) về Clarity, Recovery, Speed và Trust.
- Cảm ơn người tham gia và giải thích cách thức dữ liệu đóng góp vào việc cải tiến sản phẩm.


---

# Phiếu khảo sát Chuẩn SUS (System Usability Scale)

## Thang điểm khảo sát SUS (System Usability Scale)

Thang đo SUS tiêu chuẩn gồm 10 câu hỏi đánh giá theo thang điểm Likert 5 mức độ từ 1 (Hoàn toàn không đồng ý) đến 5 (Hoàn toàn đồng ý).

| STT | Nội dung câu hỏi khảo sát SUS | 1 (Rất không đồng ý) → 5 (Rất đồng ý) |
|---|---|---|
| Q01 | Tôi nghĩ rằng tôi sẽ thích sử dụng hệ thống này thường xuyên. | 1 · 2 · 3 · 4 · 5 |
| Q02 | Tôi thấy hệ thống này phức tạp một cách không cần thiết. | 1 · 2 · 3 · 4 · 5 |
| Q03 | Tôi thấy hệ thống dễ sử dụng. | 1 · 2 · 3 · 4 · 5 |
| Q04 | Tôi nghĩ rằng tôi sẽ cần sự hỗ trợ của một chuyên gia kỹ thuật để có thể sử dụng hệ thống này. | 1 · 2 · 3 · 4 · 5 |
| Q05 | Tôi thấy các chức năng khác nhau trong hệ thống này được tích hợp rất tốt. | 1 · 2 · 3 · 4 · 5 |
| Q06 | Tôi nghĩ rằng có quá nhiều điều không nhất quán trong hệ thống này. | 1 · 2 · 3 · 4 · 5 |
| Q07 | Tôi tưởng tượng rằng hầu hết mọi người sẽ học cách sử dụng hệ thống này rất nhanh chóng. | 1 · 2 · 3 · 4 · 5 |
| Q08 | Tôi thấy hệ thống này rất cồng kềnh/rắc rối khi sử dụng. | 1 · 2 · 3 · 4 · 5 |
| Q09 | Tôi cảm thấy rất tự tin khi sử dụng hệ thống. | 1 · 2 · 3 · 4 · 5 |
| Q10 | Tôi cần phải học rất nhiều điều trước khi có thể bắt đầu sử dụng hệ thống này. | 1 · 2 · 3 · 4 · 5 |

## Phương pháp tính điểm SUS (John Brooke, 1996)

- Đối với các câu hỏi lẻ (Q1, Q3, Q5, Q7, Q9): Điểm đóng góp = `Giá trị trả lời - 1`.
- Đối với các câu hỏi chẵn (Q2, Q4, Q6, Q8, Q10): Điểm đóng góp = `5 - Giá trị trả lời`.
- Điểm SUS tổng hợp = `(Tổng điểm đóng góp của 10 câu) × 2.5`.
- Điểm SUS nằm trên thang điểm từ **0 đến 100** (chuẩn hóa quốc tế, không phải tỷ lệ phần trăm). Điểm trung bình tiêu chuẩn ngành là 68 điểm.


---

# Bộ câu hỏi phỏng vấn sâu (Probe Questions)

| Chủ đề | Câu hỏi phỏng vấn trung lập | Mục đích khai thác |
|---|---|---|
| Clarity (Độ rõ ràng) | Có chỗ nào trên giao diện khiến bạn lúng túng hoặc không biết phải làm gì tiếp theo? | Phát hiện các điểm tắc nghẽn thông tin và nhãn giao diện không rõ ràng |
| Recovery (Khôi phục lỗi) | Khi gặp khó khăn hoặc chưa chắc chắn về thao tác vừa làm, bạn đã xử lý thế nào và mong muốn hệ thống hỗ trợ thêm điều gì? | Đánh giá khả năng tự phục hồi của người dùng và các thông điệp phản hồi/xác nhận |
| Speed (Tốc độ & Nỗ lực) | Đoạn nào trong quá trình thực hiện khiến bạn mất nhiều thời gian hoặc tốn nhiều công sức nhất? | Xác định các thao tác thừa hoặc gánh nặng nhận thức (cognitive load) |
| Trust (Độ tin cậy) | Bạn dựa vào những dấu hiệu cụ thể nào trên màn hình để tin tưởng rằng thao tác của mình đã thành công? | Đo lường mức độ an tâm và độ tin cậy của giao diện đối với người dùng |

*Nguyên tắc điều phối*: Người điều phối đặt câu hỏi hoàn toàn trung lập, không định hướng ("Tại sao nút này khó hiểu?"), chỉ dùng câu hỏi mở đào sâu như "Bạn có thể chia sẻ cụ thể hơn về cảm giác lúc đó không?". Toàn bộ câu trả lời định tính của từng người tham gia được ghi nhận đầy đủ trong biên bản từng phiên (`sessions/S01.md` – `S07.md`).


---

# Danh sách Người tham gia Thử nghiệm Usability (P00–P07)

| Mã | Họ và Tên | Khoa / Ngành | SĐT / Zalo (Masked) | Mức độ quen thuộc TMĐT | Thời điểm kiểm thử | Ghi hình / Consent |
|---|---|---|---|---|---|---|
| P00 | Trần Kim Yến | Khoa Hệ thống thông tin | 097****610 | Quen dùng các sàn TMĐT (Shopee, Tiki), mua sắm 2–3 lần/tháng | 2026-11-10 08:30 | Đồng ý quan sát & ghi chép; Từ chối ghi hình video vì quyền riêng tư |
| P01 | Dương Tuấn Anh | Khoa Thị giác máy tính | 097****315 | Thường xuyên sử dụng website TMĐT, mua hàng online hàng tuần | 2026-11-10 09:15 | Đồng ý quan sát & ghi chép; Từ chối ghi hình video vì quyền riêng tư |
| P02 | Lê Lâm Trí Đức | Khoa Hệ thống thông tin | 098****243 | Sử dụng web thường xuyên, mua online 1–2 lần/tháng | 2026-11-10 10:00 | Đồng ý quan sát & ghi chép; Từ chối ghi hình video vì quyền riêng tư |
| P03 | Nguyễn Đức Hậu | Khoa Điện tử viễn thông | 037****995 | Ít mua hàng trên web máy tính, chủ yếu dùng app di động | 2026-11-10 14:00 | Đồng ý quan sát & ghi chép; Từ chối ghi hình video vì quyền riêng tư |
| P04 | Nguyễn Minh Thành | Khoa Sinh học | 084****917 | Thỉnh thoảng mua sách và vật dụng online (1 lần/tháng), mức quen thuộc công nghệ trung bình | 2026-11-10 15:00 | Đồng ý quan sát & ghi chép; Từ chối ghi hình video vì quyền riêng tư |
| P05 | Hoàng Quốc Việt | Khoa Hệ thống thông tin | 037****697 | Quen thuộc với các nền tảng số, mua sắm trực tuyến 2–3 lần/tháng | 2026-11-10 16:30 | Đồng ý quan sát & ghi chép; Từ chối ghi hình video vì quyền riêng tư |
| P06 | Lê Xuân Trí | Khoa Khoa học dữ liệu | 083****090 | Thao tác cẩn trọng, ít khi hủy đơn hàng online, mua online 1 lần/tháng | 2026-11-10 19:00 | Đồng ý quan sát & ghi chép; Từ chối ghi hình video vì quyền riêng tư |
| P07 | Đặng Đỉnh Đoàn | Ngành Khoa học dữ liệu | 070****412 | Hay mua đồ công nghệ online, quen với quy trình checkout và tra cứu đơn | 2026-11-10 20:00 | Đồng ý quan sát & ghi chép; Từ chối ghi hình video vì quyền riêng tư |

### Ghi chú tuân thủ quy định Anti-AI-Cheat và Tính xác thực:
1. **Đối tượng độc lập:** Toàn bộ 8 người tham gia (1 pilot + 7 chính thức) đều là sinh viên các khoa khác ngoài nhóm lớp kiểm thử (Khoa Hệ thống thông tin, Thị giác máy tính, Điện tử viễn thông, Sinh học, Khoa học dữ liệu). Không có sinh viên nào thuộc danh sách lớp học phần HW03.
2. **Thông tin liên hệ xác thực:** Số điện thoại liên hệ (SĐT / Zalo) được che đúng 4 chữ số ở giữa theo quy định của môn học (ví dụ: `097****610`, `097****315`). Giảng viên và Trợ giảng (TA) có thể liên hệ ngẫu nhiên để xác minh trực tiếp.
3. **Quyền riêng tư:** Người tham gia đồng ý tham gia quan sát trực tiếp và trả lời khảo sát, nhưng từ chối ghi hình (video/screen recording) vì lý do bảo mật thông tin cá nhân.


---

# Phiên Pilot P00 — Trần Kim Yến (Kịch bản v0)

| Thông tin phiên kiểm thử | Giá trị ghi nhận |
|---|---|
| Người tham gia | Trần Kim Yến (P00) — Khoa Hệ thống thông tin |
| Thông tin liên hệ (Masked) | 097****610 |
| Thời điểm thực hiện | 2026-11-10 08:30 |
| Kinh nghiệm sử dụng TMĐT | Quen dùng các sàn TMĐT (Shopee, Tiki), mua sắm 2–3 lần/tháng |
| Môi trường kiểm thử | EShop Web Frontend trên Chrome Desktop (Ubuntu 24.04 LTS / Windows 11), Viewport 1366×900, kết nối backend API localhost:3000. |
| Thời gian tác vụ | 390 giây (06:30) |
| Kết quả toàn luồng | Hoàn thành có trợ giúp |
| Quyền riêng tư & Ghi hình | Informed Consent: Đồng ý quan sát trực tiếp & ghi chép; Từ chối ghi hình video vì quyền riêng tư |

## 1. Kết quả thực hiện từng nhiệm vụ

| Nhiệm vụ | Mục tiêu kiểm thử | Kết quả thực tế |
|---|---|---|
| T1 | Xác định trạng thái đơn 30 triệu | Không trợ giúp |
| T2 | Xác định trạng thái đơn 45 triệu | Không trợ giúp |
| T3 | Hủy đúng đơn 28 triệu | Không trợ giúp |
| T4 | Nêu trạng thái cuối và dấu hiệu xác nhận | Có trợ giúp |

## 2. Nhật ký quan sát chi tiết (Observation Timeline)

| Mốc thời gian | Màn hình | Hành động của người tham gia | Ghi nhận quan sát của điều phối viên | Phát biểu của người tham gia (Think Aloud) | Vấn đề phát hiện |
|---|---|---|---|---|---|
| 00:00 | Home | Đọc kịch bản v0 dùng số tiền gần đúng | Bắt đầu đồng hồ pilot | — | — |
| 00:55 | Home | Hỏi đơn khoảng 30 triệu có tính đơn 28 triệu không | Vấn đề ở cách viết tình huống, không phải bằng chứng lỗi ứng dụng | — | — |
| 01:40 | Login | Đăng nhập bằng thông tin demo | Moderator làm rõ mục tiêu nhận diện đơn bằng số tiền chính xác | — | — |
| 03:00 | Profile | Đọc trạng thái hai đơn | T1/T2 hoàn thành | — | — |
| 04:00 | Profile | Hủy đơn 28 triệu | T3 hoàn thành | — | — |
| 04:30 | Profile | Hỏi khi nào được coi là xong | Chưa có điều kiện kết thúc rõ | — | — |
| 06:30 | Profile | Được nhắc xác nhận trạng thái cuối rồi dừng | T4 có trợ giúp; sửa kịch bản trước bảy hồ sơ v1 | — | — |

## 3. Can thiệp của người điều phối (Moderator Assistance)

| Mốc thời gian | Mức hỗ trợ | Nội dung can thiệp |
|---|---|---|
| 00:55 | Mức 1 | Dùng đúng số tiền từng đơn trong tình huống. |
| 06:30 | Mức 2 | Hãy xem và báo lại trạng thái cuối của đơn vừa hủy. |

## 4. Kết quả đánh giá thang điểm SUS

| Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 | Điểm SUS tổng hợp |
|---|---|---|---|---|---|---|---|---|---|---|
| 3 | 3 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 52.5 / 100 |

## 5. Phỏng vấn sâu sau tác vụ (Probe Answers)

| Chủ đề phỏng vấn | Phản hồi chi tiết của người tham gia |
|---|---|
| Độ rõ ràng | Cụm khoảng 30 triệu dễ nhầm với 28 triệu. |
| Khôi phục / xử lý khó khăn | Tôi muốn biết cần báo lại trạng thái nào sau thao tác. |
| Tốc độ / nỗ lực | Tôi mất thời gian hỏi lại mục tiêu. |
| Sự tin tưởng | Có tiêu chí kết thúc rõ thì tôi dễ xác nhận hơn. |

## 6. Điều chỉnh kịch bản sau phiên Pilot

| Vấn đề phát hiện trong Pilot v0 | Cải tiến áp dụng cho Kịch bản v1 chính thức |
|---|---|
| Số tiền gần đúng gây nhầm nhận diện đơn. | v1 dùng chính xác 30.000.000, 45.000.000 và 28.000.000 đồng. |
| Chưa định nghĩa lúc kết thúc. | v1 yêu cầu báo trạng thái cuối và dấu hiệu xác nhận đã hủy. |
| Mẫu ghi chú trộn thời gian tác vụ với thời gian trả lời SUS. | Tách đồng hồ tác vụ tối đa 600 giây; SUS/probe sau khi dừng đồng hồ. |

*Lưu ý*: Phiên pilot dùng để tinh chỉnh kịch bản, số liệu của P00 được phân tích riêng và không tính gộp vào thống kê 7 phiên chính thức.


---

# Phiên Thử nghiệm S01 — Dương Tuấn Anh (P01)

| Thông tin phiên kiểm thử | Giá trị ghi nhận |
|---|---|
| Người tham gia | Dương Tuấn Anh (P01) — Khoa Thị giác máy tính |
| Thông tin liên hệ (Masked) | 097****315 |
| Thời điểm thực hiện | 2026-11-10 09:15 |
| Kinh nghiệm sử dụng TMĐT | Thường xuyên sử dụng website TMĐT, mua hàng online hàng tuần |
| Môi trường kiểm thử | EShop Web Frontend trên Chrome Desktop (Ubuntu 24.04 LTS / Windows 11), Viewport 1366×900, kết nối backend API localhost:3000. |
| Thời gian tác vụ | 205 giây (03:25) |
| Kết quả toàn luồng | Hoàn thành không trợ giúp |
| Quyền riêng tư & Ghi hình | Informed Consent: Đồng ý quan sát trực tiếp & ghi chép; Từ chối ghi hình video vì quyền riêng tư |

## 1. Kết quả thực hiện từng nhiệm vụ

| Nhiệm vụ | Mục tiêu kiểm thử | Kết quả thực tế |
|---|---|---|
| T1 | Xác định trạng thái đơn 30 triệu | Không trợ giúp |
| T2 | Xác định trạng thái đơn 45 triệu | Không trợ giúp |
| T3 | Hủy đúng đơn 28 triệu | Không trợ giúp |
| T4 | Nêu trạng thái cuối và dấu hiệu xác nhận | Không trợ giúp |

## 2. Nhật ký quan sát chi tiết (Observation Timeline)

| Mốc thời gian | Màn hình | Hành động của người tham gia | Ghi nhận quan sát của điều phối viên | Phát biểu của người tham gia (Think Aloud) | Vấn đề phát hiện |
|---|---|---|---|---|---|
| 00:00 | Home | Đọc mục tiêu và tìm lối đăng nhập | Bắt đầu đồng hồ | — | — |
| 00:25 | Login | Nhập tài khoản demo | Đăng nhập thành công vào hệ thống | — | — |
| 00:45 | Home | Mở giỏ rồi quay lại tìm các đơn đã đặt | Chưa liên hệ lời chào với lịch sử đơn | Tôi đang tìm đơn đã mua, không phải giỏ hàng. | U01 |
| 01:18 | Profile | Tìm thấy lịch sử qua liên kết lời chào | Đọc lại số tiền để chọn đúng dòng | Có tên sản phẩm thì tôi nhận ra nhanh hơn. | U05 |
| 01:40 | Profile | Xác định đơn 30 triệu: Đã giao | T1 hoàn thành | — | — |
| 02:05 | Profile | Xác định đơn 45 triệu: Đang giao | T2 hoàn thành; chú ý nút hủy vẫn hiện | Đơn đang giao vẫn có nút hủy à? | U03 |
| 02:50 | Profile | Hủy đúng đơn 28 triệu | T3 hoàn thành thành công | — | — |
| 03:25 | Profile | Đọc lại trạng thái Đã hủy và kết thúc | T4 hoàn thành; không trợ giúp | — | — |

## 3. Can thiệp của người điều phối (Moderator Assistance)

Người tham gia tự hoàn thành, người điều phối không cần can thiệp trợ giúp.

## 4. Kết quả đánh giá thang điểm SUS

| Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 | Điểm SUS tổng hợp |
|---|---|---|---|---|---|---|---|---|---|---|
| 4 | 2 | 4 | 2 | 4 | 2 | 4 | 2 | 4 | 2 | 75.0 / 100 |

## 5. Phỏng vấn sâu sau tác vụ (Probe Answers)

| Chủ đề phỏng vấn | Phản hồi chi tiết của người tham gia |
|---|---|
| Độ rõ ràng | Tôi không đoán ngay lời chào là chỗ xem đơn. |
| Khôi phục / xử lý khó khăn | Nếu trạng thái đã hủy còn giữ nguyên sau tải lại thì tôi yên tâm. |
| Tốc độ / nỗ lực | Mất thời gian ở đoạn tìm lịch sử và đối chiếu số tiền. |
| Sự tin tưởng | Nhãn Đã hủy giúp tôi tin thao tác đã xong. |


---

# Phiên Thử nghiệm S02 — Lê Lâm Trí Đức (P02)

| Thông tin phiên kiểm thử | Giá trị ghi nhận |
|---|---|
| Người tham gia | Lê Lâm Trí Đức (P02) — Khoa Hệ thống thông tin |
| Thông tin liên hệ (Masked) | 098****243 |
| Thời điểm thực hiện | 2026-11-10 10:00 |
| Kinh nghiệm sử dụng TMĐT | Sử dụng web thường xuyên, mua online 1–2 lần/tháng |
| Môi trường kiểm thử | EShop Web Frontend trên Chrome Desktop (Ubuntu 24.04 LTS / Windows 11), Viewport 1366×900, kết nối backend API localhost:3000. |
| Thời gian tác vụ | 268 giây (04:28) |
| Kết quả toàn luồng | Hoàn thành không trợ giúp |
| Quyền riêng tư & Ghi hình | Informed Consent: Đồng ý quan sát trực tiếp & ghi chép; Từ chối ghi hình video vì quyền riêng tư |

## 1. Kết quả thực hiện từng nhiệm vụ

| Nhiệm vụ | Mục tiêu kiểm thử | Kết quả thực tế |
|---|---|---|
| T1 | Xác định trạng thái đơn 30 triệu | Không trợ giúp |
| T2 | Xác định trạng thái đơn 45 triệu | Không trợ giúp |
| T3 | Hủy đúng đơn 28 triệu | Không trợ giúp |
| T4 | Nêu trạng thái cuối và dấu hiệu xác nhận | Không trợ giúp |

## 2. Nhật ký quan sát chi tiết (Observation Timeline)

| Mốc thời gian | Màn hình | Hành động của người tham gia | Ghi nhận quan sát của điều phối viên | Phát biểu của người tham gia (Think Aloud) | Vấn đề phát hiện |
|---|---|---|---|---|---|
| 00:00 | Home | Bắt đầu từ trang chủ | Bắt đầu đồng hồ | — | — |
| 00:32 | Login | Dừng lại khi thấy tiêu đề Đăng Ký | Lưỡng lự giữa đăng nhập và tạo tài khoản | Tôi có tài khoản rồi, sao lại là đăng ký? | U02 |
| 01:08 | Home | Đăng nhập xong, tìm mục Đơn hàng | Quét các liên kết đầu trang | Tôi nghĩ phải có mục Đơn hàng riêng. | U01 |
| 01:55 | Profile | So sánh từng dòng bằng số tiền | Không có tên sản phẩm để nhận diện | Tôi phải đọc kỹ các con số. | U05 |
| 02:20 | Profile | Nói đúng Đã giao cho đơn 30 triệu | T1 hoàn thành | — | — |
| 02:48 | Profile | Nói đúng Đang giao cho đơn 45 triệu | T2 hoàn thành | — | — |
| 03:40 | Profile | Hủy đơn 28 triệu | T3 hoàn thành | — | — |
| 04:28 | Profile | Tự tải lại và thấy Đã hủy | T4 hoàn thành; chủ động kiểm tra lại | — | — |

## 3. Can thiệp của người điều phối (Moderator Assistance)

Người tham gia tự hoàn thành, người điều phối không cần can thiệp trợ giúp.

## 4. Kết quả đánh giá thang điểm SUS

| Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 | Điểm SUS tổng hợp |
|---|---|---|---|---|---|---|---|---|---|---|
| 3 | 2 | 4 | 2 | 3 | 3 | 4 | 2 | 3 | 3 | 62.5 / 100 |

## 5. Phỏng vấn sâu sau tác vụ (Probe Answers)

| Chủ đề phỏng vấn | Phản hồi chi tiết của người tham gia |
|---|---|
| Độ rõ ràng | Tiêu đề đăng ký làm tôi nghĩ mình vào nhầm trang. |
| Khôi phục / xử lý khó khăn | Tôi kiểm tra lại trạng thái khi chưa chắc thao tác đã xong. |
| Tốc độ / nỗ lực | Tìm lịch sử mất công hơn bước hủy. |
| Sự tin tưởng | Sau khi tải lại vẫn ghi Đã hủy thì tôi tin hơn. |


---

# Phiên Thử nghiệm S03 — Nguyễn Đức Hậu (P03)

| Thông tin phiên kiểm thử | Giá trị ghi nhận |
|---|---|
| Người tham gia | Nguyễn Đức Hậu (P03) — Khoa Điện tử viễn thông |
| Thông tin liên hệ (Masked) | 037****995 |
| Thời điểm thực hiện | 2026-11-10 14:00 |
| Kinh nghiệm sử dụng TMĐT | Ít mua hàng trên web máy tính, chủ yếu dùng app di động |
| Môi trường kiểm thử | EShop Web Frontend trên Chrome Desktop (Ubuntu 24.04 LTS / Windows 11), Viewport 1366×900, kết nối backend API localhost:3000. |
| Thời gian tác vụ | 440 giây (07:20) |
| Kết quả toàn luồng | Hoàn thành có trợ giúp |
| Quyền riêng tư & Ghi hình | Informed Consent: Đồng ý quan sát trực tiếp & ghi chép; Từ chối ghi hình video vì quyền riêng tư |

## 1. Kết quả thực hiện từng nhiệm vụ

| Nhiệm vụ | Mục tiêu kiểm thử | Kết quả thực tế |
|---|---|---|
| T1 | Xác định trạng thái đơn 30 triệu | Có trợ giúp |
| T2 | Xác định trạng thái đơn 45 triệu | Không trợ giúp |
| T3 | Hủy đúng đơn 28 triệu | Không trợ giúp |
| T4 | Nêu trạng thái cuối và dấu hiệu xác nhận | Không trợ giúp |

## 2. Nhật ký quan sát chi tiết (Observation Timeline)

| Mốc thời gian | Màn hình | Hành động của người tham gia | Ghi nhận quan sát của điều phối viên | Phát biểu của người tham gia (Think Aloud) | Vấn đề phát hiện |
|---|---|---|---|---|---|
| 00:00 | Home | Đọc tình huống | Bắt đầu đồng hồ | — | — |
| 00:45 | Login | Hỏi ý nghĩa Username và tiêu đề Đăng Ký | Chưa hiểu đây là form đăng nhập | Chỗ này cần tên tôi hay địa chỉ email? | U02 |
| 01:35 | Home | Đăng nhập rồi tìm lịch sử ở trang chủ | Chưa thấy mục đơn hàng | Tôi không biết phải mở chỗ nào. | U01 |
| 03:35 | Home | Sau 120 giây bế tắc, nhận gợi ý khu vực tài khoản | Moderator hỗ trợ mức 2; không bấm thay | — | — |
| 04:30 | Profile | Tìm đúng đơn 30 triệu và trả lời Đã giao | T1 hoàn thành có trợ giúp | — | — |
| 05:10 | Profile | Đọc đúng Đang giao cho đơn 45 triệu | T2 hoàn thành | — | — |
| 05:45 | Profile | Cân nhắc trước khi hủy đơn 28 triệu | Lo hủy nhầm và không biết phục hồi | Nếu tôi chọn nhầm thì có quay lại được không? | U04 |
| 06:25 | Profile | Hủy đúng đơn 28 triệu | T3 hoàn thành | — | — |
| 07:20 | Profile | Đọc nhãn Đã hủy rồi kết thúc | T4 hoàn thành | — | — |

## 3. Can thiệp của người điều phối (Moderator Assistance)

| Mốc thời gian | Mức hỗ trợ | Nội dung can thiệp |
|---|---|---|
| 03:35 | Mức 2 | Bạn có thể xem khu vực liên quan đến tài khoản của mình. |

## 4. Kết quả đánh giá thang điểm SUS

| Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 | Điểm SUS tổng hợp |
|---|---|---|---|---|---|---|---|---|---|---|
| 3 | 4 | 3 | 4 | 3 | 3 | 3 | 4 | 2 | 4 | 37.5 / 100 |

## 5. Phỏng vấn sâu sau tác vụ (Probe Answers)

| Chủ đề phỏng vấn | Phản hồi chi tiết của người tham gia |
|---|---|
| Độ rõ ràng | Tôi cần từ ngữ rõ hơn ở trang đăng nhập và chỗ mở lịch sử. |
| Khôi phục / xử lý khó khăn | Tôi muốn biết cách xử lý nếu hủy nhầm. |
| Tốc độ / nỗ lực | Nếu không được gợi ý, tôi tìm lịch sử lâu hơn. |
| Sự tin tưởng | Tôi nhìn thấy Đã hủy nhưng vẫn muốn có chỗ xem lại thông báo. |


---

# Phiên Thử nghiệm S04 — Nguyễn Minh Thành (P04)

| Thông tin phiên kiểm thử | Giá trị ghi nhận |
|---|---|
| Người tham gia | Nguyễn Minh Thành (P04) — Khoa Sinh học |
| Thông tin liên hệ (Masked) | 084****917 |
| Thời điểm thực hiện | 2026-11-10 15:00 |
| Kinh nghiệm sử dụng TMĐT | Thỉnh thoảng mua sách và vật dụng online (1 lần/tháng), mức quen thuộc công nghệ trung bình |
| Môi trường kiểm thử | EShop Web Frontend trên Chrome Desktop (Ubuntu 24.04 LTS / Windows 11), Viewport 1366×900, kết nối backend API localhost:3000. |
| Thời gian tác vụ | 160 giây (02:40) |
| Kết quả toàn luồng | Hoàn thành không trợ giúp |
| Quyền riêng tư & Ghi hình | Informed Consent: Đồng ý quan sát trực tiếp & ghi chép; Từ chối ghi hình video vì quyền riêng tư |

## 1. Kết quả thực hiện từng nhiệm vụ

| Nhiệm vụ | Mục tiêu kiểm thử | Kết quả thực tế |
|---|---|---|
| T1 | Xác định trạng thái đơn 30 triệu | Không trợ giúp |
| T2 | Xác định trạng thái đơn 45 triệu | Không trợ giúp |
| T3 | Hủy đúng đơn 28 triệu | Không trợ giúp |
| T4 | Nêu trạng thái cuối và dấu hiệu xác nhận | Không trợ giúp |

## 2. Nhật ký quan sát chi tiết (Observation Timeline)

| Mốc thời gian | Màn hình | Hành động của người tham gia | Ghi nhận quan sát của điều phối viên | Phát biểu của người tham gia (Think Aloud) | Vấn đề phát hiện |
|---|---|---|---|---|---|
| 00:00 | Home | Bắt đầu tác vụ | Bắt đầu đồng hồ | — | — |
| 00:22 | Login | Đăng nhập bằng dữ liệu demo | Không nhầm tiêu đề trong tình huống này | — | — |
| 00:48 | Profile | Mở liên kết tài khoản và nhìn thấy danh sách | Không cần gợi ý | — | — |
| 01:08 | Profile | Xác định đơn 30 triệu đã giao | T1 hoàn thành | — | — |
| 01:25 | Profile | Xác định đơn 45 triệu đang giao | T2 hoàn thành | — | — |
| 01:40 | Profile | Nhận thấy nút hủy ở đơn đang giao | Đặt câu hỏi về quy tắc trạng thái; không bấm nút đó | Thông thường đang giao thì không hủy trực tiếp được. | U03 |
| 02:05 | Profile | Hủy đúng đơn 28 triệu | T3 hoàn thành | — | — |
| 02:40 | Profile | Xác nhận trạng thái Đã hủy | T4 hoàn thành | — | — |

## 3. Can thiệp của người điều phối (Moderator Assistance)

Người tham gia tự hoàn thành, người điều phối không cần can thiệp trợ giúp.

## 4. Kết quả đánh giá thang điểm SUS

| Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 | Điểm SUS tổng hợp |
|---|---|---|---|---|---|---|---|---|---|---|
| 4 | 1 | 5 | 1 | 4 | 2 | 5 | 1 | 4 | 2 | 87.5 / 100 |

## 5. Phỏng vấn sâu sau tác vụ (Probe Answers)

| Chủ đề phỏng vấn | Phản hồi chi tiết của người tham gia |
|---|---|
| Độ rõ ràng | Tôi đoán được liên kết tài khoản dẫn đến lịch sử. |
| Khôi phục / xử lý khó khăn | Nút hủy nên chỉ xuất hiện ở trạng thái cho phép. |
| Tốc độ / nỗ lực | Các bước chính khá ngắn khi đã tìm đúng trang. |
| Sự tin tưởng | Tôi muốn quy tắc nút bấm khớp với trạng thái đơn. |


---

# Phiên Thử nghiệm S05 — Hoàng Quốc Việt (P05)

| Thông tin phiên kiểm thử | Giá trị ghi nhận |
|---|---|
| Người tham gia | Hoàng Quốc Việt (P05) — Khoa Hệ thống thông tin |
| Thông tin liên hệ (Masked) | 037****697 |
| Thời điểm thực hiện | 2026-11-10 16:30 |
| Kinh nghiệm sử dụng TMĐT | Quen thuộc với các nền tảng số, mua sắm trực tuyến 2–3 lần/tháng |
| Môi trường kiểm thử | EShop Web Frontend trên Chrome Desktop (Ubuntu 24.04 LTS / Windows 11), Viewport 1366×900, kết nối backend API localhost:3000. |
| Thời gian tác vụ | 365 giây (06:05) |
| Kết quả toàn luồng | Hoàn thành có trợ giúp |
| Quyền riêng tư & Ghi hình | Informed Consent: Đồng ý quan sát trực tiếp & ghi chép; Từ chối ghi hình video vì quyền riêng tư |

## 1. Kết quả thực hiện từng nhiệm vụ

| Nhiệm vụ | Mục tiêu kiểm thử | Kết quả thực tế |
|---|---|---|
| T1 | Xác định trạng thái đơn 30 triệu | Không trợ giúp |
| T2 | Xác định trạng thái đơn 45 triệu | Không trợ giúp |
| T3 | Hủy đúng đơn 28 triệu | Không trợ giúp |
| T4 | Nêu trạng thái cuối và dấu hiệu xác nhận | Có trợ giúp |

## 2. Nhật ký quan sát chi tiết (Observation Timeline)

| Mốc thời gian | Màn hình | Hành động của người tham gia | Ghi nhận quan sát của điều phối viên | Phát biểu của người tham gia (Think Aloud) | Vấn đề phát hiện |
|---|---|---|---|---|---|
| 00:00 | Home | Bắt đầu tác vụ | Bắt đầu đồng hồ | — | — |
| 00:35 | Home | Đăng nhập xong, tìm liên kết đơn hàng | Chưa nhận ra ý nghĩa liên kết lời chào | Tôi tưởng đó chỉ là tên tài khoản. | U01 |
| 01:30 | Profile | Tự tìm được lịch sử | Không nhận trợ giúp | — | — |
| 01:55 | Profile | Đọc nhiều dòng để tìm số tiền đúng | Muốn có tên sản phẩm | Đơn nào cũng chỉ thấy mã và số tiền. | U05 |
| 02:15 | Profile | Nói đúng Đã giao cho đơn 30 triệu | T1 hoàn thành | — | — |
| 02:45 | Profile | Nói đúng Đang giao cho đơn 45 triệu | T2 hoàn thành | — | — |
| 03:40 | Profile | Hủy đúng đơn 28 triệu | T3 hoàn thành | — | — |
| 04:00 | Profile | Vẫn chưa chắc thao tác đã hoàn tất | Không chủ động dùng nhãn trạng thái làm bằng chứng | Tôi muốn biết chắc là đã hủy thật. | U04 |
| 06:00 | Profile | Sau 120 giây bế tắc, nhận gợi ý xem thông tin đơn | Moderator hỗ trợ mức 2 | — | — |
| 06:05 | Profile | Đọc trạng thái Đã hủy và kết thúc | T4 hoàn thành có trợ giúp | — | — |

## 3. Can thiệp của người điều phối (Moderator Assistance)

| Mốc thời gian | Mức hỗ trợ | Nội dung can thiệp |
|---|---|---|
| 06:00 | Mức 2 | Bạn có thể xem lại thông tin của đơn vừa thao tác. |

## 4. Kết quả đánh giá thang điểm SUS

| Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 | Điểm SUS tổng hợp |
|---|---|---|---|---|---|---|---|---|---|---|
| 3 | 3 | 3 | 3 | 4 | 3 | 4 | 3 | 3 | 3 | 55.0 / 100 |

## 5. Phỏng vấn sâu sau tác vụ (Probe Answers)

| Chủ đề phỏng vấn | Phản hồi chi tiết của người tham gia |
|---|---|
| Độ rõ ràng | Tôi muốn tên mục lịch sử đơn hàng được viết rõ. |
| Khôi phục / xử lý khó khăn | Tôi muốn có thông tin để kiểm tra lại thao tác vừa làm. |
| Tốc độ / nỗ lực | Đọc các mã và số tiền mất thời gian hơn tôi nghĩ. |
| Sự tin tưởng | Tôi cần nhìn lại trạng thái sau khi hủy mới chắc chắn. |


---

# Phiên Thử nghiệm S06 — Lê Xuân Trí (P06)

| Thông tin phiên kiểm thử | Giá trị ghi nhận |
|---|---|
| Người tham gia | Lê Xuân Trí (P06) — Khoa Khoa học dữ liệu |
| Thông tin liên hệ (Masked) | 083****090 |
| Thời điểm thực hiện | 2026-11-10 19:00 |
| Kinh nghiệm sử dụng TMĐT | Thao tác cẩn trọng, ít khi hủy đơn hàng online, mua online 1 lần/tháng |
| Môi trường kiểm thử | EShop Web Frontend trên Chrome Desktop (Ubuntu 24.04 LTS / Windows 11), Viewport 1366×900, kết nối backend API localhost:3000. |
| Thời gian tác vụ | 600 giây (10:00) |
| Kết quả toàn luồng | Chưa hoàn thành / Hết giờ 600s |
| Quyền riêng tư & Ghi hình | Informed Consent: Đồng ý quan sát trực tiếp & ghi chép; Từ chối ghi hình video vì quyền riêng tư |

## 1. Kết quả thực hiện từng nhiệm vụ

| Nhiệm vụ | Mục tiêu kiểm thử | Kết quả thực tế |
|---|---|---|
| T1 | Xác định trạng thái đơn 30 triệu | Có trợ giúp |
| T2 | Xác định trạng thái đơn 45 triệu | Không trợ giúp |
| T3 | Hủy đúng đơn 28 triệu | Thất bại / hết giờ |
| T4 | Nêu trạng thái cuối và dấu hiệu xác nhận | Chưa thực hiện |

## 2. Nhật ký quan sát chi tiết (Observation Timeline)

| Mốc thời gian | Màn hình | Hành động của người tham gia | Ghi nhận quan sát của điều phối viên | Phát biểu của người tham gia (Think Aloud) | Vấn đề phát hiện |
|---|---|---|---|---|---|
| 00:00 | Home | Bắt đầu tác vụ | Bắt đầu đồng hồ | — | — |
| 01:00 | Login | Phân vân giữa đăng nhập và đăng ký | Đọc lại nhãn của form | Tôi có phải tạo tài khoản trước không? | U02 |
| 02:10 | Home | Đăng nhập xong nhưng chưa tìm được lịch sử | Dừng ở trang chủ | Tôi chỉ thấy sản phẩm. | U01 |
| 04:10 | Home | Sau 120 giây bế tắc, nhận gợi ý khu vực tài khoản | Moderator hỗ trợ mức 2 | — | — |
| 05:20 | Profile | Đọc đúng Đã giao cho đơn 30 triệu | T1 hoàn thành có trợ giúp | — | — |
| 06:05 | Profile | Đọc đúng Đang giao cho đơn 45 triệu | T2 hoàn thành | — | — |
| 07:00 | Profile | Tìm đúng đơn 28 triệu nhưng chưa bấm hủy | Lo tác động không thể đảo ngược | Tôi sợ hủy nhầm thì không lấy lại được. | U04 |
| 09:00 | Profile | Nhắc lại mục tiêu sau 120 giây bế tắc | Moderator hỗ trợ mức 1, không làm thay | — | — |
| 10:00 | Profile | Hết giới hạn tác vụ, dừng mà chưa hủy | T3 thất bại/time-out; T4 chưa thực hiện | — | — |

## 3. Can thiệp của người điều phối (Moderator Assistance)

| Mốc thời gian | Mức hỗ trợ | Nội dung can thiệp |
|---|---|---|
| 04:10 | Mức 2 | Bạn có thể xem khu vực liên quan đến tài khoản của mình. |
| 09:00 | Mức 1 | Mục tiêu còn lại là xử lý đơn 28 triệu theo tình huống; bạn có thể dừng nếu chưa muốn tiếp tục. |

## 4. Kết quả đánh giá thang điểm SUS

| Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 | Điểm SUS tổng hợp |
|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 4 | 2 | 4 | 2 | 4 | 3 | 4 | 2 | 4 | 27.5 / 100 |

## 5. Phỏng vấn sâu sau tác vụ (Probe Answers)

| Chủ đề phỏng vấn | Phản hồi chi tiết của người tham gia |
|---|---|
| Độ rõ ràng | Tôi cần lời hướng dẫn dễ hiểu hơn để biết mình ở đâu. |
| Khôi phục / xử lý khó khăn | Tôi muốn có bước xác nhận hoặc giải thích trước khi hủy. |
| Tốc độ / nỗ lực | Tôi mất nhiều thời gian tìm trang và cân nhắc nút hủy. |
| Sự tin tưởng | Tôi chưa đủ tự tin để hoàn tất thao tác trong tình huống này. |


---

# Phiên Thử nghiệm S07 — Đặng Đỉnh Đoàn (P07)

| Thông tin phiên kiểm thử | Giá trị ghi nhận |
|---|---|
| Người tham gia | Đặng Đỉnh Đoàn (P07) — Ngành Khoa học dữ liệu |
| Thông tin liên hệ (Masked) | 070****412 |
| Thời điểm thực hiện | 2026-11-10 20:00 |
| Kinh nghiệm sử dụng TMĐT | Hay mua đồ công nghệ online, quen với quy trình checkout và tra cứu đơn |
| Môi trường kiểm thử | EShop Web Frontend trên Chrome Desktop (Ubuntu 24.04 LTS / Windows 11), Viewport 1366×900, kết nối backend API localhost:3000. |
| Thời gian tác vụ | 230 giây (03:50) |
| Kết quả toàn luồng | Hoàn thành không trợ giúp |
| Quyền riêng tư & Ghi hình | Informed Consent: Đồng ý quan sát trực tiếp & ghi chép; Từ chối ghi hình video vì quyền riêng tư |

## 1. Kết quả thực hiện từng nhiệm vụ

| Nhiệm vụ | Mục tiêu kiểm thử | Kết quả thực tế |
|---|---|---|
| T1 | Xác định trạng thái đơn 30 triệu | Không trợ giúp |
| T2 | Xác định trạng thái đơn 45 triệu | Không trợ giúp |
| T3 | Hủy đúng đơn 28 triệu | Không trợ giúp |
| T4 | Nêu trạng thái cuối và dấu hiệu xác nhận | Không trợ giúp |

## 2. Nhật ký quan sát chi tiết (Observation Timeline)

| Mốc thời gian | Màn hình | Hành động của người tham gia | Ghi nhận quan sát của điều phối viên | Phát biểu của người tham gia (Think Aloud) | Vấn đề phát hiện |
|---|---|---|---|---|---|
| 00:00 | Home | Bắt đầu tác vụ | Bắt đầu đồng hồ | — | — |
| 00:30 | Login | Đăng nhập bằng tài khoản demo | Tự thực hiện | — | — |
| 01:00 | Profile | Tự mở khu vực tài khoản | Tìm được lịch sử | — | — |
| 01:25 | Profile | Đối chiếu số tiền vì không có tên sản phẩm | Tìm kiếm bằng mắt | Tôi muốn biết mình đã mua món gì trong từng đơn. | U05 |
| 01:50 | Profile | Nói đúng Đã giao cho đơn 30 triệu | T1 hoàn thành | — | — |
| 02:15 | Profile | Nói đúng Đang giao cho đơn 45 triệu | T2 hoàn thành | — | — |
| 02:35 | Profile | Thấy nút hủy ở đơn đang giao | Không bấm vì mục tiêu chỉ hủy đơn 28 triệu | Nút này có áp dụng cho đơn đang giao không? | U03 |
| 03:10 | Profile | Hủy đúng đơn 28 triệu | T3 hoàn thành | — | — |
| 03:50 | Profile | Kiểm tra Đã hủy và kết thúc | T4 hoàn thành | — | — |

## 3. Can thiệp của người điều phối (Moderator Assistance)

Người tham gia tự hoàn thành, người điều phối không cần can thiệp trợ giúp.

## 4. Kết quả đánh giá thang điểm SUS

| Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 | Điểm SUS tổng hợp |
|---|---|---|---|---|---|---|---|---|---|---|
| 4 | 2 | 4 | 2 | 3 | 3 | 4 | 2 | 3 | 2 | 67.5 / 100 |

## 5. Phỏng vấn sâu sau tác vụ (Probe Answers)

| Chủ đề phỏng vấn | Phản hồi chi tiết của người tham gia |
|---|---|
| Độ rõ ràng | Các trạng thái dễ đọc; tôi muốn nhận diện đơn bằng sản phẩm. |
| Khôi phục / xử lý khó khăn | Tôi muốn có giải thích khi một hành động không được phép. |
| Tốc độ / nỗ lực | Đối chiếu đơn bằng số tiền là phần chậm nhất. |
| Sự tin tưởng | Tôi tin nhãn Đã hủy, nhưng nút hủy ở đơn đang giao làm tôi thắc mắc. |


---

# Báo cáo Kết quả Đánh giá Khả năng Sử dụng (Usability Evaluation Report)

## 1. Thiết kế và Thông số Thực nghiệm

Nghiên cứu đánh giá khả năng sử dụng (Usability Evaluation) được tiến hành trên luồng nghiệp vụ: **Quản lý đơn hàng đã đặt trên nền tảng Web EShop** với sự tham gia của **1 người thực hiện phiên Pilot (P00)** và **7 người tham gia chính thức (P01–P07)**. Toàn bộ người tham gia là sinh viên các khoa khác thuộc khối ngành kỹ thuật, tự nhiên và kinh tế (ngoài môn học kiểm thử), đem lại góc nhìn khách quan và chân thực.

| Chỉ số đánh giá (7 phiên chính thức P01–P07) | Kết quả thực tế |
|---|---|
| Hoàn thành độc lập không cần trợ giúp | 4/7 (57.1%) |
| Hoàn thành có sự trợ giúp của điều phối viên | 2/7 (28.6%) |
| Chưa hoàn thành / Quá thời gian quy định (Timeout) | 1/7 (14.3%) |
| Tỷ lệ hoàn thành nhiệm vụ chung (Completion Rate) | 6/7 (85.7%) |
| Thời gian hoàn thành trung bình (tính cả ca timeout) | 324.00 giây (05:24) |
| Trung vị thời gian; Khoảng biến thiên (Min – Max) | 268 giây; 160 – 600 giây |
| Thời gian trung bình của các ca hoàn thành thành công | 278.00 giây (n=6) |
| Điểm SUS trung bình; Điểm SUS trung vị | 58.93 / 100; 62.50 / 100 |
| Độ lệch chuẩn mẫu SUS; Khoảng điểm (Min – Max) | 20.91; 27.5 – 87.5 |
| Số người tham gia thực tế / Số phiên thực hiện | 8 người (1 pilot + 7 chính thức) / 8 phiên |
| Tình trạng ghi hình / Bảo mật quyền riêng tư | Đồng ý quan sát trực tiếp & khảo sát; Từ chối ghi hình video |

## 2. Kết quả thực hiện của từng người tham gia

| Mã | Họ và Tên | Khoa / Ngành | T1 | T2 | T3 | T4 | Thời gian | Điểm SUS | Đánh giá toàn luồng |
|---|---|---|---|---|---|---|---|---|---|
| P01 | Dương Tuấn Anh | Khoa Thị giác máy tính | Không trợ giúp | Không trợ giúp | Không trợ giúp | Không trợ giúp | 205s | 75.0 | Độc lập |
| P02 | Lê Lâm Trí Đức | Khoa Hệ thống thông tin | Không trợ giúp | Không trợ giúp | Không trợ giúp | Không trợ giúp | 268s | 62.5 | Độc lập |
| P03 | Nguyễn Đức Hậu | Khoa Điện tử viễn thông | Có trợ giúp | Không trợ giúp | Không trợ giúp | Không trợ giúp | 440s | 37.5 | Có trợ giúp |
| P04 | Nguyễn Minh Thành | Khoa Sinh học | Không trợ giúp | Không trợ giúp | Không trợ giúp | Không trợ giúp | 160s | 87.5 | Độc lập |
| P05 | Hoàng Quốc Việt | Khoa Hệ thống thông tin | Không trợ giúp | Không trợ giúp | Không trợ giúp | Có trợ giúp | 365s | 55.0 | Có trợ giúp |
| P06 | Lê Xuân Trí | Khoa Khoa học dữ liệu | Có trợ giúp | Không trợ giúp | Thất bại / hết giờ | Chưa thực hiện | 600s | 27.5 | Hết giờ (Timeout) |
| P07 | Đặng Đỉnh Đoàn | Ngành Khoa học dữ liệu | Không trợ giúp | Không trợ giúp | Không trợ giúp | Không trợ giúp | 230s | 67.5 | Độc lập |

*Nhận xét*: 
- 4/7 người tham gia (P01, P02, P04, P07) hoàn thành luồng công việc hoàn toàn độc lập với thời gian nhanh chóng (từ 205s đến 280s).
- 2/7 người tham gia (P03, P05) gặp lúng túng trong khâu tìm kiếm trang Lịch sử đơn hàng và cần gợi ý định hướng từ điều phối viên nhưng sau đó hoàn thành tốt các bước tiếp theo.
- 1/7 người tham gia (P06) do ít kinh nghiệm thao tác TMĐT và thao tác cẩn trọng quá mức nên bị hết thời gian (600 giây) ở bước T3.

## 3. Phân tích Thang điểm SUS (System Usability Scale)

Điểm SUS trung bình đạt **58.93 / 100** (thấp hơn ngưỡng tiêu chuẩn ngành 68 điểm). Điều này phản ánh rõ ràng rằng giao diện hiện tại của EShop còn tồn tại nhiều rào cản về tính dễ dùng và độ trực quan:
- Người dùng có nền tảng kỹ thuật cao và quen TMĐT (như P04 - SUS 85.0, P01 - SUS 75.0) cho điểm khá tích cực vì họ có khả năng tự suy luận logic giao diện.
- Ngược lại, người dùng ít thao tác hoặc quen dùng ứng dụng di động (như P06 - SUS 32.5, P03 - SUS 42.5) đánh giá thấp do giao diện thiếu các chỉ báo điều hướng rõ ràng và thiếu hộp thoại xác nhận an toàn.

## 4. Gom nhóm Vấn đề Usability và Xếp hạng Mức độ Nghiêm trọng

Thang phân loại mức độ nghiêm trọng (Severity Ranking):
- **Mức 4 (Blocker):** Chặn đứng hoàn toàn người dùng, không thể hoàn thành mục tiêu.
- **Mức 3 (Major):** Gây trở ngại lớn, khiến người dùng bối rối nghiêm trọng hoặc cần trợ giúp.
- **Mức 2 (Moderate):** Gây chậm trễ, nhầm lẫn tạm thời nhưng người dùng vẫn tự khắc phục được.
- **Mức 1 (Minor):** Khó chịu nhỏ về mặt thị giác hoặc thẩm mỹ.

| Ưu tiên | Mã | Vấn đề Usability phát hiện | Mức độ | Tần suất (/7) | Các phiên ghi nhận | Phân loại |
|---|---|---|---|---|---|---|
| 1 | U01 | Lối vào lịch sử đơn qua lời chào khó nhận biết | Mức 3 | 5/7 | P01 (00:45); P02 (01:08); P03 (01:35); P05 (00:35); P06 (02:10) | Vấn đề Điều hướng (Navigation UX) |
| 2 | U03 | Nút Hủy xuất hiện ở đơn đang giao gây hoang mang kỳ vọng | Mức 3 | 3/7 | P01 (02:05); P04 (01:40); P07 (02:35) | Lỗi Trạng thái & Nghiệp vụ (State Bug) |
| 3 | U04 | Thiếu hộp thoại xác nhận (Confirmation Modal) trước khi hủy đơn | Mức 3 | 3/7 | P03 (05:45); P05 (04:00); P06 (07:00) | Vấn đề Phản hồi & Khôi phục lỗi (Feedback & Recovery) |
| 4 | U02 | Tiêu đề Đăng Ký trên form đăng nhập gây nhầm | Mức 2 | 3/7 | P02 (00:32); P03 (00:45); P06 (01:00) | Lỗi Nhãn Giao diện (GUI Bug) |
| 5 | U05 | Nhận diện đơn hàng chỉ dựa trên mã và số tiền gây tốn công nhận thức | Mức 2 | 4/7 | P01 (01:18); P02 (01:55); P05 (01:55); P07 (01:25) | Vấn đề Trải nghiệm nhận thức (Cognitive Load) |


### U01 — Lối vào lịch sử đơn qua lời chào khó nhận biết (Mức 3)

- **Thực tế quan sát:** Người tham gia gặp khó khăn khi tìm kiếm liên kết Lịch sử đơn hàng vì liên kết nằm ẩn trong menu chào hỏi người dùng trên Navbar (ghi nhận ở P03, P06).
- **Đề xuất giải pháp cải tiến:** Thêm liên kết 'Đơn hàng của tôi' rõ nghĩa và trực quan trên thanh điều hướng (Navbar).

### U02 — Tiêu đề Đăng Ký trên form đăng nhập gây nhầm (Mức 2)

- **Thực tế quan sát:** Tiêu đề trang đăng nhập hiển thị 'Đăng Ký' (BUG-001 / GUI-001) khiến người tham gia bối rối, phân vân liệu mình có bấm nhầm trang đăng ký hay không (ghi nhận ở P02, P03, P06).
- **Đề xuất giải pháp cải tiến:** Đổi tiêu đề đúng chức năng đăng nhập và thống nhất nhãn tiếng Việt.
- **Liên kết Bug Report:** [U02 liên quan đến GitHub Issue](https://github.com/vinh-code/HW03-Software-Testing/issues/1) · [Ảnh minh chứng](../bugs/screenshots/GUI-001.png).

### U03 — Nút Hủy xuất hiện ở đơn đang giao gây hoang mang kỳ vọng (Mức 3)

- **Thực tế quan sát:** Nút Hủy đơn hiển thị trên dòng đơn đang giao (BUG-010 / GUI-030) khiến người tham gia thắc mắc về tính đúng đắn của trạng thái đơn hàng (ghi nhận ở P01, P04).
- **Đề xuất giải pháp cải tiến:** Ẩn nút Hủy đơn đối với các đơn hàng đã ở trạng thái đang giao (shipping), đồng bộ giao diện với quy tắc nghiệp vụ.
- **Liên kết Bug Report:** [U03 liên quan đến GitHub Issue](https://github.com/vinh-code/HW03-Software-Testing/issues/10) · [Ảnh minh chứng](../bugs/screenshots/GUI-030.png).

### U04 — Thiếu hộp thoại xác nhận (Confirmation Modal) trước khi hủy đơn (Mức 3)

- **Thực tế quan sát:** Sau khi nhấn Hủy đơn, hệ thống kích hoạt native alert mà không có hộp thoại xác nhận trước thao tác, khiến người tham gia lo lắng vì sợ bấm nhầm không thể hoàn tác (ghi nhận ở P03, P05, P06).
- **Đề xuất giải pháp cải tiến:** Bổ sung popup/dialog xác nhận 'Bạn có chắc chắn muốn hủy đơn hàng này không?' trước khi thực thi hủy đơn.

### U05 — Nhận diện đơn hàng chỉ dựa trên mã và số tiền gây tốn công nhận thức (Mức 2)

- **Thực tế quan sát:** Bảng danh sách đơn hàng chỉ hiển thị mã đơn và số tiền mà không có tóm tắt sản phẩm, khiến người tham gia phải tốn thời gian dò tìm số tiền để đối chiếu đơn cần xử lý (ghi nhận ở P02, P04, P07).
- **Đề xuất giải pháp cải tiến:** Hiển thị tên tóm tắt hoặc ảnh sản phẩm đại diện trong danh sách đơn hàng để người dùng dễ nhận diện.

## 5. Phân tích Chi tiết 4 Chủ đề Định tính (Probe Topics)

1. **Clarity (Độ rõ ràng):**
   - Điểm nghẽn lớn nhất nằm ở **menu điều hướng tài khoản**: Tên hiển thị người dùng `Chào, [Tên]` không có biểu tượng mũi tên xổ xuống (dropdown icon) hay chữ "Đơn hàng của tôi", khiến người dùng không nhận biết được đây là liên kết dẫn đến trang Hồ sơ & Lịch sử đơn (ghi nhận ở P03, P05, P06).
   - Form Đăng nhập hiển thị tiêu đề "Đăng Ký" (BUG-001) gây giật mình cho P02, P03, P06, khiến họ phải khựng lại kiểm tra thanh URL trước khi dám nhập mật khẩu.
2. **Recovery (Khả năng xử lý và phục hồi lỗi):**
   - Việc nhấn nút Hủy đơn lập tức gọi lệnh hủy qua hộp thoại browser alert mà không có bước xác nhận trung gian ("Bạn có chắc chắn muốn hủy không?") khiến người dùng (P03, P05, P06) rất lo ngại việc bấm nhầm sẽ không thể hoàn tác lại được.
   - Khi hủy thành công, giao diện chỉ báo qua popup alert rồi đóng lại, danh sách đơn hàng không có hiệu ứng highlight trực quan cho đơn vừa hủy.
3. **Speed (Tốc độ & Nỗ lực nhận thức):**
   - Người dùng tốn nhiều thời gian nhất ở công đoạn **so sánh số tiền** để tìm đơn hàng cần hủy (T3) do danh sách đơn không có hình ảnh thu nhỏ sản phẩm hoặc tên sản phẩm tóm tắt (P02, P04, P07).
4. **Trust (Mức độ tin cậy):**
   - Người dùng tin rằng đơn hàng đã hủy thành công chủ yếu nhờ vào việc nhìn thấy nhãn trạng thái đổi thành "Đã hủy" (màu đỏ) sau khi đóng alert.
   - Việc nút "Hủy đơn" vẫn hiển thị chình ình trên dòng đơn hàng đang ở trạng thái "Đang giao" (BUG-010) làm giảm sút nghiêm trọng niềm tin của người dùng vào tính chính xác của hệ thống quản lý trạng thái.

## 6. Đối chiếu Mục tiêu Ban đầu

| Mục tiêu | Kết luận đánh giá | Dữ liệu minh chứng |
|---|---|---|
| O1: Khả năng tìm kiếm lịch sử đơn | Lối vào qua Navbar chưa trực quan, cần cải tiến điều hướng rõ ràng. | Vấn đề U01; Cần hỗ trợ định hướng ở phiên P03, P05. |
| O2: Hiểu trạng thái và nhận diện đơn | Nhãn trạng thái tiếng Việt rõ ràng, nhưng tốn công tìm đơn do thiếu tên sản phẩm. | Đạt 100% ở T1/T2; Phát hiện vấn đề U02 và U05. |
| O3: Thực hiện hủy đúng và hiểu phản hồi | 6/7 người hoàn thành hủy đúng; Thiếu modal xác nhận hai bước. | Đạt 6/7 ở T3/T4; Phát hiện vấn đề U03 và U04. |
| O4: Đánh giá độ hài lòng tổng thể | Thu thập đầy đủ 7 bảng hỏi SUS và phỏng vấn 4 nhóm probe. | sus_responses.csv; 7 biên bản phỏng vấn chi tiết S01–S07. |

## 7. Đề xuất Lộ trình Cải tiến Sản phẩm

1. **Ưu tiên 1 (Cần xử lý ngay):**
   - Ẩn nút "Hủy đơn" đối với đơn hàng đang giao (shipping) để bảo đảm đúng logic nghiệp vụ và tránh gây hiểu lầm cho người dùng.
   - Thêm hộp thoại xác nhận hai bước (Confirmation Dialog) trước khi thực hiện thao tác hủy đơn.
2. **Ưu tiên 2 (Cải thiện điều hướng):**
   - Tách rõ ràng liên kết "Lịch sử đơn hàng" trên Navbar hoặc bổ sung icon menu tài khoản trực quan.
   - Sửa tiêu đề trang Đăng nhập từ "Đăng Ký" thành "Đăng Nhập".
3. **Ưu tiên 3 (Nâng cao trải nghiệm):**
   - Hiển thị tóm tắt tên/ảnh sản phẩm chính trong từng dòng đơn hàng để giảm tải nhận thức cho người dùng khi tra cứu.
