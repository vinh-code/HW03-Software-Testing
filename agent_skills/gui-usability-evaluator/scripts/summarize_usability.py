#!/usr/bin/env python3
"""Analyse supplied real or simulated sessions without mixing their provenance."""
import argparse,csv,json,statistics as st
from pathlib import Path

def score(a):
    if a is None:return None
    if len(a)!=10 or any(type(x) is not int or not 1<=x<=5 for x in a):raise ValueError('SUS needs ten integer ratings 1–5, or null')
    return 2.5*sum(x-1 if i%2==0 else 5-x for i,x in enumerate(a))

def summarize(d):
    kind=d.get('data_kind');rows=d.get('sessions',[])
    if kind not in ('real','simulated') or not rows:raise ValueError('Specify provenance and main sessions')
    seen=set();out=[]
    for r in rows:
        if not r.get('id') or r['id'] in seen:raise ValueError('Missing/duplicate session ID')
        if r.get('data_kind')!=kind:raise ValueError('Mixed or missing provenance')
        if kind=='real' and not r.get('interview_datetime'):raise ValueError('Missing interview timestamp')
        seen.add(r['id']);t=r.get('task_time_seconds')
        if type(t) not in (int,float) or not 0<t<float('inf'):raise ValueError('Invalid elapsed time')
        tasks=r.get('tasks',{});allowed={'independent','assisted','failed','not_reached'}
        if not tasks or any(v not in allowed for v in tasks.values()):raise ValueError('Invalid task statuses')
        complete=all(v in ('independent','assisted') for v in tasks.values())
        assisted=bool(r.get('assistance')) or 'assisted' in tasks.values()
        state='incomplete' if not complete else 'assisted' if assisted else 'independent'
        out.append({'id':r['id'],'data_kind':kind,'sus':score(r.get('sus_answers')),'elapsed_seconds':t,'outcome':state})
    if (d.get('pilot') or {}).get('id') in seen:raise ValueError('Pilot appears in main sample')
    values=[x['sus'] for x in out if x['sus'] is not None];complete=[x for x in out if x['outcome']!='incomplete']
    return out,{'data_kind':kind,'main_sessions':len(out),'pilot_excluded':bool(d.get('pilot')),'sus_valid_n':len(values),'sus_missing_n':len(out)-len(values),
        'sus_mean':st.mean(values) if values else None,'sus_sample_sd':st.stdev(values) if len(values)>1 else None,
        'outcomes':{k:sum(x['outcome']==k for x in out) for k in ('independent','assisted','incomplete')},
        'elapsed_all_mean':st.mean(x['elapsed_seconds'] for x in out),
        'completed_elapsed_mean':st.mean(x['elapsed_seconds'] for x in complete) if complete else None,
        'interpretation':'Synthetic example, not observed user satisfaction' if kind=='simulated' else 'Descriptive statistics of supplied observations; provenance is not independently verified'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('input',type=Path);p.add_argument('--output',required=True,type=Path);a=p.parse_args()
    rows,s=summarize(json.loads(a.input.read_text()));a.output.mkdir(parents=True,exist_ok=False)
    (a.output/'summary.json').write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n')
    with (a.output/'scores.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
    print(json.dumps(s,ensure_ascii=False))
if __name__=='__main__':main()
