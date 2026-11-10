#!/usr/bin/env python3
import json,collections
from pathlib import Path
R=Path(__file__).resolve().parents[2];P=R/'cross_platform'
read=lambda p:json.loads(p.read_text())
design=read(R/'checklist/task1_design.json');issues=read(R/'task1/evidence/issues.json')
bugs={cid:i for i in issues for cid in i['cases']}
runs={b:read(P/f'evidence/{b}.json') for b in ('chrome','firefox') if (P/f'evidence/{b}.json').exists()}
by={b:{r['id']:r for r in d['results']} for b,d in runs.items()}
md=['# Task 3 — Cross-browser / Cross-platform','','Sinh viên: **Phạm Quang Vinh — 23120202 — 23120202@student.hcmus.edu.vn**.','','**Trạng thái: 2/3 nền tảng; chưa hoàn thành Task 3.** Đã thực thi toàn bộ 58 mục trên Chrome và Firefox. Chưa có Safari, Android Chrome hoặc Expo Go trên điện thoại thật.','','## Môi trường và kết quả','','| Trình duyệt | Máy / OS | Chạy | Passed | Failed | Bằng chứng |','|---|---|---|---|---|---|']
for b,d in runs.items():
 c=collections.Counter(r['status'] for r in d['results']);v=d['runs']['login']['browser']
 md.append(f'| {b} {v} | MSI Cyborg 15 A12VF / Ubuntu 24.04.5 LTS | 58 | {c["Passed"]} | {c["Failed"]} | [JSON](evidence/{b}.json), [ảnh](screenshots/{b}/) |')
md+=['| Nền tảng 3 | Chưa có môi trường phù hợp | 0 | — | — | Not run |','','Chrome là Google Chrome cài trên máy. Firefox 159.0 là bản Firefox do Playwright tải về (build v1573), chạy Gecko thật có cửa sổ; không phải đổi user-agent Chrome. Firefox hệ thống 156.0.1 không được dùng trong lượt tự động này. Cả hai chạy trên laptop thật, không phát hiện hypervisor (`systemd-detect-virt: none`). Không dùng BrowserStack/LambdaTest trong lượt này vì chưa được cung cấp tài khoản trial.','','## Quy trình và tính xác thực của ảnh','','- Dùng nguyên 58 tiêu chí Task 1 đã duyệt; 3 màn hình chính Login, Profile/Lịch sử đơn, Admin Orders, Home/navbar hỗ trợ thao tác.','- Mỗi trình duyệt có bộ fixture task3-* riêng theo lượt; không thay kết quả hay tài khoản fixture của Task 1. Các đơn gốc của người dùng được giữ lại.','- Viewport 1366×900; ca responsive 360×800 là kiểm tra bố cục desktop, không tính là thiết bị mobile. Locale en-US.','- Mỗi ảnh Failed được chụp trực tiếp bởi Playwright, kèm nhãn bằng chứng chứa email, MSSV, họ tên, browser/version, OS, model máy, URL localhost và UTC. Nhãn được thêm vào cuối tài liệu sau khi đo kết quả, rồi gỡ ngay; không vẽ lại giao diện hoặc chỉnh ảnh hậu kỳ.','- Form Hồ sơ của tài khoản thử chứa Họ Tên = Phạm Quang Vinh — 23120202. Các màn không có trường họ tên dùng nhãn bằng chứng.','- GUI-036/037 chủ động trì hoãn API/trả HTTP 500; native alert được ghi text vào JSON trước khi đóng. Ảnh alert là nền trang sau khi đóng, không phải ảnh hộp thoại.','- 56 ảnh Failed cho hai trình duyệt. Kết quả giữ nguyên 30 Passed/28 Failed mỗi trình duyệt.','','## Đối chiếu 58 mục','','| ID | IA | Chrome | Firefox | Nền tảng 3 | Bug / bằng chứng |','|---|---|---|---|---|---|']
comparison=[]
for item in design:
 cid=item['id'];states={b:by[b][cid]['status'] for b in runs};links=[]
 if cid in bugs:links.append(f'[{bugs[cid]["id"]}]({bugs[cid]["url"]})')
 for b in runs:
  if by[b][cid]['screenshot']:links.append(f'[ảnh {b}](screenshots/{b}/{cid}.png)')
 md.append('| '+' | '.join([cid,item['ia'],states.get('chrome','Not run'),states.get('firefox','Not run'),'Not run',' / '.join(links)])+' |')
 comparison.append({'id':cid,'statuses':states,'different_status':len(set(states.values()))>1})
md+=['','## Khác biệt quan sát được','','Không có khác biệt Passed/Failed trong 58 mục giữa hai môi trường đã chạy. Điều này không chứng minh ứng dụng tương thích mọi nền tảng. Browser validation message và kích thước render có thể khác; số đo thực tế lưu trong JSON.','','| Mục | Chrome | Firefox | Ý nghĩa |','|---|---|---|---|']
for cid in ('GUI-011','GUI-013','GUI-057'):
 vals=[by[b][cid]['actual'].replace('|',' / ') for b in ('chrome','firefox')]
 md.append(f'| {cid} | {vals[0]} | {vals[1]} | Cùng kết luận Failed |')
md+=['','Các mục Failed tiếp tục ánh xạ vào 23 Issues hiện có; không tạo Issues trùng cho cùng lỗi.','','## Phần còn thiếu','','Cần chạy cùng checklist trên Safari thật (ví dụ qua BrowserStack/LambdaTest hoặc máy Mac), Chrome trên Android thật, hoặc Expo Go trên điện thoại thật. Playwright WebKit trên Linux và Chrome giả lập kích thước điện thoại không được tính thành Safari/Android. Khi có môi trường thứ ba, ghi rõ các mục tương ứng và bằng chứng thực tế trước khi cập nhật trạng thái hoàn tất.','','## Chạy lại','','Từ HW03 root, với các server :3000, :5173, :5174 đang chạy:','','```bash','python3 submission/cross_platform/scripts/run_platform.py chrome','python3 submission/cross_platform/scripts/run_platform.py firefox','python3 submission/cross_platform/scripts/build_report.py','python3 submission/checklist/build_checklist.py','```','','Script chỉ dùng task3-* fixtures; backup trước khi chạy. Không khởi động lại backend nếu chưa backup vì database.js reset dữ liệu khi import. Không chạy song song hai trình duyệt do fixture DB dùng chung.','','Nguồn checklist và bằng chứng Task 1 được giữ nguyên. Xác nhận duyệt trước đó là cho Task 1; báo cáo này ghi nhận các lượt chạy Task 3 mới.']
(P/'README.md').write_text('\n'.join(md)+'\n')
(P/'evidence/comparison.json').write_text(json.dumps({'completed_platforms':list(runs),'required_platform_count':3,'status':'incomplete','comparisons':comparison},ensure_ascii=False,indent=2)+'\n')
print('Task 3:',len(runs),'/ 3 platforms; differences:',sum(x['different_status'] for x in comparison))
