import json,shutil,html
from pathlib import Path
from collections import Counter
from openpyxl import Workbook
from openpyxl.styles import Font,PatternFill,Alignment
from openpyxl.worksheet.datavalidation import DataValidation
ROOT=Path(__file__).resolve().parents[2]
def load(p):return json.loads((ROOT/p).read_text())
design=load('checklist/task1_design.json');evidence=load('task1/evidence/results.json');results={r['id']:r for r in evidence['results']}
def ids(*ns):return [f'GUI-{n:03}' for n in ns]
# Title, severity, cases, concrete reproduction steps. UX items are explicitly separate from FR violations.
groups=[
('Trang đăng nhập mang tiêu đề Đăng Ký','Minor',ids(1),'Mở /login. Quan sát tiêu đề form.'),
('Login và Profile thiếu h1 mô tả trang','Minor',ids(2,23),'Mở /login rồi /profile sau đăng nhập. Inspect DOM trong main: kiểm tra số h1.'),
('Nhãn email và nút đăng nhập dùng tiếng Anh','Minor',ids(3,4),'Mở /login. Quan sát nhãn Username và nút Sign In.'),
('Email dùng text và không chặn định dạng sai','Moderate',ids(5,10),'Mở /login. Nhập not-an-email và DemoOnly123!, bấm Sign In. Kiểm tra HTML validity và phản hồi.'),
('Mật khẩu đăng nhập hiển thị nguyên văn','Major',ids(6),'Mở /login. Nhập mật khẩu thử DemoOnly123!. Quan sát ký tự hiển thị và type của input.'),
('Thiếu dấu sao ở nhãn các trường bắt buộc','Minor',ids(7,25),'Mở /login rồi /profile với tài khoản fixture. Quan sát email, mật khẩu và Họ Tên; đối chiếu required với nhãn.'),
('Lỗi đăng nhập nằm dưới nút gửi','Moderate',ids(11),'Mở /login. Nhập not-an-email và DemoOnly123!, gửi form. Quan sát vị trí thông báo lỗi so với Sign In.'),
('Tab từ đầu trang nhảy thẳng tới Sign In','Moderate',ids(13),'Mở mới /login và chờ form render. Nhấn Tab lần đầu. Quan sát phần tử focus; kiểm tra tabIndex.'),
('Validation điện thoại từ chối số hợp lệ và nhận số sai','Major',ids(27,28),'Đăng nhập task1-main@example.test / GuiTest123!. Mở /profile. Nhập 0912345678, bấm Cập nhật; tiếp tục thử 123456789. Ghi nội dung alert mỗi lần.'),
('User thấy nút Hủy đơn khi đơn đang giao','Major',ids(30),'Seed fixture, đăng nhập tài khoản task1-main. Mở /profile, tìm đơn trạng thái Đang giao. Quan sát nút Hủy đơn.'),
('UX: đang tải đơn lại báo chưa có đơn','Moderate',ids(36),'Đăng nhập tài khoản có đơn. Trì hoãn GET /api/orders/my-orders 1800ms bằng Playwright route; tải lại /profile và quan sát trong khi chờ. Đây là fault injection có ghi trong script.'),
('UX: API tải đơn lỗi 500 bị hiển thị thành danh sách trống','Moderate',ids(37),'Đăng nhập tài khoản có đơn. Dùng Playwright route trả HTTP 500 cho GET /api/orders/my-orders; tải lại /profile. Không thay dữ liệu DOM; phản hồi mạng lỗi là dữ liệu thử có kiểm soát.'),
('Empty state lịch sử đơn thiếu hình minh họa','Minor',ids(38),'Đăng nhập task1-empty@example.test / GuiTest123!, mở /profile. Quan sát khối lịch sử đơn trống.'),
('Nút đăng xuất mang nhãn Thoát','Minor',ids(39),'Đăng nhập và quan sát nút ở navbar.'),
('Navbar không đổi highlight theo trang hiện tại','Minor',ids(40),'Đăng nhập. Mở /profile rồi bấm EShop về Home. So sánh màu/class của link hồ sơ giữa hai trang.'),
('Giỏ hàng trên navbar không có badge số lượng','Moderate',ids(43),'Đăng nhập, vào Home. Bấm Thêm vào giỏ ở sản phẩm đầu tiên. Quan sát link Giỏ hàng trên navbar.'),
('Admin vẫn có nút chuyển đơn Đã hủy sang Đã giao','Major',ids(50),'Đăng nhập Admin bằng tài khoản demo. Chọn Đơn hàng, tìm đơn fixture Đã hủy. Quan sát nút Đánh dấu Đã giao. Ca này xác minh nút hiện sai, không tuyên bố đã bấm chuyển trạng thái.'),
('Nút Hủy đơn trong Admin có màu xám','Minor',ids(52),'Đăng nhập Admin, chọn Đơn hàng. Quan sát các nút Hủy của pending/confirmed, kiểm tra computed background-color.'),
('Địa chỉ giao hàng trong Admin bị render HTML','Major',ids(53),'Seed địa chỉ đơn fixture thành chuỗi vô hại <b>GUI_ADDRESS</b>. Mở Admin > Đơn hàng. Quan sát chữ đậm và kiểm tra có node b trong ô địa chỉ. Không dùng payload thực thi script.'),
('Lỗi hủy đơn hiển thị chuỗi tiếng Anh từ API','Moderate',ids(55),'User mở /profile khi đơn còn confirmed. Admin chuyển cùng đơn qua shipping rồi delivered bằng API. Không tải lại trang user; bấm Hủy đơn trên dữ liệu cũ. Ghi alert Lỗi: Cannot cancel this order.'),
('UX: nhãn form hồ sơ không liên kết với ô nhập','Moderate',ids(56),'Đăng nhập, mở /profile. Inspect label/control của Họ Tên, Số điện thoại, Địa chỉ. Các control có labels.length=0; thử click nhãn để kiểm tra focus.'),
('UX: lịch sử đơn làm tràn ngang ở viewport 360px','Moderate',ids(57),'Đăng nhập, mở /profile có đơn. Đặt viewport 360x800. So sánh documentElement.scrollWidth với innerWidth và quan sát bảng bị tràn. Đây là viewport desktop, không phải mobile thật.'),
('Tên người dùng trên navbar bị render HTML','Major',ids(58),'Dùng tài khoản fixture, cập nhật name thành <b>GUI_NAME</b> qua API. Tải lại /profile. Quan sát header hiển thị chữ đậm và có node b. Khôi phục tên sau ca thử.'),
]
previous={i['id']:i.get('url','') for i in load('task1/evidence/issues.json')} if (ROOT/'task1/evidence/issues.json').exists() else {}
issues=[];mapping={}
for i,(title,severity,cases,steps) in enumerate(groups,1):
 bid=f'BUG-{i:03}';kind='UX bổ sung' if title.startswith('UX:') else 'Vi phạm đặc tả'
 issue=dict(id=bid,title=title,severity=severity,cases=cases,steps=steps,kind=kind,url=previous.get(bid,''))
 issues.append(issue)
 for cid in cases:mapping[cid]=bid
 lines=[f'# {bid} — {title}', '',f'- Mức độ: **{severity}**',f'- Loại: {kind}',f'- Checklist: {", ".join(cases)}','- Môi trường: Linux x86_64; Chrome headless 156.0.8078.79; 1366×900, trừ ca responsive 360×800.','- SUT: eshop-sut commit 85af3ba; code không sửa trong lượt test.',f'- GitHub Issue: {issue["url"] or "Chưa đăng"}','','## Các bước tái hiện','',steps,'','## Kết quả mong đợi và thực tế','']
 for cid in cases:
  item=next(x for x in design if x['id']==cid);r=results[cid]
  lines += [f'### {cid}',f'- Cơ sở: {item["spec"]}',f'- Mong đợi: {item["expected"]}',f'- Thực tế: {r["actual"]}',f'- URL: {r["url"]}',f'- Thời gian UTC: {r["time"]}','',f'![{cid}](screenshots/{cid}.png)','']
 lines += ['## Giới hạn bằng chứng','','Ảnh chụp trực tiếp bằng Playwright. Kiểm tra DOM, computed style và nội dung native alert nằm trong `../task1/evidence/results.json`. Native alert được Playwright ghi nhận rồi đóng; ảnh sau đó chụp nền trang, không phải ảnh của hộp thoại. Không dựng lại hộp thoại để làm bằng chứng.']
 (ROOT/'bugs'/f'{bid}.md').write_text('\n'.join(lines)+'\n')
(ROOT/'task1/evidence/issues.json').write_text(json.dumps(issues,ensure_ascii=False,indent=2))
counts=Counter(r['status'] for r in results.values());ias=Counter(d['ia'] for d in design)
wb=Workbook();ws=wb.active;ws.title='Checklist'
headers=['ID','IA','Screen','Expected result','Spec / basis','Origin','Why earlier AI draft missed it','Status (Chrome)','Actual / Notes','Bug ID','Screenshot','Executed UTC','Status (Firefox)','Status (Platform 3)']
ws.append(headers)
md=['# Task 1 — GUI checklist đã thực thi','','58 mục; Chrome headless 156.0.8078.79 / Linux. 30 Passed, 28 Failed. Firefox và nền tảng 3 chưa chạy.','','Origin AI-reviewed/AI-added là công việc AI; chưa thay thế human review của sinh viên.','','| ID | IA | Màn hình | Mong đợi / Cơ sở | Kết quả | Thực tế | Bug / ảnh |','|---|---|---|---|---|---|---|']
def esc(s):return s.replace('|',' / ').replace('\n','; ').replace('<','&lt;').replace('>','&gt;')
for d in design:
 r=results[d['id']];bid=mapping.get(d['id'],'');ws.append([d['id'],d['ia'],d['screen'],d['expected'],d['spec'],d['origin'],d['why'],r['status'],r['actual'],bid,r['screenshot'],r['time'],'Not run','Not run'])
 if r['screenshot']:ws.cell(ws.max_row,11).hyperlink=r['screenshot']
 links=f'[{bid}](../bugs/{bid}.md) / [ảnh]({r["screenshot"]})' if bid else ''
 md.append('| '+' | '.join([d['id'],d['ia'],d['screen'],esc(d['expected']+' — '+d['spec']),r['status'],esc(r['actual']),links])+' |')
ws.freeze_panes='D2';ws.auto_filter.ref=ws.dimensions
for col,w in zip('ABCDEFGHIJKLMN',[12,10,18,65,35,30,65,18,90,14,44,28,20,20]):ws.column_dimensions[col].width=w
for row in ws:
 for c in row:c.alignment=Alignment(vertical='top',wrap_text=True)
for c in ws[1]:c.fill=PatternFill('solid',fgColor='17365D');c.font=Font(color='FFFFFF',bold=True)
for row in ws.iter_rows(min_row=2):row[7].fill=PatternFill('solid',fgColor='F8CBAD' if row[7].value=='Failed' else 'C6E0B4')
s=wb.create_sheet('Summary');s.append(['Metric','Value']);
for k,v in [('Designed',58),('Executed',58),('Passed',counts['Passed']),('Failed',counts['Failed']),('Bugs / findings',len(issues)),('Screens',3),('Platform','Chrome headless / Linux'),('Firefox','Not run'),('Platform 3','Not run'),('Human review','Pending'),('GitHub Issues',sum(bool(i['url']) for i in issues))]:s.append([k,v])
for k,v in ias.items():s.append([k,v])
s.column_dimensions['A'].width=28;s.column_dimensions['B'].width=45
rev=wb.create_sheet('AI Review');rev.append(['ID','Origin','Why earlier draft missed it'])
for d in design:
 if d['why']:rev.append([d['id'],d['origin'],d['why']])
for col,w in [('A',15),('B',38),('C',100)]:rev.column_dimensions[col].width=w
for row in rev:
 for c in row:c.alignment=Alignment(wrap_text=True,vertical='top')
wb.save(ROOT/'checklist/GUI_Checklist.xlsx');(ROOT/'checklist/GUI_Checklist.md').write_text('\n'.join(md)+'\n')
for row in ws.iter_rows(min_row=2):
 if row[10].value:
  row[10].value=row[10].value.removeprefix('../')
  row[10].hyperlink=row[10].value
wb.save(ROOT/'GUI_Checklist.xlsx')
# Root Markdown is a pointer: relative evidence links remain correct in the canonical checklist.
(ROOT/'GUI_Checklist.md').write_text('# GUI Checklist\n\nBản chính: [checklist/GUI_Checklist.md](checklist/GUI_Checklist.md). Excel ở đây đồng bộ với [bản chính](checklist/GUI_Checklist.xlsx).\n\n58 mục đã chạy: 30 Passed, 28 Failed.\n')
summary=['# Task 1 — Bug report','','28 mục Failed được gom thành 23 bug/phát hiện; trong đó 4 vấn đề UX bổ sung.','','| Bug | Nội dung | Mức độ | Checklist | GitHub |','|---|---|---|---|---|']
for i in issues:summary.append(f'| [{i["id"]}]({i["id"]}.md) | {i["title"]} | {i["severity"]} | {", ".join(i["cases"])} | {i["url"] or "Chưa đăng"} |')
(ROOT/'bugs/README.md').write_text('\n'.join(summary)+'\n')
print('Generated:',dict(counts),'issues',len(issues),'IA',dict(ias))
