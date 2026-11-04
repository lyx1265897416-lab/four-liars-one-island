"""开播时延实测：按播放页的规则开播（第 1 段好了、第 2 段 eta_left ≤ 15−3−1.5 秒），记发送→开播、第 1 段播完时第 2 段到没到（接缝停多久）。
每轮之间等 40 秒，像真人看完再点（预写能做完）。用法：python3 tests/latency.py wes|jasper [轮数]"""
import json, time, sys
from pathlib import Path
from urllib import request as U
LINE = sys.argv[1]; N = int(sys.argv[2]) if len(sys.argv) > 2 else 3; D = Path(__file__).resolve().parent.parent
K = (D / LINE / 'token.txt').read_text().strip(); API = 'http://127.0.0.1:%d' % {'wes': 8906, 'jasper': 8907}[LINE]
op = U.build_opener(U.ProxyHandler({}))
def call(p, b=None):
    q = U.Request(API + p, data=json.dumps(dict(b, k=K)).encode() if b is not None else None, headers={'Content-Type': 'application/json'}, method='POST' if b is not None else 'GET')
    with op.open(q, timeout=60) as r: return json.loads(r.read())
s = call('/api/session', {'mode': 'auto'}); sid = s['sid']; print(LINE, sid, flush=True); rows = []
for n in range(1, N + 1):
    t0 = time.time(); rid = call('/api/round', {'sid': sid, 'kind': 'option', 'choice': 'A'})['id']; play = None
    while True:
        r = call(f'/api/round/{rid}?k={K}'); sg = r.get('segs') or []
        if r['status'] == 'error' or any(x.get('status') == 'error' for x in sg): break
        if play is None and len(sg) == 2 and sg[0].get('url') and (sg[1].get('url') or (sg[1].get('eta_left') is not None and sg[1]['eta_left'] <= 15 - 3.0 - 1.5)): play = time.time()
        if r['status'] == 'done': break
        time.sleep(0.5)
    if play is None and r['status'] == 'done': play = time.time()
    seg2 = (sg[1]['ready_at'] / 1000 - t0) if len(sg) == 2 and sg[1].get('ready_at') else None
    row = dict(n=n, input=r.get('input'), status=r['status'], mode=r.get('mode'), director=r.get('director'), send_to_play=round(play - t0, 1) if play else None, seg2_ready=round(seg2, 1) if seg2 else None,
               stall=round(max(0, seg2 + 3.0 - (play - t0 + 15)), 1) if (play and seg2) else None)
    rows.append(row); print(json.dumps(row, ensure_ascii=False), flush=True)
    if r['status'] != 'done': break
    time.sleep(40)
(D / 'tests' / f'latency_{sid}.json').write_text(json.dumps(rows, ensure_ascii=False, indent=1))
