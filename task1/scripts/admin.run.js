async (page) => {
const fixture={
  "users": {
    "main": 3,
    "empty": 4,
    "other": 5
  },
  "orders": {
    "pending": 5,
    "confirmed": 6,
    "shipping": 7,
    "delivered": 8,
    "canceled": 9,
    "other": 10
  }
};
const results=[];
const dialogs=[];
page.removeAllListeners('dialog');
page.on('dialog',async d=>{dialogs.push({type:d.type(),message:d.message()});await d.accept();});
await page.setViewportSize({width:1366,height:900});
const web='http://localhost:5173',api='http://localhost:3000/api';
const pause=()=>page.waitForTimeout(250);
const check=async(n,ok,actual)=>{const id=`GUI-${String(n).padStart(3,'0')}`;const screenshot=ok?'':`output/playwright/task1/${id}.png`;if(screenshot)await page.screenshot({path:screenshot,fullPage:true});results.push({id,status:ok?'Passed':'Failed',actual, screenshot:screenshot?`../bugs/screenshots/${id}.png`:'',url:page.url(),time:new Date().toISOString()});};
const login=async(which='main')=>{await page.goto(web+'/login');await page.locator('form input').nth(0).fill(`task1-${which}@example.test`);await page.locator('form input').nth(1).fill('GuiTest123!');await page.locator('form button[type=submit]').click();await page.waitForURL(web+'/');await pause();};
const profile=async()=>{await page.goto(web+'/profile');await page.getByRole('heading',{name:'Lịch sử đơn hàng'}).waitFor();await pause();};
const row=id=>page.locator('tbody tr').filter({has:page.getByRole('cell',{name:`#${id}`,exact:true})});
const rgb=async loc=>loc.evaluate(e=>getComputedStyle(e).backgroundColor);
const blue=x=>{const v=x.match(/\d+/g).map(Number);return v[2]>v[0]&&v[2]>v[1];};
const red=x=>{const v=x.match(/\d+/g).map(Number);return v[0]>v[1]&&v[0]>v[2];};
await page.goto('http://localhost:5174');
await page.evaluate(()=>localStorage.removeItem('adminToken'));await page.reload();
await page.getByPlaceholder('Email',{exact:true}).fill('admin@eshop.com');await page.getByPlaceholder('Password',{exact:true}).fill('Admin123!');await page.getByRole('button',{name:'Login',exact:true}).click();await page.getByText('Đơn hàng',{exact:true}).click();await row(fixture.orders.pending).waitFor();
let texts=[];for (const state of ['pending','confirmed','shipping','delivered','canceled'])texts.push(await row(fixture.orders[state]).locator('td').nth(4).innerText());await check(45,JSON.stringify(texts)===JSON.stringify(['Chờ xác nhận','Đã xác nhận','Đang giao','Đã giao','Đã hủy']),texts.join(' | '));
for(const [id,state,names] of [[46,'pending',['Xác nhận','Hủy']],[47,'confirmed',['Giao hàng','Hủy']],[48,'shipping',['Hoàn thành']]]){const actual=await row(fixture.orders[state]).getByRole('button').allTextContents();await check(id,JSON.stringify(actual)===JSON.stringify(names),state+': '+actual.join(' | '));}
for(const [id,state] of [[49,'delivered'],[50,'canceled']]){const actual=await row(fixture.orders[state]).getByRole('button').allTextContents();await check(id,actual.length===0,state+': '+JSON.stringify(actual));}
let selected=page.getByText('Đơn hàng',{exact:true});let style=await selected.evaluate(e=>({class:e.className,color:getComputedStyle(e).color}));await check(51,style.class.includes('text-blue-400'),JSON.stringify(style));
let colors=await page.getByRole('button',{name:'Hủy',exact:true}).evaluateAll(es=>es.map(e=>getComputedStyle(e).backgroundColor));await check(52,colors.length>0&&colors.every(red),JSON.stringify(colors));
let address=row(fixture.orders.pending).locator('td').nth(3);let rendered=await address.locator('b').count();await check(53,rendered===0&&(await address.innerText()).includes('<b>'),'Thẻ b render: '+rendered+'; text: '+await address.innerText());
await row(fixture.orders.pending).getByRole('button',{name:'Xác nhận',exact:true}).click();await row(fixture.orders.pending).getByText('Đã xác nhận',{exact:true}).waitFor();await login();await profile();let state=await row(fixture.orders.pending).locator('td').nth(3).innerText();await check(54,state==='Đã xác nhận','Admin xác nhận #'+fixture.orders.pending+'; user tải lại thấy '+state);
// Concurrent-state scenario: a stale user page still has cancel button; admin changes order to delivered via API.
const adminResp=await page.request.post(api+'/login',{data:{email:'admin@eshop.com',password:'Admin123!'}});const adminToken=(await adminResp.json()).token;
for(const state of ['shipping','delivered']){const r=await page.request.put(api+`/admin/orders/${fixture.orders.pending}/status`,{headers:{Authorization:`Bearer ${adminToken}`},data:{status:state}});if(!r.ok())throw new Error('Fixture state transition failed '+r.status());}
let start=dialogs.length;await row(fixture.orders.pending).getByRole('button',{name:'Hủy đơn'}).click();await pause();let ds=dialogs.slice(start);await check(55,ds.length>0&&!ds.some(d=>/Cannot cancel|order|Error|Request failed/i.test(d.message)),JSON.stringify(ds)+'; user đang xem trang cũ, admin đã chuyển đơn sang delivered');

return {results,dialogs,browser:page.context().browser().version()};
}