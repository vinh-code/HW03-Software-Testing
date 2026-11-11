# GUI evaluation — EShop Login — complete 16-criterion screen

Data kind: **real**. Executed 16/16; complete.

Passed: 6 | Failed: 10 | Blocked: 0 | Not run: 0

| ID | Aspect | Expected / basis | Status | Actual | Evidence path relative to input |
|---|---|---|---|---|---|
| GUI-001 | IA-01 | Tiêu đề trang mô tả đúng chức năng Đăng nhập / FR-21 | Failed | Tiêu đề thực tế: Đăng Ký | screenshots/GUI-001.png |
| GUI-002 | IA-01 | Có đúng một h1 mô tả trang / FR-21 | Failed | Số h1: 0 | screenshots/GUI-002.png |
| GUI-003 | IA-01 | Nhãn trường email bằng tiếng Việt và đúng nội dung / FR-21 | Failed | Nhãn email: Username | screenshots/GUI-003.png |
| GUI-004 | IA-01 | Nút gửi có nhãn Đăng nhập bằng tiếng Việt / FR-21 | Failed | Nhãn nút: Sign In | screenshots/GUI-004.png |
| GUI-005 | IA-02 | Email dùng type=email / FR-02, FR-22 | Failed | type email: text | screenshots/GUI-005.png |
| GUI-006 | IA-02 | Mật khẩu dùng type=password / FR-22 | Failed | type mật khẩu: text; nhập dữ liệu thử DemoOnly123! | screenshots/GUI-006.png |
| GUI-007 | IA-02 | Hai trường bắt buộc có dấu * ở nhãn / FR-22 | Failed | Nhãn: Username / Mật khẩu | screenshots/GUI-007.png |
| GUI-008 | IA-02 | Bỏ trống email bị chặn gửi form / HTML validation / tiêu chí bổ sung | Passed | {"valid":false,"message":"Please fill out this field."} | None |
| GUI-009 | IA-02 | Bỏ trống mật khẩu bị chặn gửi form / HTML validation / tiêu chí bổ sung | Passed | {"valid":false,"message":"Please fill out this field."} | None |
| GUI-010 | IA-02 | Email sai định dạng bị chặn tại form / FR-02 | Failed | {"valid":true,"typeMismatch":false}; form gửi tới API và hiện lỗi đăng nhập | screenshots/GUI-010.png |
| GUI-011 | IA-02 | Lỗi đăng nhập nằm phía trên nút gửi / FR-22 | Failed | error.y=516, button.y=424 | screenshots/GUI-011.png |
| GUI-012 | IA-04 | Đăng nhập sai có thông báo lỗi tiếng Việt / FR-02, FR-21 | Passed | Đăng nhập thất bại. Vui lòng kiểm tra lại. | None |
| GUI-013 | IA-01 | Tab đầu tiên đi vào phần tử tương tác trên cùng, không nhảy tới submit / FR-21 | Failed | {"tag":"BUTTON","text":"Sign In","tabIndex":1} | screenshots/GUI-013.png |
| GUI-014 | IA-03 | Liên kết Quên mật khẩu mở đúng trang / IA-03; yêu cầu điều hướng bổ sung | Passed | http://localhost:5173/forgot-password | None |
| GUI-015 | IA-03 | Liên kết Đăng ký mở đúng trang / IA-03; yêu cầu điều hướng bổ sung | Passed | http://localhost:5173/register | None |
| GUI-016 | IA-02 | Enter tại mật khẩu gửi form đăng nhập hợp lệ / IA-02; hỗ trợ bàn phím bổ sung | Passed | Enter đăng nhập thành công, tới http://localhost:5173/ | None |

Validation checks structure and local files; it does not certify observation truth or specification completeness.
