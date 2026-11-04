"""Vivix 并发和流式探测：同时交几条短任务，0.5 秒一查状态，记下每条 queued→processing→succeeded 的时刻；HLS 任务记下播放列表什么时候出现、分片怎么增长。
用法：python3 vivix_probe.py <实验名> <model:秒数:格式> [...]   例：python3 vivix_probe.py par vivix-w1-ultrafast:5:mp4 vivix-w1-ultrafast:5:mp4"""
import json, os, sys, time, threading
from pathlib import Path
from urllib import request as U
R = '/Users/vicky/Interactive storyline'; sys.path.insert(0, R)
for _l in open(R + '/.env.vivix', encoding='utf-8'):
    if '=' in _l and _l.split('=', 1)[0].strip() == 'VIVIX_API_KEY': os.environ.setdefault('VIVIX_API_KEY', _l.split('=', 1)[1].strip().strip('"\''))
import vivix_w1 as V
op = U.build_opener(U.ProxyHandler({}))
name, specs = sys.argv[1], sys.argv[2:]
PROMPT = '夜里的海岛别墅泳池边，一个穿浅天蓝亚麻衬衫的年轻男人笑着转身走向镜头，串灯在头顶，泳池泛着青绿色的光。写实电影画面。'
c = V.W1Client(max_retries=0); t0 = time.time(); log = []
def stamp(i, ev, extra=''):
    log.append((round(time.time() - t0, 2), i, ev, extra)); print(f'{time.time() - t0:6.2f}s #{i} {ev} {extra}', flush=True)
def one(i, spec):
    model, dur, fmt = spec.split(':')
    body = c.build(prompt=PROMPT, duration=int(dur), aspect_ratio='9:16', output_format=fmt if fmt != 'mp4' else None, resolve=False); body['model'] = model
    while True:
        try: jid = c.submit_body(body); break
        except V.VivixError as e:
            if e.code == 30006: stamp(i, '30006'); time.sleep(1); continue
            raise
    stamp(i, 'submitted', f'{model} {dur}s {fmt} {jid}')
    last = None; seen_url = False; segs_last = -1
    while True:
        g = c.get(jid); st = g.get('status'); url = g.get('video_url')
        if st != last: stamp(i, st); last = st
        if url and not seen_url: stamp(i, 'url', url[-60:]); seen_url = True
        if url and fmt == 'hls':
            try:
                txt = op.open(url, timeout=10).read().decode('utf-8', 'ignore')
                n = txt.count('#EXTINF'); end = '#EXT-X-ENDLIST' in txt
                if n != segs_last: stamp(i, 'hls', f'{n} 分片 end={end}'); segs_last = n
                if end and st in ('succeeded', 'failed'): break
            except Exception as e: pass
        if st in ('succeeded', 'failed', 'cancelled') and (fmt != 'hls' or not url): break
        if st in ('succeeded', 'failed', 'cancelled') and fmt != 'hls': break
        time.sleep(0.5)
th = [threading.Thread(target=one, args=(i, s)) for i, s in enumerate(specs)]
for t in th: t.start(); time.sleep(0.2)
for t in th: t.join()
Path(R + f'/output/island-liars-live-v1/tests/vivix-probe/{name}.json').write_text(json.dumps(log, ensure_ascii=False, indent=1))
