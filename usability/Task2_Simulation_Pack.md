# Task 2 — Bộ hồ sơ mô phỏng hoàn chỉnh

**KẾT QUẢ MÔ PHỎNG PHỤC VỤ BÀI TẬP** — hồ sơ, thời gian, diễn biến và câu trả lời đều do AI tạo cho tình huống giả định. Không có phỏng vấn, người tham gia, đồng ý ghi hình hoặc video thực tế.

Sinh viên: Phạm Quang Vinh — 23120202 — 23120202@student.hcmus.edu.vn.


## Nội dung bộ hồ sơ

1. Tình huống và kế hoạch đánh giá.
2. Lời dẫn, phiếu SUS và câu hỏi mở.
3. Hồ sơ pilot P00 và điều chỉnh kịch bản.
4. Bảy phiên S01–S07, mỗi phiên có timeline, kết quả, SUS và probe.
5. Phân tích, ưu tiên cải tiến và nguồn tham chiếu.

Thông tin sinh viên đã điền sẵn. Các hồ sơ P00–P07 là giả định; không có người tham gia thực tế. Excel và CSV đi kèm chứa dữ liệu để đối chiếu số liệu trong PDF.


# Tình huống Task 2

**KẾT QUẢ MÔ PHỎNG PHỤC VỤ BÀI TẬP** — hồ sơ, thời gian, diễn biến và câu trả lời đều do AI tạo cho tình huống giả định. Không có phỏng vấn, người tham gia, đồng ý ghi hình hoặc video thực tế.

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


# Lời dẫn điều phối — kịch bản minh họa

**KẾT QUẢ MÔ PHỎNG PHỤC VỤ BÀI TẬP** — hồ sơ, thời gian, diễn biến và câu trả lời đều do AI tạo cho tình huống giả định. Không có phỏng vấn, người tham gia, đồng ý ghi hình hoặc video thực tế.

## Mở đầu

“Cảm ơn bạn. Mục tiêu hôm nay là xem trang web hỗ trợ công việc của bạn như thế nào. Chúng tôi đánh giá sản phẩm, không đánh giá năng lực của bạn. Trong lúc thao tác, hãy nói điều bạn đang nghĩ hoặc đang tìm. Bạn có thể dừng bất cứ lúc nào.”

Không nói mọi chỗ khó hiểu đều là lỗi của sản phẩm; ghi nhận trước, phân tích sau.

## Trước tác vụ

Trong phiên thật, giải thích mục đích và xin phép riêng việc ghi màn hình/ghi âm; ghi nhận lựa chọn thực tế. Trong bộ mô phỏng này, các trường đồng ý và ghi hình đều không áp dụng.

Đưa `scenario.md` v1, không giải thích đường dẫn hay vị trí nút. Bắt đầu đồng hồ tác vụ sau khi người tham gia đã đọc mục tiêu.

## Trong tác vụ

Quan sát trung lập. Có thể nhắc “Bạn đang nghĩ gì?” khi họ im lặng. Chỉ gợi ý khi hoàn toàn bế tắc ít nhất 120 giây; ghi chính xác thời điểm, nội dung và mức hỗ trợ. Không thao tác thay. Dừng ở 600 giây nếu chưa xong.

## Kết thúc

Dừng đồng hồ tác vụ. Đưa SUS để trả lời trước khi thảo luận; tiếp đến hỏi bốn probe. Cảm ơn và giải thích cách sử dụng dữ liệu. Các lời thoại hoàn thành trong bộ này là nội dung mô phỏng, không phải bản chép lời một cuộc phỏng vấn.


# Phiếu SUS — bản tiếng Việt dùng trong bài tập

**KẾT QUẢ MÔ PHỎNG PHỤC VỤ BÀI TẬP** — hồ sơ, thời gian, diễn biến và câu trả lời đều do AI tạo cho tình huống giả định. Không có phỏng vấn, người tham gia, đồng ý ghi hình hoặc video thực tế.

Bản diễn đạt tiếng Việt có sẵn trong workspace; chưa xác minh đây là bản dịch đã được thẩm định.

Participant đánh giá mỗi câu từ **1 (Hoàn toàn không đồng ý)** đến **5 (Hoàn toàn đồng ý)**.
Hoàn thành **ngay sau** tác vụ, trước khi hỏi probe.

| # | Câu | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 1 | Tôi nghĩ tôi sẽ muốn dùng trang web này thường xuyên. | ☐ | ☐ | ☐ | ☐ | ☐ |
| 2 | Tôi thấy trang web này phức tạp một cách không cần thiết. | ☐ | ☐ | ☐ | ☐ | ☐ |
| 3 | Tôi thấy trang web này dễ sử dụng. | ☐ | ☐ | ☐ | ☐ | ☐ |
| 4 | Tôi nghĩ tôi cần sự hỗ trợ của người có chuyên môn để dùng được trang web này. | ☐ | ☐ | ☐ | ☐ | ☐ |
| 5 | Tôi thấy các chức năng trong trang web này được tích hợp tốt. | ☐ | ☐ | ☐ | ☐ | ☐ |
| 6 | Tôi thấy trang web này có quá nhiều điểm không nhất quán. | ☐ | ☐ | ☐ | ☐ | ☐ |
| 7 | Tôi nghĩ hầu hết mọi người sẽ học cách dùng trang web này rất nhanh. | ☐ | ☐ | ☐ | ☐ | ☐ |
| 8 | Tôi thấy trang web này rất cồng kềnh, khó dùng. | ☐ | ☐ | ☐ | ☐ | ☐ |
| 9 | Tôi cảm thấy rất tự tin khi dùng trang web này. | ☐ | ☐ | ☐ | ☐ | ☐ |
| 10 | Tôi cần học nhiều thứ trước khi có thể bắt đầu dùng trang web này. | ☐ | ☐ | ☐ | ☐ | ☐ |

## Cách tính điểm

- Câu **lẻ** (1,3,5,7,9): điểm đóng góp = `câu trả lời − 1`
- Câu **chẵn** (2,4,6,8,10): điểm đóng góp = `5 − câu trả lời`
- **SUS = tổng 10 đóng góp × 2.5** (thang 0-100)


## Nguồn và cách dùng

Công thức đối chiếu với [John Brooke — SUS](https://digital.ahrq.gov/sites/default/files/docs/survey/systemusabilityscale%2528sus%2529_comp%255B1%255D.pdf). Điểm 0–100 không phải phần trăm. Bộ này chỉ minh họa tính điểm; không suy ra mức hài lòng thực tế hoặc gán hạng A–F.

Câu trả lời bảy hồ sơ: `sus_responses.csv`; pilot lưu riêng trong `data/simulation.json`.


# Bốn câu hỏi mở sau SUS

**KẾT QUẢ MÔ PHỎNG PHỤC VỤ BÀI TẬP** — hồ sơ, thời gian, diễn biến và câu trả lời đều do AI tạo cho tình huống giả định. Không có phỏng vấn, người tham gia, đồng ý ghi hình hoặc video thực tế.

| Chủ đề | Câu hỏi trung lập |
|---|---|
| Clarity | Có chỗ nào khiến bạn không biết phải làm gì tiếp theo? |
| Recovery | Khi thấy khó khăn hoặc chưa chắc về thao tác, bạn đã làm gì và cần thêm điều gì? |
| Speed | Đoạn nào khiến bạn mất nhiều thời gian hoặc công sức nhất? |
| Trust | Bạn dựa vào điều gì để tin rằng thông tin hoặc thao tác đã đúng? |

Câu đào sâu tùy diễn biến: “Bạn có thể nói rõ hơn điều đó không?”. Không đưa sẵn đánh giá tốt/xấu, không hỏi “Có phải nút này gây khó hiểu không?”. Bốn câu trả lời của mỗi hồ sơ đã được điền ở `sessions/S01.md`…`S07.md` và workbook; tất cả là lời đáp giả định.


# Danh sách hồ sơ giả định P00–P07

**KẾT QUẢ MÔ PHỎNG PHỤC VỤ BÀI TẬP** — hồ sơ, thời gian, diễn biến và câu trả lời đều do AI tạo cho tình huống giả định. Không có phỏng vấn, người tham gia, đồng ý ghi hình hoặc video thực tế.

| Mã | Vai trò | Đặc điểm giả định | Kinh nghiệm giả định | Liên hệ / ngày phỏng vấn / ghi hình |
|---|---|---|---|---|
| P00 | Pilot | Hồ sơ pilot giả định: non-IT, nhóm tuổi 25–34 | Mua online khoảng mỗi tháng | Không áp dụng — không có người thật |
| P01 | Phiên chính mô phỏng | Nhân viên văn phòng, nhóm tuổi 25–34; non-IT | Mua online 2–3 lần/tháng | Không áp dụng — không có người thật |
| P02 | Phiên chính mô phỏng | Nhân viên bán hàng, nhóm tuổi 25–34; non-IT | Mua online khoảng mỗi tuần | Không áp dụng — không có người thật |
| P03 | Phiên chính mô phỏng | Người làm công việc hành chính, nhóm tuổi 45–54; non-IT | Ít mua online; thường dùng điện thoại | Không áp dụng — không có người thật |
| P04 | Phiên chính mô phỏng | Nhân viên kỹ thuật, nhóm tuổi 25–34; IT | Mua online thường xuyên; quen website thương mại điện tử | Không áp dụng — không có người thật |
| P05 | Phiên chính mô phỏng | Người kinh doanh tự do, nhóm tuổi 35–44; non-IT | Mua online 1–2 lần/tháng | Không áp dụng — không có người thật |
| P06 | Phiên chính mô phỏng | Người ít dùng dịch vụ trực tuyến, nhóm tuổi 45–54; non-IT | Hiếm mua online; mức quen công nghệ thấp | Không áp dụng — không có người thật |
| P07 | Phiên chính mô phỏng | Sinh viên ngành kinh tế, nhóm tuổi 18–24; non-IT | Mua online vài lần/tháng | Không áp dụng — không có người thật |

Không thay mã hồ sơ bằng tên một người thật để gán cho họ các câu trả lời này. Nếu sau này thu dữ liệu thật, lưu thành bộ dữ liệu khác với nguồn gốc và bằng chứng tương ứng.


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


# Phiên S01 — hồ sơ P01, kịch bản v1

**KẾT QUẢ MÔ PHỎNG PHỤC VỤ BÀI TẬP** — hồ sơ, thời gian, diễn biến và câu trả lời đều do AI tạo cho tình huống giả định. Không có phỏng vấn, người tham gia, đồng ý ghi hình hoặc video thực tế.

| Thông tin | Giá trị |
|---|---|
| Hồ sơ giả định | Nhân viên văn phòng, nhóm tuổi 25–34; non-IT |
| Kinh nghiệm giả định | Mua online 2–3 lần/tháng |
| Môi trường giả định | Giả định: EShop web, Chrome desktop / Ubuntu, viewport 1366×900; không chạy phiên người dùng trong bộ dữ liệu này. |
| Ngày giờ phỏng vấn / liên hệ / đồng ý / video | Không áp dụng — không có phiên thật |
| Thời gian tác vụ giả định | 205 giây (03:25) |
| Kết quả toàn luồng | Hoàn thành không trợ giúp |

## Mục tiêu và kết quả giả định

| Mục | Mục tiêu | Kết quả |
|---|---|---|
| T1 | Xác định trạng thái đơn 30 triệu | Không trợ giúp |
| T2 | Xác định trạng thái đơn 45 triệu | Không trợ giúp |
| T3 | Hủy đúng đơn 28 triệu | Không trợ giúp |
| T4 | Nêu trạng thái cuối và dấu hiệu xác nhận | Không trợ giúp |

## Nhật ký mô phỏng — mốc tương đối, không phải timestamp video

| Mốc | Màn hình | Hành động giả định | Ghi nhận giả định | Lời thoại giả định | Nhóm |
|---|---|---|---|---|---|
| 00:00 | Home | Đọc mục tiêu và tìm lối đăng nhập | Bắt đầu đồng hồ giả định | — | — |
| 00:25 | Login | Nhập tài khoản demo | Đăng nhập được theo giả định | — | — |
| 00:45 | Home | Mở giỏ rồi quay lại tìm các đơn đã đặt | Chưa liên hệ lời chào với lịch sử đơn | Tôi đang tìm đơn đã mua, không phải giỏ hàng. | U01 |
| 01:18 | Profile | Tìm thấy lịch sử qua liên kết lời chào | Đọc lại số tiền để chọn đúng dòng | Có tên sản phẩm thì tôi nhận ra nhanh hơn. | U05 |
| 01:40 | Profile | Xác định đơn 30 triệu: Đã giao | T1 hoàn thành | — | — |
| 02:05 | Profile | Xác định đơn 45 triệu: Đang giao | T2 hoàn thành; chú ý nút hủy vẫn hiện | Đơn đang giao vẫn có nút hủy à? | U03 |
| 02:50 | Profile | Hủy đúng đơn 28 triệu | T3 hoàn thành trong mô phỏng | — | — |
| 03:25 | Profile | Đọc lại trạng thái Đã hủy và kết thúc | T4 hoàn thành; không trợ giúp | — | — |

## Can thiệp giả định của moderator

Không có can thiệp trong diễn biến giả định.

## SUS giả định — trả lời trước probe

| Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 | Điểm SUS |
|---|---|---|---|---|---|---|---|---|---|---|
| 4 | 2 | 4 | 2 | 4 | 2 | 4 | 2 | 4 | 2 | 75.0 |

## Câu trả lời mở giả định

| Chủ đề | Lời đáp giả định |
|---|---|
| Độ rõ ràng | Tôi không đoán ngay lời chào là chỗ xem đơn. |
| Khôi phục / xử lý khó khăn | Nếu trạng thái đã hủy còn giữ nguyên sau tải lại thì tôi yên tâm. |
| Tốc độ / nỗ lực | Mất thời gian ở đoạn tìm lịch sử và đối chiếu số tiền. |
| Sự tin tưởng | Nhãn Đã hủy giúp tôi tin thao tác đã xong. |


# Phiên S02 — hồ sơ P02, kịch bản v1

**KẾT QUẢ MÔ PHỎNG PHỤC VỤ BÀI TẬP** — hồ sơ, thời gian, diễn biến và câu trả lời đều do AI tạo cho tình huống giả định. Không có phỏng vấn, người tham gia, đồng ý ghi hình hoặc video thực tế.

| Thông tin | Giá trị |
|---|---|
| Hồ sơ giả định | Nhân viên bán hàng, nhóm tuổi 25–34; non-IT |
| Kinh nghiệm giả định | Mua online khoảng mỗi tuần |
| Môi trường giả định | Giả định: EShop web, Chrome desktop / Ubuntu, viewport 1366×900; không chạy phiên người dùng trong bộ dữ liệu này. |
| Ngày giờ phỏng vấn / liên hệ / đồng ý / video | Không áp dụng — không có phiên thật |
| Thời gian tác vụ giả định | 268 giây (04:28) |
| Kết quả toàn luồng | Hoàn thành không trợ giúp |

## Mục tiêu và kết quả giả định

| Mục | Mục tiêu | Kết quả |
|---|---|---|
| T1 | Xác định trạng thái đơn 30 triệu | Không trợ giúp |
| T2 | Xác định trạng thái đơn 45 triệu | Không trợ giúp |
| T3 | Hủy đúng đơn 28 triệu | Không trợ giúp |
| T4 | Nêu trạng thái cuối và dấu hiệu xác nhận | Không trợ giúp |

## Nhật ký mô phỏng — mốc tương đối, không phải timestamp video

| Mốc | Màn hình | Hành động giả định | Ghi nhận giả định | Lời thoại giả định | Nhóm |
|---|---|---|---|---|---|
| 00:00 | Home | Bắt đầu từ trang chủ | Bắt đầu đồng hồ giả định | — | — |
| 00:32 | Login | Dừng lại khi thấy tiêu đề Đăng Ký | Lưỡng lự giữa đăng nhập và tạo tài khoản | Tôi có tài khoản rồi, sao lại là đăng ký? | U02 |
| 01:08 | Home | Đăng nhập xong, tìm mục Đơn hàng | Quét các liên kết đầu trang | Tôi nghĩ phải có mục Đơn hàng riêng. | U01 |
| 01:55 | Profile | So sánh từng dòng bằng số tiền | Không có tên sản phẩm để nhận diện | Tôi phải đọc kỹ các con số. | U05 |
| 02:20 | Profile | Nói đúng Đã giao cho đơn 30 triệu | T1 hoàn thành | — | — |
| 02:48 | Profile | Nói đúng Đang giao cho đơn 45 triệu | T2 hoàn thành | — | — |
| 03:40 | Profile | Hủy đơn 28 triệu | T3 hoàn thành | — | — |
| 04:28 | Profile | Tự tải lại và thấy Đã hủy | T4 hoàn thành; chủ động kiểm tra lại | — | — |

## Can thiệp giả định của moderator

Không có can thiệp trong diễn biến giả định.

## SUS giả định — trả lời trước probe

| Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 | Điểm SUS |
|---|---|---|---|---|---|---|---|---|---|---|
| 3 | 2 | 4 | 2 | 3 | 3 | 4 | 2 | 3 | 3 | 62.5 |

## Câu trả lời mở giả định

| Chủ đề | Lời đáp giả định |
|---|---|
| Độ rõ ràng | Tiêu đề đăng ký làm tôi nghĩ mình vào nhầm trang. |
| Khôi phục / xử lý khó khăn | Tôi kiểm tra lại trạng thái khi chưa chắc thao tác đã xong. |
| Tốc độ / nỗ lực | Tìm lịch sử mất công hơn bước hủy. |
| Sự tin tưởng | Sau khi tải lại vẫn ghi Đã hủy thì tôi tin hơn. |


# Phiên S03 — hồ sơ P03, kịch bản v1

**KẾT QUẢ MÔ PHỎNG PHỤC VỤ BÀI TẬP** — hồ sơ, thời gian, diễn biến và câu trả lời đều do AI tạo cho tình huống giả định. Không có phỏng vấn, người tham gia, đồng ý ghi hình hoặc video thực tế.

| Thông tin | Giá trị |
|---|---|
| Hồ sơ giả định | Người làm công việc hành chính, nhóm tuổi 45–54; non-IT |
| Kinh nghiệm giả định | Ít mua online; thường dùng điện thoại |
| Môi trường giả định | Giả định: EShop web, Chrome desktop / Ubuntu, viewport 1366×900; không chạy phiên người dùng trong bộ dữ liệu này. |
| Ngày giờ phỏng vấn / liên hệ / đồng ý / video | Không áp dụng — không có phiên thật |
| Thời gian tác vụ giả định | 440 giây (07:20) |
| Kết quả toàn luồng | Hoàn thành có trợ giúp |

## Mục tiêu và kết quả giả định

| Mục | Mục tiêu | Kết quả |
|---|---|---|
| T1 | Xác định trạng thái đơn 30 triệu | Có trợ giúp |
| T2 | Xác định trạng thái đơn 45 triệu | Không trợ giúp |
| T3 | Hủy đúng đơn 28 triệu | Không trợ giúp |
| T4 | Nêu trạng thái cuối và dấu hiệu xác nhận | Không trợ giúp |

## Nhật ký mô phỏng — mốc tương đối, không phải timestamp video

| Mốc | Màn hình | Hành động giả định | Ghi nhận giả định | Lời thoại giả định | Nhóm |
|---|---|---|---|---|---|
| 00:00 | Home | Đọc tình huống | Bắt đầu đồng hồ giả định | — | — |
| 00:45 | Login | Hỏi ý nghĩa Username và tiêu đề Đăng Ký | Chưa hiểu đây là form đăng nhập | Chỗ này cần tên tôi hay địa chỉ email? | U02 |
| 01:35 | Home | Đăng nhập rồi tìm lịch sử ở trang chủ | Chưa thấy mục đơn hàng | Tôi không biết phải mở chỗ nào. | U01 |
| 03:35 | Home | Sau 120 giây bế tắc, nhận gợi ý khu vực tài khoản | Moderator hỗ trợ mức 2; không bấm thay | — | — |
| 04:30 | Profile | Tìm đúng đơn 30 triệu và trả lời Đã giao | T1 hoàn thành có trợ giúp | — | — |
| 05:10 | Profile | Đọc đúng Đang giao cho đơn 45 triệu | T2 hoàn thành | — | — |
| 05:45 | Profile | Cân nhắc trước khi hủy đơn 28 triệu | Lo hủy nhầm và không biết phục hồi | Nếu tôi chọn nhầm thì có quay lại được không? | U04 |
| 06:25 | Profile | Hủy đúng đơn 28 triệu | T3 hoàn thành | — | — |
| 07:20 | Profile | Đọc nhãn Đã hủy rồi kết thúc | T4 hoàn thành | — | — |

## Can thiệp giả định của moderator

| Mốc | Mức | Nội dung |
|---|---|---|
| 03:35 | 2 | Bạn có thể xem khu vực liên quan đến tài khoản của mình. |

## SUS giả định — trả lời trước probe

| Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 | Điểm SUS |
|---|---|---|---|---|---|---|---|---|---|---|
| 3 | 4 | 3 | 4 | 3 | 3 | 3 | 4 | 2 | 4 | 37.5 |

## Câu trả lời mở giả định

| Chủ đề | Lời đáp giả định |
|---|---|
| Độ rõ ràng | Tôi cần từ ngữ rõ hơn ở trang đăng nhập và chỗ mở lịch sử. |
| Khôi phục / xử lý khó khăn | Tôi muốn biết cách xử lý nếu hủy nhầm. |
| Tốc độ / nỗ lực | Nếu không được gợi ý, tôi tìm lịch sử lâu hơn. |
| Sự tin tưởng | Tôi nhìn thấy Đã hủy nhưng vẫn muốn có chỗ xem lại thông báo. |


# Phiên S04 — hồ sơ P04, kịch bản v1

**KẾT QUẢ MÔ PHỎNG PHỤC VỤ BÀI TẬP** — hồ sơ, thời gian, diễn biến và câu trả lời đều do AI tạo cho tình huống giả định. Không có phỏng vấn, người tham gia, đồng ý ghi hình hoặc video thực tế.

| Thông tin | Giá trị |
|---|---|
| Hồ sơ giả định | Nhân viên kỹ thuật, nhóm tuổi 25–34; IT |
| Kinh nghiệm giả định | Mua online thường xuyên; quen website thương mại điện tử |
| Môi trường giả định | Giả định: EShop web, Chrome desktop / Ubuntu, viewport 1366×900; không chạy phiên người dùng trong bộ dữ liệu này. |
| Ngày giờ phỏng vấn / liên hệ / đồng ý / video | Không áp dụng — không có phiên thật |
| Thời gian tác vụ giả định | 160 giây (02:40) |
| Kết quả toàn luồng | Hoàn thành không trợ giúp |

## Mục tiêu và kết quả giả định

| Mục | Mục tiêu | Kết quả |
|---|---|---|
| T1 | Xác định trạng thái đơn 30 triệu | Không trợ giúp |
| T2 | Xác định trạng thái đơn 45 triệu | Không trợ giúp |
| T3 | Hủy đúng đơn 28 triệu | Không trợ giúp |
| T4 | Nêu trạng thái cuối và dấu hiệu xác nhận | Không trợ giúp |

## Nhật ký mô phỏng — mốc tương đối, không phải timestamp video

| Mốc | Màn hình | Hành động giả định | Ghi nhận giả định | Lời thoại giả định | Nhóm |
|---|---|---|---|---|---|
| 00:00 | Home | Bắt đầu tác vụ | Bắt đầu đồng hồ giả định | — | — |
| 00:22 | Login | Đăng nhập bằng dữ liệu demo | Không nhầm tiêu đề trong tình huống này | — | — |
| 00:48 | Profile | Mở liên kết tài khoản và nhìn thấy danh sách | Không cần gợi ý | — | — |
| 01:08 | Profile | Xác định đơn 30 triệu đã giao | T1 hoàn thành | — | — |
| 01:25 | Profile | Xác định đơn 45 triệu đang giao | T2 hoàn thành | — | — |
| 01:40 | Profile | Nhận thấy nút hủy ở đơn đang giao | Đặt câu hỏi về quy tắc trạng thái; không bấm nút đó | Thông thường đang giao thì không hủy trực tiếp được. | U03 |
| 02:05 | Profile | Hủy đúng đơn 28 triệu | T3 hoàn thành | — | — |
| 02:40 | Profile | Xác nhận trạng thái Đã hủy | T4 hoàn thành | — | — |

## Can thiệp giả định của moderator

Không có can thiệp trong diễn biến giả định.

## SUS giả định — trả lời trước probe

| Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 | Điểm SUS |
|---|---|---|---|---|---|---|---|---|---|---|
| 4 | 1 | 5 | 1 | 4 | 2 | 5 | 1 | 4 | 2 | 87.5 |

## Câu trả lời mở giả định

| Chủ đề | Lời đáp giả định |
|---|---|
| Độ rõ ràng | Tôi đoán được liên kết tài khoản dẫn đến lịch sử. |
| Khôi phục / xử lý khó khăn | Nút hủy nên chỉ xuất hiện ở trạng thái cho phép. |
| Tốc độ / nỗ lực | Các bước chính khá ngắn khi đã tìm đúng trang. |
| Sự tin tưởng | Tôi muốn quy tắc nút bấm khớp với trạng thái đơn. |


# Phiên S05 — hồ sơ P05, kịch bản v1

**KẾT QUẢ MÔ PHỎNG PHỤC VỤ BÀI TẬP** — hồ sơ, thời gian, diễn biến và câu trả lời đều do AI tạo cho tình huống giả định. Không có phỏng vấn, người tham gia, đồng ý ghi hình hoặc video thực tế.

| Thông tin | Giá trị |
|---|---|
| Hồ sơ giả định | Người kinh doanh tự do, nhóm tuổi 35–44; non-IT |
| Kinh nghiệm giả định | Mua online 1–2 lần/tháng |
| Môi trường giả định | Giả định: EShop web, Chrome desktop / Ubuntu, viewport 1366×900; không chạy phiên người dùng trong bộ dữ liệu này. |
| Ngày giờ phỏng vấn / liên hệ / đồng ý / video | Không áp dụng — không có phiên thật |
| Thời gian tác vụ giả định | 365 giây (06:05) |
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
| 00:00 | Home | Bắt đầu tác vụ | Bắt đầu đồng hồ giả định | — | — |
| 00:35 | Home | Đăng nhập xong, tìm liên kết đơn hàng | Chưa nhận ra ý nghĩa liên kết lời chào | Tôi tưởng đó chỉ là tên tài khoản. | U01 |
| 01:30 | Profile | Tự tìm được lịch sử | Không nhận trợ giúp | — | — |
| 01:55 | Profile | Đọc nhiều dòng để tìm số tiền đúng | Muốn có tên sản phẩm | Đơn nào cũng chỉ thấy mã và số tiền. | U05 |
| 02:15 | Profile | Nói đúng Đã giao cho đơn 30 triệu | T1 hoàn thành | — | — |
| 02:45 | Profile | Nói đúng Đang giao cho đơn 45 triệu | T2 hoàn thành | — | — |
| 03:40 | Profile | Hủy đúng đơn 28 triệu | T3 hoàn thành | — | — |
| 04:00 | Profile | Vẫn chưa chắc thao tác đã hoàn tất | Không chủ động dùng nhãn trạng thái làm bằng chứng | Tôi muốn biết chắc là đã hủy thật. | U04 |
| 06:00 | Profile | Sau 120 giây bế tắc, nhận gợi ý xem thông tin đơn | Moderator hỗ trợ mức 2 | — | — |
| 06:05 | Profile | Đọc trạng thái Đã hủy và kết thúc | T4 hoàn thành có trợ giúp | — | — |

## Can thiệp giả định của moderator

| Mốc | Mức | Nội dung |
|---|---|---|
| 06:00 | 2 | Bạn có thể xem lại thông tin của đơn vừa thao tác. |

## SUS giả định — trả lời trước probe

| Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 | Điểm SUS |
|---|---|---|---|---|---|---|---|---|---|---|
| 3 | 3 | 3 | 3 | 4 | 3 | 4 | 3 | 3 | 3 | 55.0 |

## Câu trả lời mở giả định

| Chủ đề | Lời đáp giả định |
|---|---|
| Độ rõ ràng | Tôi muốn tên mục lịch sử đơn hàng được viết rõ. |
| Khôi phục / xử lý khó khăn | Tôi muốn có thông tin để kiểm tra lại thao tác vừa làm. |
| Tốc độ / nỗ lực | Đọc các mã và số tiền mất thời gian hơn tôi nghĩ. |
| Sự tin tưởng | Tôi cần nhìn lại trạng thái sau khi hủy mới chắc chắn. |


# Phiên S06 — hồ sơ P06, kịch bản v1

**KẾT QUẢ MÔ PHỎNG PHỤC VỤ BÀI TẬP** — hồ sơ, thời gian, diễn biến và câu trả lời đều do AI tạo cho tình huống giả định. Không có phỏng vấn, người tham gia, đồng ý ghi hình hoặc video thực tế.

| Thông tin | Giá trị |
|---|---|
| Hồ sơ giả định | Người ít dùng dịch vụ trực tuyến, nhóm tuổi 45–54; non-IT |
| Kinh nghiệm giả định | Hiếm mua online; mức quen công nghệ thấp |
| Môi trường giả định | Giả định: EShop web, Chrome desktop / Ubuntu, viewport 1366×900; không chạy phiên người dùng trong bộ dữ liệu này. |
| Ngày giờ phỏng vấn / liên hệ / đồng ý / video | Không áp dụng — không có phiên thật |
| Thời gian tác vụ giả định | 600 giây (10:00) |
| Kết quả toàn luồng | Chưa hoàn thành / hết 600 giây |

## Mục tiêu và kết quả giả định

| Mục | Mục tiêu | Kết quả |
|---|---|---|
| T1 | Xác định trạng thái đơn 30 triệu | Có trợ giúp |
| T2 | Xác định trạng thái đơn 45 triệu | Không trợ giúp |
| T3 | Hủy đúng đơn 28 triệu | Thất bại / hết giờ |
| T4 | Nêu trạng thái cuối và dấu hiệu xác nhận | Chưa thực hiện |

## Nhật ký mô phỏng — mốc tương đối, không phải timestamp video

| Mốc | Màn hình | Hành động giả định | Ghi nhận giả định | Lời thoại giả định | Nhóm |
|---|---|---|---|---|---|
| 00:00 | Home | Bắt đầu tác vụ | Bắt đầu đồng hồ giả định | — | — |
| 01:00 | Login | Phân vân giữa đăng nhập và đăng ký | Đọc lại nhãn của form | Tôi có phải tạo tài khoản trước không? | U02 |
| 02:10 | Home | Đăng nhập xong nhưng chưa tìm được lịch sử | Dừng ở trang chủ | Tôi chỉ thấy sản phẩm. | U01 |
| 04:10 | Home | Sau 120 giây bế tắc, nhận gợi ý khu vực tài khoản | Moderator hỗ trợ mức 2 | — | — |
| 05:20 | Profile | Đọc đúng Đã giao cho đơn 30 triệu | T1 hoàn thành có trợ giúp | — | — |
| 06:05 | Profile | Đọc đúng Đang giao cho đơn 45 triệu | T2 hoàn thành | — | — |
| 07:00 | Profile | Tìm đúng đơn 28 triệu nhưng chưa bấm hủy | Lo tác động không thể đảo ngược | Tôi sợ hủy nhầm thì không lấy lại được. | U04 |
| 09:00 | Profile | Nhắc lại mục tiêu sau 120 giây bế tắc | Moderator hỗ trợ mức 1, không làm thay | — | — |
| 10:00 | Profile | Hết giới hạn tác vụ, dừng mà chưa hủy | T3 thất bại/time-out; T4 chưa thực hiện | — | — |

## Can thiệp giả định của moderator

| Mốc | Mức | Nội dung |
|---|---|---|
| 04:10 | 2 | Bạn có thể xem khu vực liên quan đến tài khoản của mình. |
| 09:00 | 1 | Mục tiêu còn lại là xử lý đơn 28 triệu theo tình huống; bạn có thể dừng nếu chưa muốn tiếp tục. |

## SUS giả định — trả lời trước probe

| Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 | Điểm SUS |
|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 4 | 2 | 4 | 2 | 4 | 3 | 4 | 2 | 4 | 27.5 |

## Câu trả lời mở giả định

| Chủ đề | Lời đáp giả định |
|---|---|
| Độ rõ ràng | Tôi cần lời hướng dẫn dễ hiểu hơn để biết mình ở đâu. |
| Khôi phục / xử lý khó khăn | Tôi muốn có bước xác nhận hoặc giải thích trước khi hủy. |
| Tốc độ / nỗ lực | Tôi mất nhiều thời gian tìm trang và cân nhắc nút hủy. |
| Sự tin tưởng | Tôi chưa đủ tự tin để hoàn tất thao tác trong tình huống này. |


# Phiên S07 — hồ sơ P07, kịch bản v1

**KẾT QUẢ MÔ PHỎNG PHỤC VỤ BÀI TẬP** — hồ sơ, thời gian, diễn biến và câu trả lời đều do AI tạo cho tình huống giả định. Không có phỏng vấn, người tham gia, đồng ý ghi hình hoặc video thực tế.

| Thông tin | Giá trị |
|---|---|
| Hồ sơ giả định | Sinh viên ngành kinh tế, nhóm tuổi 18–24; non-IT |
| Kinh nghiệm giả định | Mua online vài lần/tháng |
| Môi trường giả định | Giả định: EShop web, Chrome desktop / Ubuntu, viewport 1366×900; không chạy phiên người dùng trong bộ dữ liệu này. |
| Ngày giờ phỏng vấn / liên hệ / đồng ý / video | Không áp dụng — không có phiên thật |
| Thời gian tác vụ giả định | 230 giây (03:50) |
| Kết quả toàn luồng | Hoàn thành không trợ giúp |

## Mục tiêu và kết quả giả định

| Mục | Mục tiêu | Kết quả |
|---|---|---|
| T1 | Xác định trạng thái đơn 30 triệu | Không trợ giúp |
| T2 | Xác định trạng thái đơn 45 triệu | Không trợ giúp |
| T3 | Hủy đúng đơn 28 triệu | Không trợ giúp |
| T4 | Nêu trạng thái cuối và dấu hiệu xác nhận | Không trợ giúp |

## Nhật ký mô phỏng — mốc tương đối, không phải timestamp video

| Mốc | Màn hình | Hành động giả định | Ghi nhận giả định | Lời thoại giả định | Nhóm |
|---|---|---|---|---|---|
| 00:00 | Home | Bắt đầu tác vụ | Bắt đầu đồng hồ giả định | — | — |
| 00:30 | Login | Đăng nhập bằng tài khoản demo | Tự thực hiện | — | — |
| 01:00 | Profile | Tự mở khu vực tài khoản | Tìm được lịch sử | — | — |
| 01:25 | Profile | Đối chiếu số tiền vì không có tên sản phẩm | Tìm kiếm bằng mắt | Tôi muốn biết mình đã mua món gì trong từng đơn. | U05 |
| 01:50 | Profile | Nói đúng Đã giao cho đơn 30 triệu | T1 hoàn thành | — | — |
| 02:15 | Profile | Nói đúng Đang giao cho đơn 45 triệu | T2 hoàn thành | — | — |
| 02:35 | Profile | Thấy nút hủy ở đơn đang giao | Không bấm vì mục tiêu chỉ hủy đơn 28 triệu | Nút này có áp dụng cho đơn đang giao không? | U03 |
| 03:10 | Profile | Hủy đúng đơn 28 triệu | T3 hoàn thành | — | — |
| 03:50 | Profile | Kiểm tra Đã hủy và kết thúc | T4 hoàn thành | — | — |

## Can thiệp giả định của moderator

Không có can thiệp trong diễn biến giả định.

## SUS giả định — trả lời trước probe

| Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 | Điểm SUS |
|---|---|---|---|---|---|---|---|---|---|---|
| 4 | 2 | 4 | 2 | 3 | 3 | 4 | 2 | 3 | 2 | 67.5 |

## Câu trả lời mở giả định

| Chủ đề | Lời đáp giả định |
|---|---|
| Độ rõ ràng | Các trạng thái dễ đọc; tôi muốn nhận diện đơn bằng sản phẩm. |
| Khôi phục / xử lý khó khăn | Tôi muốn có giải thích khi một hành động không được phép. |
| Tốc độ / nỗ lực | Đối chiếu đơn bằng số tiền là phần chậm nhất. |
| Sự tin tưởng | Tôi tin nhãn Đã hủy, nhưng nút hủy ở đơn đang giao làm tôi thắc mắc. |


# Báo cáo Task 2 — mô phỏng usability

**KẾT QUẢ MÔ PHỎNG PHỤC VỤ BÀI TẬP** — hồ sơ, thời gian, diễn biến và câu trả lời đều do AI tạo cho tình huống giả định. Không có phỏng vấn, người tham gia, đồng ý ghi hình hoặc video thực tế.

## 1. Thiết kế và giới hạn diễn giải

Một pilot v0 và bảy hồ sơ v1 giả định cùng thực hiện luồng quản lý đơn đã đặt. P00 chỉ dùng minh họa việc chỉnh kịch bản. Các phản ứng, thời gian và câu trả lời là dữ liệu tổng hợp có chủ đích; không phải mẫu khảo sát độc lập. Không tính khoảng tin cậy, không suy rộng kết quả sang người dùng thật.

| Chỉ số mô phỏng — chỉ P01–P07 | Giá trị |
|---|---|
| Hoàn thành không trợ giúp | 4/7 (57.1%) |
| Hoàn thành có trợ giúp | 2/7 (28.6%) |
| Chưa hoàn thành / hết giờ | 1/7 (14.3%) |
| Hoàn thành có hoặc không trợ giúp | 6/7 (85.7%) |
| Thời gian TB tất cả, gồm mốc dừng time-out | 324.00 giây |
| Trung vị; min–max thời gian | 268; 160–600 giây |
| Thời gian TB các hồ sơ hoàn thành | 278.00 giây (n=6) |
| SUS trung bình; trung vị | 58.93; 62.50 |
| SUS độ lệch chuẩn mẫu; min–max | 20.91; 27.5–87.5 |
| Phiên thật / người thật / video thật | 0 / 0 / 0 |

## 2. Kết quả từng hồ sơ

| Hồ sơ | T1 | T2 | T3 | T4 | Giây | SUS |
|---|---|---|---|---|---|---|
| P01 | Không trợ giúp | Không trợ giúp | Không trợ giúp | Không trợ giúp | 205 | 75.0 |
| P02 | Không trợ giúp | Không trợ giúp | Không trợ giúp | Không trợ giúp | 268 | 62.5 |
| P03 | Có trợ giúp | Không trợ giúp | Không trợ giúp | Không trợ giúp | 440 | 37.5 |
| P04 | Không trợ giúp | Không trợ giúp | Không trợ giúp | Không trợ giúp | 160 | 87.5 |
| P05 | Không trợ giúp | Không trợ giúp | Không trợ giúp | Có trợ giúp | 365 | 55.0 |
| P06 | Có trợ giúp | Không trợ giúp | Thất bại / hết giờ | Chưa thực hiện | 600 | 27.5 |
| P07 | Không trợ giúp | Không trợ giúp | Không trợ giúp | Không trợ giúp | 230 | 67.5 |

P06 dừng ở 600 giây: đây là thời gian đã dùng đến khi dừng, không phải thời gian hoàn thành. T4 chưa thực hiện được giữ riêng với T3 thất bại. Không tự thay câu trả lời SUS để đạt mức điểm mong muốn.

## 3. Tính SUS

Câu lẻ: trừ 1 từ đáp án; câu chẵn: lấy 5 trừ đáp án. Cộng 10 phần rồi nhân 2,5. Ví dụ P01 có tổng đóng góp 30, được 75 điểm. Điểm nằm trên thang 0–100, không phải tỷ lệ phần trăm. Công thức tham khảo [John Brooke — SUS](https://digital.ahrq.gov/sites/default/files/docs/survey/systemusabilityscale%2528sus%2529_comp%255B1%255D.pdf). Bản tiếng Việt chưa được xác minh thẩm định. Điểm trong báo cáo chỉ mô tả dữ liệu tổng hợp này.

## 4. Gom nhóm và ưu tiên

Mức 4: chặn hoàn toàn mục tiêu; 3: trở ngại đáng kể/cần hỗ trợ; 2: gây chậm hoặc nhầm; 1: bất tiện nhỏ; 0: quan sát. Các mức dưới đây là ưu tiên đề xuất trong mô phỏng.

| Ưu tiên | Nhóm | Vấn đề | Mức | Hồ sơ /7 | Mốc trong phiên mô phỏng | Phân loại |
|---|---|---|---|---|---|---|
| 1 | U01 | Lối vào lịch sử đơn qua lời chào khó nhận biết | 3 | 5 | P01 00:45; P02 01:08; P03 01:35; P05 00:35; P06 02:10 | Giả thuyết UX |
| 2 | U03 | Nút hủy xuất hiện ở đơn đang giao gây kỳ vọng sai | 3 | 3 | P01 02:05; P04 01:40; P07 02:35 | Liên hệ lỗi đã kiểm thử |
| 3 | U04 | Thiếu tự tin trước/sau thao tác hủy và khả năng phục hồi | 3 | 3 | P03 05:45; P05 04:00; P06 07:00 | Giả thuyết UX |
| 4 | U02 | Tiêu đề Đăng Ký trên form đăng nhập gây nhầm | 2 | 3 | P02 00:32; P03 00:45; P06 01:00 | Liên hệ lỗi đã kiểm thử |
| 5 | U05 | Nhận diện đơn bằng mã và số tiền tốn công | 2 | 4 | P01 01:18; P02 01:55; P05 01:55; P07 01:25 | Giả thuyết UX |

### U01 — Lối vào lịch sử đơn qua lời chào khó nhận biết

Đường vào hiện tại được đọc từ mã UI; tần suất khó tìm chỉ thuộc mô phỏng.

Đề xuất: Thêm liên kết Đơn hàng rõ nghĩa trong điều hướng tài khoản.

### U02 — Tiêu đề Đăng Ký trên form đăng nhập gây nhầm

BUG-001/GUI-001 đã có bằng chứng Task 1; phản ứng hồ sơ ở đây là giả định.

Đề xuất: Đổi tiêu đề đúng chức năng đăng nhập và thống nhất nhãn.

[Issue có sẵn](https://github.com/vinh-code/HW03-Software-Testing/issues/1) · [Ảnh Task 1, không phải ảnh phỏng vấn](../bugs/screenshots/GUI-001.png).

### U03 — Nút hủy xuất hiện ở đơn đang giao gây kỳ vọng sai

BUG-010/GUI-030 xác minh sự xuất hiện của nút. Mô phỏng không tuyên bố đã kiểm thử mới việc hủy đơn đang giao.

Đề xuất: Đồng bộ nút với quy tắc trạng thái; kiểm tra cả UI và API bằng ca thực riêng.

[Issue có sẵn](https://github.com/vinh-code/HW03-Software-Testing/issues/10) · [Ảnh Task 1, không phải ảnh phỏng vấn](../bugs/screenshots/GUI-030.png).

### U04 — Thiếu tự tin trước/sau thao tác hủy và khả năng phục hồi

Lo ngại/lời thoại do mô phỏng; không suy ra yêu cầu FR mới hoặc lỗi đã xác minh.

Đề xuất: Thiết kế phản hồi bền vững về đơn đã hủy, giải thích hậu quả và cân nhắc bước xác nhận theo mức rủi ro.

### U05 — Nhận diện đơn bằng mã và số tiền tốn công

Khả năng UI hiện có đọc từ source; cảm nhận tốn công là giả định và chức năng mới không mặc nhiên bắt buộc theo spec.

Đề xuất: Cân nhắc tóm tắt sản phẩm hoặc chức năng tìm đơn khi mở rộng thiết kế.

## 5. Phân tích bốn chủ đề

- **Clarity:** P02/P03/P06 được xây dựng với nhầm lẫn ở form đăng nhập; nhóm U01 minh họa khó tìm đường vào lịch sử. Tên liên kết và nhãn chức năng là giả thuyết cần thử với người thật.
- **Recovery:** P03/P05/P06 minh họa nhu cầu hiểu hậu quả và kiểm tra lại thao tác hủy. Tình huống không yêu cầu hủy đơn đang giao; U03 chỉ ghi câu hỏi về nút đang hiển thị, không giả định đã thực thi ca API mới.
- **Speed:** khác biệt thời gian được đặt để thể hiện mức quen công nghệ và các điểm do dự. Đây không phải số đo hiệu năng mạng, tốc độ browser hay bằng chứng nhóm tuổi nào chậm hơn.
- **Trust:** nhãn Đã hủy là căn cứ giả định để hoàn tất T4. Có hồ sơ tự kiểm tra lại, có hồ sơ cần gợi ý và có hồ sơ dừng trước khi hủy.

## 6. Đối chiếu mục tiêu

| Mục tiêu | Kết luận trong bộ mô phỏng | Dữ liệu |
|---|---|---|
| O1 | Điều hướng là một giả thuyết ưu tiên kiểm tra | U01; can thiệp T1 tại P03/P06 |
| O2 | Các hồ sơ tiếp cận danh sách đều đọc đúng trạng thái theo kịch bản | T1/T2; U02/U05 |
| O3 | 6/7 hồ sơ đạt cả hủy và xác nhận; 1 hồ sơ chưa hủy khi hết giờ | T3/T4; P06; U03/U04 |
| O4 | Có bảng SUS và bốn nhóm probe cho đủ bảy hồ sơ | sus_responses.csv; sessions/S01–S07 |

## 7. Bằng chứng và công việc tiếp theo

BUG-001 và BUG-010 đã có ảnh thực thi Task 1 và Issue từ trước. Chỉ tham chiếu chúng để làm căn cứ thiết kế mô phỏng; không đổi nguồn thành phỏng vấn Task 2. U01/U04/U05 chưa được xác minh bằng người dùng thật và không được đăng như lỗi mới đã xác nhận. Không có video hay bản đồng ý ghi hình cho P00–P07.

Nếu dùng để quyết định thiết kế sản phẩm, cần thu dữ liệu thực tế riêng và kiểm tra lại các giả thuyết. Với phạm vi hiện tại, bộ mô phỏng đã có đủ kịch bản, pilot, bảy phiên, câu trả lời, tính điểm và phân tích.
