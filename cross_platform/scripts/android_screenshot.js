// Native Android viewport capture. Full-page capture is unreliable on this remote transport.
const screenshotWithMetadata=async(path,id)=>{
 const n=Number(id.slice(4));const oldScroll=await page.evaluate(()=>({x:scrollX,y:scrollY,padding:document.body.style.paddingTop}));
 await page.evaluate(()=>{if(document.activeElement instanceof HTMLElement)document.activeElement.blur();});await page.waitForTimeout(500);
 await page.evaluate(({n,orders})=>{
  const q=s=>document.querySelector(s);const r=state=>[...document.querySelectorAll('tbody tr')].find(e=>e.children[0]?.textContent==='#'+orders[state]);
  let target=q('main h2');
  if([3,5,7].includes(n))target=q('form label');
  if([4,10,11,27,28].includes(n))target=q('form button');
  if(n===6)target=document.querySelectorAll('form input')[1];
  if(n===13)target=q('form button');
  if(n===39)target=q('header button');
  if([40,58].includes(n))target=q('header a[href="/profile"]');
  if(n===43)target=q('header a[href="/cart"]');
  if([25,56].includes(n))target=document.querySelectorAll('form label')[1];
  if(n===30)target=r('shipping')?.querySelector('button');
  if([36,37,38].includes(n))target=[...document.querySelectorAll('main p')].find(e=>e.textContent.includes('Bạn chưa có đơn hàng nào'))||q('main');
  if(n===50)target=r('canceled')?.querySelector('button');
  if(n===52)target=[...document.querySelectorAll('button')].find(e=>e.textContent==='Hủy');
  if(n===53)target=r('pending')?.children[3];
  if(n===55)target=r('pending')?.querySelector('button');
  if(n===57)target=q('table');
  target?.scrollIntoView({block:'center',inline:'center'});
 },{n,orders:fixture.orders});
 const metadata={id,student:environment.student,version:browserVersion,os:environment.os,device:environment.device,url:page.url(),utc:new Date().toISOString()};
 await page.evaluate(m=>{
  const box=document.createElement('aside');box.id='hw03-evidence-overlay';box.setAttribute('aria-hidden','true');
  Object.assign(box.style,{position:'fixed',left:visualViewport.offsetLeft+'px',width:visualViewport.width+'px',boxSizing:'border-box',padding:'7px 8px',background:'#10243a',color:'#fff',font:'11px/1.35 sans-serif',zIndex:'2147483647',pointerEvents:'none',whiteSpace:'pre-wrap',overflowWrap:'anywhere'});
  box.textContent=`${m.id} • ${m.student.name} • ${m.student.student_id}\n${m.student.email}\nChrome ${m.version} • ${m.os} • Samsung ${m.device}\n${m.url}\n${m.utc}`;document.body.append(box);document.body.style.paddingTop=(parseFloat(getComputedStyle(document.body).paddingTop)+box.offsetHeight)+'px';box.style.top=visualViewport.offsetTop+'px';
 },metadata);
 try{await page.screenshot({path,clip:{x:0,y:0,...await page.evaluate(()=>({width:visualViewport.width,height:visualViewport.height}))}});}finally{await page.evaluate(p=>{document.getElementById('hw03-evidence-overlay')?.remove();document.body.style.paddingTop=p.padding;scrollTo(p.x,p.y);},oldScroll);}
};
