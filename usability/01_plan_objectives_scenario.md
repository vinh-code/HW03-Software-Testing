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
