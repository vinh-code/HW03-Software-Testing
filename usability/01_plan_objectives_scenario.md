# Kế hoạch Task 2 — quản lý đơn đã đặt

**KẾT QUẢ MÔ PHỎNG PHỤC VỤ BÀI TẬP** — hồ sơ, thời gian, diễn biến và câu trả lời đều do AI tạo cho tình huống giả định. Không có phỏng vấn, người tham gia, đồng ý ghi hình hoặc video thực tế.

## Phạm vi

Một luồng: đăng nhập → tìm lịch sử → đọc trạng thái → hủy đúng đơn chưa xử lý → kiểm tra phản hồi. Bốn mục tiêu nhỏ thuộc cùng luồng này. Chưa đối chiếu lựa chọn với thành viên khác trong nhóm.

| Mục tiêu | Điều cần xem xét | Chỉ số trong mô phỏng |
|---|---|---|
| O1 | Khả năng tìm lịch sử đơn | Khó khăn U01; trợ giúp ở T1 |
| O2 | Hiểu trạng thái và nhận diện đơn | Kết quả T1/T2; U02/U05 |
| O3 | Thực hiện hủy đúng và hiểu phản hồi | Kết quả T3/T4; U03/U04 |
| O4 | Cảm nhận về quá trình | SUS và bốn nhóm probe |

## Môi trường và dữ liệu giả định

Giả định: EShop web, Chrome desktop / Ubuntu, viewport 1366×900; không chạy phiên người dùng trong bộ dữ liệu này.

| Đơn ký hiệu — không phải ID DB | Số tiền | Trạng thái ban đầu |
|---|---|---|
| A | 28.000.000 đồng | Chờ xác nhận |
| B | 1.500.000 đồng | Đã xác nhận |
| C | 45.000.000 đồng | Đang giao |
| D | 30.000.000 đồng | Đã giao |

Tài khoản và bốn đơn được giả định trở về cùng trạng thái ban đầu cho mỗi hồ sơ. Không seed, reset hoặc khởi động lại backend để tạo bộ mô phỏng này. `seed_orders.mjs` là công cụ cũ cho kiểm thử thật, không được chạy trong quy trình này.

## Tình huống v1 — dùng chung cho P01–P07

Bạn đã có tài khoản và đã đặt một số đơn hàng trên EShop. Hôm nay bạn muốn kiểm tra các đơn đã đặt và xử lý một đơn không còn nhu cầu.

1. Cho biết đơn **30.000.000 đồng** đã được giao hay chưa.
2. Cho biết đơn **45.000.000 đồng** hiện ở trạng thái nào.
3. Bạn không còn muốn mua đơn **28.000.000 đồng**. Hãy hủy đúng đơn đó.
4. Cho biết trạng thái cuối của đơn vừa hủy và điều gì trên trang khiến bạn biết thao tác đã hoàn tất.

Khi đã thực hiện xong hoặc thấy không thể tiếp tục, hãy báo cho người điều phối. Trong lúc thao tác, hãy nói điều bạn đang tìm hoặc đang phân vân. Không cần thao tác lên các đơn khác.

**Thông tin demo trong thế giới giả định:** `usability-demo@example.test` / `UsabilityDemo123!`. Tài khoản này chưa được tạo trên SUT; không dùng thông tin trên như tài khoản đã sẵn sàng chạy thật.

## Mục tiêu ban đầu dùng cho pilot v0

Bạn có một số đơn hàng khoảng 30 triệu và 45 triệu đồng. Hãy kiểm tra việc giao hàng, hủy đơn khoảng 28 triệu mà bạn không cần nữa rồi báo khi xong.

v0 cố ý thể hiện bản nháp còn mơ hồ để minh họa quy trình pilot. Phiên pilot là mô phỏng, không phải cuộc thử nghiệm đã diễn ra.

## Quy tắc ghi nhận

- T1: nhận diện đúng đơn 30 triệu và trả lời Đã giao; bao gồm bước đăng nhập và tìm lịch sử.
- T2: nhận diện đúng đơn 45 triệu và trả lời Đang giao.
- T3: chỉ đơn 28 triệu chuyển thành Đã hủy trong diễn biến giả định.
- T4: hồ sơ nói được trạng thái Đã hủy và nêu nhãn trạng thái/thông tin sau tải lại làm căn cứ.
- Toàn luồng không trợ giúp: cả bốn mục tiêu đạt và không có can thiệp. Có trợ giúp: đạt cả bốn, nhưng đã có gợi ý. Chưa hoàn thành: có mục tiêu thất bại hoặc chưa thực hiện khi dừng.
- Đồng hồ tác vụ bắt đầu sau khi đã đọc mục tiêu, từ Home chưa đăng nhập; dừng khi báo kết quả cuối hoặc chạm 600 giây. Không cộng thời gian SUS/probe.
- Khi bế tắc ít nhất 120 giây: mức 1 nhắc lại mục tiêu, mức 2 gợi ý khu vực, mức 3 chỉ vị trí; ghi mức và thời điểm, không bấm thay.
- Pilot P00 tách khỏi bảy hồ sơ v1; không cộng vào điểm trung bình hoặc tần suất phát hiện.

## Công cụ và sản phẩm

Dùng SUS tiếng Việt trong tài liệu sẵn có (chưa xác minh thẩm định bản dịch), bốn câu probe trung lập, timeline giả định, CSV và Excel. Không tạo danh tính, liên hệ, chữ ký đồng ý, ngày phỏng vấn hay video giả.
