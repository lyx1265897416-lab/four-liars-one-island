"""冒烟测试：在一条线的本机中转上新开 auto 会话，按给定输入逐轮生成，存两段视频。用法：python3 tests/smoke.py wes|jasper"""
import json, time, sys
from pathlib import Path
from urllib import request as U
LINE = sys.argv[1]; D = Path(__file__).resolve().parent.parent; K = (D / LINE / 'token.txt').read_text().strip(); API = 'http://127.0.0.1:%d' % {'wes': 8906, 'jasper': 8907}[LINE]
op = U.build_opener(U.ProxyHandler({}))
def call(p, b=None):
    q = U.Request(API + p, data=json.dumps(dict(b, k=K)).encode() if b is not None else None, headers={'Content-Type': 'application/json'}, method='POST' if b is not None else 'GET')
    with op.open(q, timeout=60) as r: return json.loads(r.read())
STEPS = {'wes': [('option', 'A'), ('free', '回到套房，我直接问他：你是那四个骗子之一吗？')], 'jasper': [('option', 'A')]}[LINE]
s = call('/api/session', {'mode': 'auto'}); sid = s['sid']; print(LINE, sid, flush=True)
out = D / 'tests' / 'runs' / sid; out.mkdir(parents=True, exist_ok=True); rows = []
for n, (kind, v) in enumerate(STEPS, 1):
    b = {'sid': sid, 'kind': kind, 'choice': v} if kind == 'option' else {'sid': sid, 'kind': kind, 'input': v}
    t0 = time.time(); rid = call('/api/round', b)['id']
    while True:
        r = call(f'/api/round/{rid}?k={K}')
        if r['status'] in ('done', 'error'): break
        time.sleep(1)
    row = dict(n=n, rid=rid, input=r['input'], status=r['status'], mode=r.get('mode'), sec=round(time.time() - t0, 1), segs=[(x.get('dur'), x.get('status'), x.get('url'), x.get('err')) for x in r.get('segs', [])], lines=r.get('lines'), next=r.get('next'), err=r.get('err'), location=r.get('location'))
    rows.append(row); print(json.dumps({k: row[k] for k in ('n', 'input', 'status', 'mode', 'sec', 'location', 'err')}, ensure_ascii=False), [x[:2] for x in row['segs']], flush=True)
    if r['status'] != 'done': break
    for i, x in enumerate(r['segs']):
        with op.open(x['url'], timeout=120) as f: (out / f'{n}_{i + 1}.mp4').write_bytes(f.read())
    time.sleep(20)
(out / 'rows.json').write_text(json.dumps(rows, ensure_ascii=False, indent=1)); print('DONE', sid, out)
