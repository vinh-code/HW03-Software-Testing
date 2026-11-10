# AI Critique — đã được sinh viên duyệt

AI hỗ trợ thiết kế checklist và chạy kiểm thử nhanh, nhưng bản nháp ban đầu cho thấy số lượng mục không đồng nghĩa với chất lượng. Một số tiêu chí yêu cầu timeline đơn hàng, breadcrumb ở trang hồ sơ hoặc xác nhận hủy đơn dù đặc tả chưa bắt buộc. Nếu giữ nguyên và đánh Failed, báo cáo sẽ nhầm đề xuất cải thiện thành lỗi vi phạm yêu cầu. Nguyên nhân là AI suy rộng từ kinh nghiệm thiết kế giao diện và những màn hình tương tự, thay vì truy vết từng tiêu chí đến yêu cầu cụ thể.

Bản nháp cũng gộp nhiều điều kiện trong một dòng và gắn nhãn Student cho các mục chưa có bằng chứng sinh viên tự bổ sung. Quá trình rà soát đã tách tiêu chí, ghi rõ nguồn AI và phân biệt vấn đề UX với lỗi đặc tả. Khi chạy trình duyệt, một thao tác Tab diễn ra trước khi giao diện render và một selector tìm sai nhãn menu Admin. Những lỗi tự động hóa này được sửa trước khi chốt kết quả; timeout không được tính là lỗi ứng dụng.

Bài học là phải kiểm tra cả tiêu chí lẫn cách thu bằng chứng. Kết quả cần gắn với dữ liệu thử, môi trường, thời điểm và bước tái hiện. Ảnh nền trang không thay thế nội dung native alert; vì vậy thông báo được lưu riêng trong JSON. Cuối cùng, AI không thể xác nhận thay việc sinh viên đã duyệt hoặc tuyển người thật. GitHub Issues đã được đăng bằng gh theo yêu cầu. Những phần chưa làm phải được ghi rõ, thay vì làm báo cáo trông hoàn chỉnh.
