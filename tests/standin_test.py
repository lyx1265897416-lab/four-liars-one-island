"""男配角顶替实测（V3.11）：在 Jasper 线开一局（带前情），打一句去找别的男嘉宾的话，看第 2 段是不是她和那位男嘉宾、表情对不对。用法：python3 tests/standin_test.py "<她这一句>" """
import json, sys, time
from pathlib import Path
from urllib import request as U
D = Path(__file__).resolve().parent.parent; K = (D / 'jasper' / 'token.txt').read_text().strip(); API = 'http://127.0.0.1:8907'
op = U.build_opener(U.ProxyHandler({}))
def call(p, b=None):
    q = U.Request(API + p, data=json.dumps(dict(b, k=K)).encode() if b is not None else None, headers={'Content-Type': 'application/json'}, method='POST' if b is not None else 'GET')
    with op.open(q, timeout=60) as r: return json.loads(r.read())
recap = ('节目第二天上午，白沙海滩。她和 Jasper 是搭档；第一晚 Jasper 自称是四个骗子之一，问她还选不选他；她刚赢下夺旗赛，Jasper 认赌服输欠她一个问题。'
         'Ravi 一直在泳池边观察所有人，据说读人很准。')
s = call('/api/session', {'mode': 'auto', 'recap': recap, 'cards': ['K02', 'K03'], 'rounds': 2}); sid = s['sid']; print('session', sid, flush=True)
t0 = time.time(); rid = call('/api/round', {'sid': sid, 'kind': 'free', 'input': sys.argv[1]})['id']
while True:
    r = call(f'/api/round/{rid}?k={K}')
    if r['status'] in ('done', 'error'): break
    time.sleep(2)
print(rid, r['status'], round(time.time() - t0, 1), json.dumps({k: r.get(k) for k in ('location', 'err')}, ensure_ascii=False))
for i, x in enumerate(r.get('segs') or [], 1): print(' seg', i, x.get('status'), x.get('stand_in'), (x.get('url') or '')[-40:], [h.get('why', '')[:60] for h in x.get('hard_check', []) if h.get('bad')])
print(json.dumps(r.get('lines'), ensure_ascii=False)[:600])
