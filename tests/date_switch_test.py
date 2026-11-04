"""换搭档约会实测：Wes 线演到夺旗赛后，页面切到 Jasper 线（带前情和已演过的卡，K04 算演过），发“去吧台和 Jasper 约会”，看画面里是不是只有 Jasper 和她。用法：python3 tests/date_switch_test.py <wes 会话 id>"""
import glob, json, sys, time
from pathlib import Path
from urllib import request as U
D = Path(__file__).resolve().parent.parent; K = (D / 'jasper' / 'token.txt').read_text().strip(); API = 'http://127.0.0.1:8907'
op = U.build_opener(U.ProxyHandler({}))
def call(p, b=None):
    q = U.Request(API + p, data=json.dumps(dict(b, k=K)).encode() if b is not None else None, headers={'Content-Type': 'application/json'}, method='POST' if b is not None else 'GET')
    with op.open(q, timeout=60) as r: return json.loads(r.read())
rs = sorted((json.load(open(f)) for f in glob.glob(str(D / 'wes/rounds/*.json'))), key=lambda r: r['at']); rs = [r for r in rs if r.get('sid') == sys.argv[1] and r.get('status') == 'done']
last = rs[-1]; state = (last.get('spec') or {}).get('state') or ''
recap = state + ' Mei 安排了换搭档约会：她现在在吧台和 Jasper 单独约会，了解他这个人；她名义上的搭档还是 Wes，Wes 不在这场戏里。约会之后剧情照节目流程往下走。'
cards = sorted(set((last.get('cards_after') or []) + ['K04']))
s = call('/api/session', {'mode': 'auto', 'recap': recap, 'cards': cards}); sid = s['sid']; print('session', sid, cards, flush=True)
t = '我接受换搭档，去吧台和 Jasper 约会，从他嘴里套出 Wes 的事'
r = call('/api/round', {'sid': sid, 'kind': 'free', 'input': t}); rid = r['id']; t0 = time.time()
while True:
    time.sleep(3); g = call(f'/api/round/{rid}?k={K}')
    if g.get('status') in ('done', 'error'): break
print(json.dumps({'status': g.get('status'), 'sec': round(time.time() - t0, 1), 'location': g.get('location'), 'cards_after': g.get('cards_after'), 'lines': g.get('lines'), 'next': g.get('next')}, ensure_ascii=False, indent=1)[:3000])
