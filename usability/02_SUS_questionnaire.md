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
