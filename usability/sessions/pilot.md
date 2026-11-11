# Pilot P00 — kịch bản v0

**KẾT QUẢ MÔ PHỎNG PHỤC VỤ BÀI TẬP** — hồ sơ, thời gian, diễn biến và câu trả lời đều do AI tạo cho tình huống giả định. Không có phỏng vấn, người tham gia, đồng ý ghi hình hoặc video thực tế.

| Thông tin | Giá trị |
|---|---|
| Hồ sơ giả định | Hồ sơ pilot giả định: non-IT, nhóm tuổi 25–34 |
| Kinh nghiệm giả định | Mua online khoảng mỗi tháng |
| Môi trường giả định | Giả định: EShop web, Chrome desktop / Ubuntu, viewport 1366×900; không chạy phiên người dùng trong bộ dữ liệu này. |
| Ngày giờ phỏng vấn / liên hệ / đồng ý / video | Không áp dụng — không có phiên thật |
| Thời gian tác vụ giả định | 390 giây (06:30) |
| Kết quả toàn luồng | Hoàn thành có trợ giúp |

## Mục tiêu và kết quả giả định

| Mục | Mục tiêu | Kết quả |
|---|---|---|
| T1 | Xác định trạng thái đơn 30 triệu | Không trợ giúp |
| T2 | Xác định trạng thái đơn 45 triệu | Không trợ giúp |
| T3 | Hủy đúng đơn 28 triệu | Không trợ giúp |
| T4 | Nêu trạng thái cuối và dấu hiệu xác nhận | Có trợ giúp |

## Nhật ký mô phỏng — mốc tương đối, không phải timestamp video

| Mốc | Màn hình | Hành động giả định | Ghi nhận giả định | Lời thoại giả định | Nhóm |
|---|---|---|---|---|---|
| 00:00 | Home | Đọc kịch bản v0 dùng số tiền gần đúng | Bắt đầu đồng hồ pilot giả định | — | — |
| 00:55 | Home | Hỏi đơn khoảng 30 triệu có tính đơn 28 triệu không | Vấn đề ở cách viết tình huống, không phải bằng chứng lỗi ứng dụng | — | — |
| 01:40 | Login | Đăng nhập bằng thông tin demo | Moderator làm rõ mục tiêu nhận diện đơn bằng số tiền chính xác | — | — |
| 03:00 | Profile | Đọc trạng thái hai đơn | T1/T2 hoàn thành | — | — |
| 04:00 | Profile | Hủy đơn 28 triệu | T3 hoàn thành | — | — |
| 04:30 | Profile | Hỏi khi nào được coi là xong | Chưa có điều kiện kết thúc rõ | — | — |
| 06:30 | Profile | Được nhắc xác nhận trạng thái cuối rồi dừng | T4 có trợ giúp; sửa kịch bản trước bảy hồ sơ v1 | — | — |

## Can thiệp giả định của moderator

| Mốc | Mức | Nội dung |
|---|---|---|
| 00:55 | 1 | Dùng đúng số tiền từng đơn trong tình huống. |
| 06:30 | 2 | Hãy xem và báo lại trạng thái cuối của đơn vừa hủy. |

## SUS giả định — trả lời trước probe

| Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 | Điểm SUS |
|---|---|---|---|---|---|---|---|---|---|---|
| 3 | 3 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 52.5 |

## Câu trả lời mở giả định

| Chủ đề | Lời đáp giả định |
|---|---|
| Độ rõ ràng | Cụm khoảng 30 triệu dễ nhầm với 28 triệu. |
| Khôi phục / xử lý khó khăn | Tôi muốn biết cần báo lại trạng thái nào sau thao tác. |
| Tốc độ / nỗ lực | Tôi mất thời gian hỏi lại mục tiêu. |
| Sự tin tưởng | Có tiêu chí kết thúc rõ thì tôi dễ xác nhận hơn. |

## Điều chỉnh trước bảy phiên v1

| Vấn đề mô phỏng | Điều chỉnh kịch bản |
|---|---|
| Số tiền gần đúng gây nhầm nhận diện đơn. | v1 dùng chính xác 30.000.000, 45.000.000 và 28.000.000 đồng. |
| Chưa định nghĩa lúc kết thúc. | v1 yêu cầu báo trạng thái cuối và dấu hiệu xác nhận đã hủy. |
| Mẫu ghi chú trộn thời gian tác vụ với thời gian trả lời SUS. | Tách đồng hồ tác vụ tối đa 600 giây; SUS/probe sau khi dừng đồng hồ. |

SUS và thời gian pilot không được gộp vào phân tích bảy hồ sơ chính.
