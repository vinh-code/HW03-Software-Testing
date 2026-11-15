// Real Android runner. Credentials stay in the user's private cache, never in this repository.
const fs=require('node:fs'),path=require('node:path'),os=require('node:os'),cp=require('node:child_process');
const root=path.resolve(__dirname,'../../..'),sub=path.join(root,'submission');process.chdir(root);
const cache=path.join(os.homedir(),'.cache/hw03-browserstack');
const { _android }=require(path.join(cache,'runtime/node_modules/playwright-core'));
const { Local }=require(path.join(cache,'runtime/node_modules/browserstack-local'));
const credentials=JSON.parse(fs.readFileSync(path.join(cache,'credentials.json'),'utf8'));
const scrub=s=>String(s).split(credentials.access_key).join('[REDACTED]').split(credentials.username).join('[REDACTED]').replace(/wss:\/\/cdp\.browserstack\.com\/playwright\?caps=\S+/g,'[REDACTED endpoint]');
const local=new Local();let device,context,page;
const localId='hw03-23120202';const out=path.join(root,'output/playwright/task3/android');fs.mkdirSync(out,{recursive:true});
const evidence=path.join(sub,'cross_platform/evidence');
(async()=>{
 await new Promise((resolve,reject)=>local.start({key:credentials.access_key,binarypath:path.join(cache,'BrowserStackLocal'),localIdentifier:localId,only:'localhost,3000,0,localhost,5173,0,localhost,5174,0',logfile:path.join(cache,'local.log')},e=>e?reject(e):resolve()));
 console.log('BrowserStack Local connected');
 const caps={osVersion:'13.0',deviceName:'Samsung Galaxy S23',browserName:'chrome',browser:'chrome',realMobile:'true',name:'HW03 23120202 GUI checklist Android',build:'HW03 Task3 real Android', 'browserstack.username':credentials.username,'browserstack.accessKey':credentials.access_key,'browserstack.local':true,'browserstack.localIdentifier':localId,'client.playwrightVersion':'1.62.0','browserstack.playwrightVersion':'1.62.0','browserstack.idleTimeout':180};
 device=await _android.connect('wss://cdp.browserstack.com/playwright?caps='+encodeURIComponent(JSON.stringify(caps)),{timeout:120000});
 console.log('Real Android connected:',device.model());
 context=await device.launchBrowser({hasTouch:true,isMobile:true});for(const port of [5173,5174])await context.grantPermissions(['local-network-access'],{origin:'http://localhost:'+port});page=await context.newPage();
 page.setDefaultTimeout(30000);
 // Map desktop clicks to actual touch taps and dismiss the software keyboard first.
 // This avoids viewport-coordinate drift while the Android IME is visible.
 const locatorPrototype=Object.getPrototypeOf(page.locator('body'));
 locatorPrototype.click=async function(options={}) {
   for(let attempt=0;attempt<3;attempt++){try{await page.evaluate(()=>{if(document.activeElement instanceof HTMLElement)document.activeElement.blur();});break;}catch(e){if(attempt===2||!e.message.includes('Execution context was destroyed'))throw e;await page.waitForTimeout(500);}}
   await page.waitForTimeout(500);
   await this.scrollIntoViewIfNeeded();
   const point=await this.evaluate(e=>{const r=e.getBoundingClientRect(),x=r.x+r.width/2,y=r.y+r.height/2,hit=document.elementFromPoint(x,y);return {x:x-visualViewport.offsetLeft,y:y-visualViewport.offsetTop,clear:hit===e||e.contains(hit)};});
   if(!point.clear)throw new Error('Touch target is obstructed in the DOM');
   return page.touchscreen.tap(point.x,point.y);
 };

 await page.goto('http://localhost:5173/login',{timeout:60000});await page.locator('form input').first().waitFor();
 const ua=await page.evaluate(()=>navigator.userAgent);const version=ua.match(/Chrome\/([\d.]+)/)?.[1]||'unknown';
 let session={};try{const details=await page.evaluate(()=>{},'browserstack_executor: '+JSON.stringify({action:'getSessionDetails'}));session=typeof details==='string'?JSON.parse(details):details;}catch{}
 const osVersion=String(session.os_version||session.osVersion||'13.0 (requested capability)');
 const env={os:'Android '+osVersion,device:device.model(),vendor:'Samsung',execution:'BrowserStack real Android; Playwright Android transport, no emulation',student:JSON.parse(fs.readFileSync(path.join(sub,'task1/student.json')))};

 const smoke={ua,version,os:env.os,model:device.model(),url:page.url(),viewport:await page.evaluate(()=>({width:innerWidth,height:innerHeight,dpr:devicePixelRatio})),session:{hashed_id:session.hashed_id,name:session.name,browser_url:session.browser_url,device:session.device,os:session.os,os_version:session.os_version,browser_version:session.browser_version},verified_at_utc:new Date().toISOString()};
 fs.writeFileSync(path.join(out,'session.json'),JSON.stringify(smoke,null,2));console.log('Android localhost verified:',JSON.stringify(smoke));
 if(process.argv.includes('--smoke-only')){
  await page.locator('form input').nth(1).fill('DemoOnly123!');await page.locator('form button').click();
  await page.locator('form input').nth(0).fill('unknown@example.test');await page.locator('form input').nth(1).fill('');await page.locator('form button').click();
  console.log('Touch validation smoke:',await page.locator('form input').nth(1).evaluate(e=>e.validity.valid));
  await page.evaluate(m=>{document.activeElement.blur();const b=document.createElement('aside');b.textContent=m;Object.assign(b.style,{position:'fixed',bottom:'0',left:'0',right:'0',background:'#10243a',color:'white',padding:'8px',font:'12px/1.4 sans-serif',zIndex:'2147483647',whiteSpace:'pre-wrap',overflowWrap:'anywhere'});document.body.append(b);},'Phạm Quang Vinh • 23120202\n23120202@student.hcmus.edu.vn\nAndroid 13 / Samsung Galaxy S23 / Chrome '+version+'\n'+page.url());
  await page.waitForTimeout(1000);await page.screenshot({path:path.join(out,'smoke.png'),fullPage:false});return;
 }
 cp.execFileSync('python3',['submission/cross_platform/scripts/seed_fixture.py']);
 const fixture=JSON.parse(fs.readFileSync(path.join(evidence,'fixture.json')));const runs={};let results=[];
 const AsyncFunction=Object.getPrototypeOf(async function(){}).constructor;
 if(process.argv.includes('--profile-smoke')){
  await page.locator('form input').nth(0).fill('task3-main@example.test');await page.locator('form input').nth(1).fill('GuiTest123!');await page.locator('form button').click();await page.waitForURL('http://localhost:5173/');await page.goto('http://localhost:5173/profile');await page.locator('tbody tr').first().waitFor();
  const button=page.locator('tbody tr').filter({has:page.getByRole('cell',{name:'#'+fixture.orders.pending,exact:true})}).getByRole('button');
  await button.evaluate(e=>e.scrollIntoView({block:'center',inline:'center'}));
  console.log('Profile geometry',await button.evaluate(e=>({rect:e.getBoundingClientRect().toJSON(),innerWidth,innerHeight,scrollX,scrollY,vv:{width:visualViewport.width,height:visualViewport.height,x:visualViewport.offsetLeft,y:visualViewport.offsetTop,scale:visualViewport.scale}})));
  try{await device.screenshot({path:path.join(out,'device-smoke.png')});console.log('Device screenshot captured');}catch(e){console.log('Device capture unavailable',scrub(e.message));}
  await page.screenshot({path:path.join(out,'clip-smoke.png'),clip:{x:0,y:0,width:360,height:649}});
  let captureCommon=fs.readFileSync(path.join(__dirname,'common.js'),'utf8').replace('await page.setViewportSize({width:1366,height:900});','').replace('page.context().browser().version()','actualBrowserVersion').replace(/const screenshotWithMetadata=async[\s\S]*?(?=const check=)/,fs.readFileSync(path.join(__dirname,'android_screenshot.js'),'utf8'));
  await new AsyncFunction('page','fixture','environment','platformKey','actualBrowserVersion','androidDevice',captureCommon+"\nawait screenshotWithMetadata('output/playwright/task3/android/metadata-smoke.png','GUI-030');")(page,fixture,env,'android',version,device);
  await button.click();await page.getByRole('cell',{name:'#'+fixture.orders.pending,exact:true}).locator('..').getByText('Đã hủy',{exact:true}).waitFor();console.log('Real touch cancel succeeded');return;
 }

 for(const stage of ['login','profile','admin']){
  if(stage==='admin')cp.execFileSync('python3',['-c',"import sqlite3,json; f=json.load(open('submission/cross_platform/evidence/fixture.json')); c=sqlite3.connect('sut/backend/database.sqlite'); [c.execute('update orders set status=? where id=?',(s,f['orders'][s])) for s in ('pending','confirmed')]; c.commit()"]);
  let common=fs.readFileSync(path.join(__dirname,'common.js'),'utf8').replace('await page.setViewportSize({width:1366,height:900});','').replace('page.context().browser().version()','actualBrowserVersion');
  common=common.replace("results.push({id,status:","console.log('Android check',id,ok?'Passed':'Failed');results.push({id,status:");
  common=common.replace(/const screenshotWithMetadata=async[\s\S]*?(?=const check=)/,fs.readFileSync(path.join(__dirname,'android_screenshot.js'),'utf8'));
  let body=fs.readFileSync(path.join(sub,'task1/scripts',stage+'.body.js'),'utf8').replaceAll('task1-','task3-').replaceAll("name:'Task 1 Tester'","name:'Phạm Quang Vinh — 23120202'");
  // Android tap completes before SPA navigation; wait for the destination before judging it.
  body=body.replace("await page.getByRole('link',{name:'Quên mật khẩu?'}).click();", "await page.getByRole('link',{name:'Quên mật khẩu?'}).click();await page.waitForURL(web+'/forgot-password');").replace("await page.getByRole('link',{name:'Đăng ký ngay'}).click();", "await page.getByRole('link',{name:'Đăng ký ngay'}).click();await page.waitForURL(web+'/register');").replace("await page.getByRole('link',{name:'EShop',exact:true}).click();", "await page.getByRole('link',{name:'EShop',exact:true}).click();await page.waitForURL(web+'/');");
  // Keep the physical phone's native viewport; do not turn it into desktop emulation.
  body=body.replaceAll('await page.setViewportSize({width:360,height:800});','').replaceAll('await page.setViewportSize({width:1366,height:900});','');
  body=body.replace('viewport:innerWidth,scroll:document.documentElement.scrollWidth','viewport:visualViewport.width,layoutViewport:innerWidth,scroll:document.documentElement.scrollWidth');
  if(stage==='profile')body=body.replace("await page.route('**/api/orders/my-orders',async route=>", "let releaseOrders;const loadingGate=new Promise(r=>releaseOrders=r);await page.route('**/api/orders/my-orders',async route=>").replace('await new Promise(r=>setTimeout(r,1800));','await loadingGate;').replace('API trì hoãn 1800ms','API được giữ đến khi đo và chụp ảnh xong').replace("await page.locator('tbody tr').first().waitFor();await page.unroute", "releaseOrders();await page.locator('tbody tr').first().waitFor();await page.unroute");
  if(stage==='login')await page.evaluate(()=>localStorage.clear());
  const run=new AsyncFunction('page','fixture','environment','platformKey','actualBrowserVersion','androidDevice',common+'\n'+body+'\nreturn {results,dialogs,browser:browserVersion,ua:await page.evaluate(()=>navigator.userAgent),locale:await page.evaluate(()=>navigator.language)};');
  runs[stage]=await run(page,fixture,env,'android',version,device);results.push(...runs[stage].results);
  fs.writeFileSync(path.join(out,stage+'.json'),JSON.stringify(runs[stage],null,2));console.log('Android',stage,runs[stage].results.length,'checks');
 }
 results.sort((a,b)=>a.id.localeCompare(b.id));if(results.length!==58||new Set(results.map(r=>r.id)).size!==58)throw new Error('Incomplete checklist');
 const folder=path.join(sub,'cross_platform/screenshots/android');fs.mkdirSync(folder,{recursive:true});for(const r of results)if(r.status==='Failed')fs.copyFileSync(path.join(out,r.id+'.png'),path.join(folder,r.id+'.png'));
 fs.writeFileSync(path.join(evidence,'android_session.json'),JSON.stringify(smoke,null,2));
 fs.writeFileSync(path.join(evidence,'android.json'),JSON.stringify({platform:'android',headed:true,real_mobile:true,environment:env,fixture,session:smoke.session,runs,results},null,2));
 await page.evaluate(()=>{},'browserstack_executor: '+JSON.stringify({action:'setSessionStatus',arguments:{status:'passed',reason:'Checklist execution completed; application failures documented in report'}}));
 console.log('Android completed:',results.filter(r=>r.status==='Passed').length,'Passed,',results.filter(r=>r.status==='Failed').length,'Failed');
})().catch(e=>{console.error(scrub(e.stack||e.message));process.exitCode=1;}).finally(async()=>{if(context)await context.close().catch(()=>{});if(device)await device.close().catch(()=>{});await new Promise(r=>local.stop(()=>r()));});
