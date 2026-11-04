"""换搭档实测：在 Wes 线开会话时带上 Jasper 线的前情（recap、已演过的卡），发“重新配对：我改选 Wes”，看接不接得上。用法：python3 tests/switch_test.py"""
import json, time
from pathlib import Path
from urllib import request as U
D = Path(__file__).resolve().parent.parent; K = (D / 'wes' / 'token.txt').read_text().strip(); API = 'http://127.0.0.1:8906'
op = U.build_opener(U.ProxyHandler({}))
def call(p, b=None):
    q = U.Request(API + p, data=json.dumps(dict(b, k=K)).encode() if b is not None else None, headers={'Content-Type': 'application/json'}, method='POST' if b is not None else 'GET')
    with op.open(q, timeout=60) as r: return json.loads(r.read())
recap = ('节目第二天夜里。她和 Jasper 做了两天搭档：她赢了夺旗赛、在吧台和 Wes 约会时听 Wes 说 Jasper 手上的茧不像普通人；第一次仪式送走了 Ethan（真富豪）；Sloane 当众挑拨说她早就腻了 Jasper。'
         '现在是夜里篝火露台的重新配对仪式，她当着所有人决定改选 Wes 做搭档，Wes 站在她面前。')
s = call('/api/session', {'mode': 'auto', 'recap': recap, 'cards': ['K02', 'K03', 'K04', 'K05', 'K06', 'K07']}); sid = s['sid']; print('session', sid, flush=True)
t0 = time.time(); rid = call('/api/round', {'sid': sid, 'kind': 'free', 'input': '重新配对：我改选 Wes，再当着 Jasper 的面说理由'})['id']
while True:
    r = call(f'/api/round/{rid}?k={K}')
    if r['status'] in ('done', 'error'): break
    time.sleep(1)
print(json.dumps({k: r.get(k) for k in ('status', 'mode', 'location', 'cards_after', 'err')}, ensure_ascii=False), round(time.time() - t0, 1))
print(json.dumps(r.get('lines'), ensure_ascii=False)); print('state', (r.get('state') or '')[:200]); print('next', json.dumps(r.get('next'), ensure_ascii=False)[:300])
out = D / 'tests' / 'runs' / sid; out.mkdir(parents=True, exist_ok=True)
for i, x in enumerate(r.get('segs') or []):
    if x.get('url'): (out / f'1_{i + 1}.mp4').write_bytes(op.open(x['url'], timeout=120).read())
print('DONE', out)
