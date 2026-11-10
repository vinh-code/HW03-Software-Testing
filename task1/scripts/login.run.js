async (page) => {
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
await page.goto(web+'/login');
let txt=await page.locator('main h2').innerText();await check(1,/đăng nhập/i.test(txt),'Tiêu đề thực tế: '+txt);
let n=await page.locator('main h1').count();await check(2,n===1,`Số h1: ${n}`);
let labels=await page.locator('form label').allTextContents();await check(3,/email|thư điện tử/i.test(labels[0]),'Nhãn email: '+labels[0]);
txt=await page.locator('form button').innerText();await check(4,txt==='Đăng nhập','Nhãn nút: '+txt);
let types=await page.locator('form input').evaluateAll(es=>es.map(e=>e.type));await check(5,types[0]==='email','type email: '+types[0]);
await page.locator('form input').nth(1).fill('DemoOnly123!');await check(6,types[1]==='password','type mật khẩu: '+types[1]+'; nhập dữ liệu thử DemoOnly123!');
await check(7,labels.every(x=>x.includes('*')),'Nhãn: '+labels.join(' / '));
await page.locator('form button').click();let valid=await page.locator('form input').nth(0).evaluate(e=>({valid:e.validity.valid,message:e.validationMessage}));await check(8,!valid.valid,JSON.stringify(valid));
await page.locator('form input').nth(0).fill('unknown@example.test');await page.locator('form input').nth(1).fill('');await page.locator('form button').click();valid=await page.locator('form input').nth(1).evaluate(e=>({valid:e.validity.valid,message:e.validationMessage}));await check(9,!valid.valid,JSON.stringify(valid));
await page.locator('form input').nth(0).fill('not-an-email');await page.locator('form input').nth(1).fill('DemoOnly123!');
valid=await page.locator('form input').nth(0).evaluate(e=>({valid:e.validity.valid,typeMismatch:e.validity.typeMismatch}));await page.locator('form button').click();await page.getByText('Đăng nhập thất bại. Vui lòng kiểm tra lại.').waitFor();await check(10,!valid.valid,JSON.stringify(valid)+'; form gửi tới API và hiện lỗi đăng nhập');
let err=page.getByText('Đăng nhập thất bại. Vui lòng kiểm tra lại.');let er=await err.boundingBox(),btn=await page.locator('form button').boundingBox();await check(11,er.y+er.height<=btn.y,`error.y=${er.y}, button.y=${btn.y}`);
await check(12,await err.isVisible(),await err.innerText());
await page.goto(web+'/login');await page.locator('form button').waitFor();await pause();await page.keyboard.press('Tab');let focused=await page.evaluate(()=>({tag:document.activeElement.tagName,text:document.activeElement.textContent,tabIndex:document.activeElement.tabIndex}));await check(13,focused.tag==='A'&&focused.text==='EShop',JSON.stringify(focused));
await page.getByRole('link',{name:'Quên mật khẩu?'}).click();await check(14,page.url().endsWith('/forgot-password'),page.url());
await page.goto(web+'/login');await page.getByRole('link',{name:'Đăng ký ngay'}).click();await check(15,page.url().endsWith('/register'),page.url());
await page.goto(web+'/login');await page.locator('form input').nth(0).fill('task1-main@example.test');await page.locator('form input').nth(1).fill('GuiTest123!');await page.locator('form input').nth(1).press('Enter');await page.waitForURL(web+'/');await check(16,page.url()===web+'/', 'Enter đăng nhập thành công, tới '+page.url());

return {results,dialogs,browser:page.context().browser().version(),ua:await page.evaluate(()=>navigator.userAgent)};
}