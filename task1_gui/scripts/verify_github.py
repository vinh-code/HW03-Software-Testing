import json,re,subprocess,urllib.request,concurrent.futures
from pathlib import Path
repo='vinh-code/HW03-Software-Testing';R=Path(__file__).resolve().parents[2]
issues=json.loads(subprocess.check_output(['gh','issue','list','--repo',repo,'--state','all','--limit','100','--json','number,title,url,body'],text=True))
images=set()
for issue in issues:
 assert re.match(r'\[BUG-\d{3}\]',issue['title'])
 urls=re.findall(r'!\[[^\]]*\]\((https://raw.githubusercontent.com/[^)]+)\)',issue['body']);assert urls,issue['number'];images.update(urls)
def verify(url):
 req=urllib.request.Request(url,method='HEAD')
 with urllib.request.urlopen(req,timeout=30) as r:
  assert r.status==200 and r.headers.get_content_type()=='image/png'
  return {'url':url,'status':r.status,'content_type':r.headers.get_content_type()}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:checked=list(pool.map(verify,sorted(images)))
result={'repository':'https://github.com/'+repo,'issue_count':len(issues),'image_count':len(images),'issues':[{'number':i['number'],'url':i['url']} for i in issues],'images':checked}
(R/'task1/evidence/github_verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
print('Issues:',len(issues),'valid screenshot URLs:',len(images))
assert len(issues)==23 and len(images)==28
