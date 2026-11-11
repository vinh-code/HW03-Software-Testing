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
