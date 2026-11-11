#!/usr/bin/env node
// Seed 4 đơn hàng ở 4 trạng thái khác nhau cho tài khoản test@eshop.com
// để participant có dữ liệu "lịch sử đơn hàng" thật khi làm usability test.
//
// Công cụ cũ cho chạy SUT thật, không dùng trong bộ mô phỏng.
// Chỉ dùng trên bản DB thử đã backup riêng; không reset database.js trên DB đang giữ bằng chứng.
// Dùng (backend thử đang chạy ở :3000):
//   node seed_orders.mjs
//
// Kết quả (mới nhất ở trên cùng trong giao diện, vì sắp xếp theo id giảm dần):
//   #A  28.000.000 ₫  pending     (Chờ xác nhận)
//   #B   1.500.000 ₫  confirmed   (Đã xác nhận)
//   #C  45.000.000 ₫  shipping    (Đang giao)
//   #D  30.000.000 ₫  delivered   (Đã giao)
const API = process.env.API || "http://localhost:3000/api";

async function call(method, path, body, token) {
  const res = await fetch(API + path, {
    method,
    headers: {
      "Content-Type": "application/json",
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: body ? JSON.stringify(body) : undefined,
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) throw new Error(`${method} ${path} -> ${res.status} ${JSON.stringify(data)}`);
  return data;
}

async function login(email, passwords) {
  for (const password of passwords) {
    try {
      return (await call("POST", "/login", { email, password })).token;
    } catch (_) { /* thử mật khẩu kế tiếp */ }
  }
  throw new Error(`Không đăng nhập được ${email}`);
}

const userToken = await login("test@eshop.com", ["Test1234!"]);
const adminToken = await login("admin@eshop.com", ["Admin123!", "admin123"]);

// [số tiền, trạng thái đích, đường chuyển trạng thái hợp lệ]
const plan = [
  [30000000, ["confirmed", "shipping", "delivered"]],
  [45000000, ["confirmed", "shipping"]],
  [1500000, ["confirmed"]],
  [28000000, []],
];
const address = "123 Nguyễn Huệ, Quận 1, TP. Hồ Chí Minh";

for (const [amount, path] of plan) {
  const { orderId } = await call("POST", "/checkout", { total_amount: amount, shipping_address: address }, userToken);
  for (const status of path) {
    await call("PUT", `/admin/orders/${orderId}/status`, { status }, adminToken);
  }
  console.log(`Đơn #${orderId}: ${amount.toLocaleString("vi-VN")} ₫ -> ${path.at(-1) ?? "pending"}`);
}
