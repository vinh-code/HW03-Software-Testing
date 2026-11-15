const results=[],dialogs=[];
page.removeAllListeners('dialog');
page.on('dialog',async d=>{dialogs.push({type:d.type(),message:d.message()});await d.accept();});
await page.setViewportSize({width:1366,height:900});
const web='http://localhost:5173',api='http://localhost:3000/api';
const pause=()=>page.waitForTimeout(350);
const browserVersion=page.context().browser().version();
const screenshotWithMetadata=async(path,id)=>{
 const metadata={id,student:environment.student,platform:platformKey,version:browserVersion,os:environment.os,device:environment.device,url:page.url(),utc:new Date().toISOString()};
 await page.evaluate(m=>{
  const box=document.createElement('aside');box.id='hw03-evidence-overlay';box.setAttribute('aria-hidden','true');
  Object.assign(box.style,{position:'relative',width:innerWidth+'px',maxWidth:'100vw',boxSizing:'border-box',padding:'7px 12px',background:'#10243a',color:'#fff',font:'12px/1.4 sans-serif',zIndex:'2147483647',pointerEvents:'none',whiteSpace:'pre-wrap',overflowWrap:'anywhere'});
  box.textContent=`BẰNG CHỨNG KIỂM THỬ • ${m.id}\n${m.student.name} • MSSV ${m.student.student_id} • ${m.student.email}\n${m.platform} ${m.version} • ${m.os} • ${m.device}\n${m.url} • ${m.utc}`;
  document.body.appendChild(box);
 },metadata);
 try{await page.screenshot({path,fullPage:true});}finally{await page.locator('#hw03-evidence-overlay').evaluate(e=>e.remove());}
};
const check=async(n,ok,actual)=>{
 const id=`GUI-${String(n).padStart(3,'0')}`;
 const screenshot=ok?'':`output/playwright/task3/${platformKey}/${id}.png`;
 if(screenshot)await screenshotWithMetadata(screenshot,id);
 results.push({id,status:ok?'Passed':'Failed',actual,screenshot:screenshot?`../screenshots/${platformKey}/${id}.png`:'',url:page.url(),time:new Date().toISOString(),browser:browserVersion});
};
const login=async(which='main')=>{await page.goto(web+'/login');await page.locator('form input').nth(0).fill(`task3-${which}@example.test`);await page.locator('form input').nth(1).fill('GuiTest123!');await page.locator('form button[type=submit]').click();await page.waitForURL(web+'/');await pause();};
const profile=async()=>{await page.goto(web+'/profile');await page.getByRole('heading',{name:'Lịch sử đơn hàng'}).waitFor();await pause();};
const row=id=>page.locator('tbody tr').filter({has:page.getByRole('cell',{name:`#${id}`,exact:true})});
const rgb=async loc=>loc.evaluate(e=>getComputedStyle(e).backgroundColor);
const blue=x=>{const v=x.match(/\d+/g).map(Number);return v[2]>v[0]&&v[2]>v[1];};
const red=x=>{const v=x.match(/\d+/g).map(Number);return v[0]>v[1]&&v[0]>v[2];};
