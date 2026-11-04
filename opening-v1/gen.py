# -*- coding: utf-8 -*-
"""usage: gen.py costume [id..] | frames [key..] | native [key..]
照 meet-me-third opening-v1/gen.py：waku gen run，jobs/ 记任务可续跑，inputs/ 缓存上传地址。"""
import json, subprocess, sys, time, hashlib, os
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
V = Path(__file__).resolve().parent
sys.path.insert(0, str(V))
sys.path.insert(0, '/Users/vicky/Interactive storyline/projects/meet-me-again-deepspace-20261013/interactive-video-v1/tools')
from cast import CAST, LIB, costume_prompt
os.environ['PATH'] = '/Users/vicky/.local/bin:/Users/vicky/.waku/bin:/opt/homebrew/bin:' + os.environ['PATH']


def cli(a, t=600):
    p = subprocess.run(['waku'] + a, capture_output=True, text=True, timeout=t)
    try: return json.loads(p.stdout[p.stdout.find('{'):])
    except Exception: return dict(_err=(p.stdout + p.stderr)[-200:])


def upload(path):
    sha = hashlib.sha256(Path(path).read_bytes()).hexdigest(); rec = V / 'inputs' / (sha + '.json')
    if rec.exists(): return json.loads(rec.read_text())['url']
    for k in range(4):
        d = cli(['persist', str(path)], 400)
        if d.get('url'): rec.write_text(json.dumps(dict(url=d['url']))); return d['url']
        time.sleep(4)
    import mcp_upload
    for k in range(5):
        try: u = mcp_upload.upload(str(path)); rec.write_text(json.dumps(dict(url=u))); return u
        except Exception:
            if k == 4: raise
            mcp_upload._mcp = None; time.sleep(5 * (k + 1))


def run(name, model, cap, params, out):
    rec = V / 'jobs' / f'{name}.json'
    if out.exists() and out.stat().st_size > 30000: return name, 'cached'
    r = json.loads(rec.read_text()) if rec.exists() else None
    if not r or not r.get('job_id') and not r.get('asset_url'):
        d = cli(['gen', 'run', model, '--capability', cap, '--params', json.dumps(params, ensure_ascii=False)])
        r = dict(model=model, params=params, job_id=d.get('job_id'), asset_url=d.get('asset_url')); rec.write_text(json.dumps(r, ensure_ascii=False))
        if not r['job_id'] and not r['asset_url']: rec.unlink(); return name, 'SUBMIT FAIL ' + str(d)[:200]
    url = r.get('asset_url')
    for _ in range(200):
        if url: break
        x = cli(['gen', 'result', r['job_id'], '--refresh'], 120)
        url = x.get('asset_url') or x.get('result_url')
        if x.get('status') in ('failed', 'cancelled'): rec.unlink(); return name, 'FAILED ' + str(x.get('error'))[:200]
        if not url: time.sleep(10)
    if not url: return name, 'pending'
    r['asset_url'] = url; rec.write_text(json.dumps(r, ensure_ascii=False))
    tmp = out.with_suffix('.part' + out.suffix)
    for _ in range(8):
        if subprocess.run(['curl', '-fsSL', '-C', '-', '--retry', '3', '--max-time', '900', url, '-o', str(tmp)]).returncode == 0: break
        time.sleep(5)
    tmp.rename(out); return name, 'ok'


def image(name, refs, prompt, folder='frames'):
    if not refs:  # 空镜没有参考图，走文生图
        return run(name, 'openai/gpt-image-2/text-to-image', 'multimodal.generate.image', dict(prompt=prompt, aspect_ratio='9:16'), V / folder / f'{name}.png')
    return run(name, 'openai/gpt-image-2/edit', 'multimodal.generate.image', dict(images=[upload(p) for p in refs], prompt=prompt, aspect_ratio='9:16'), V / folder / f'{name}.png')


def costume(cid):
    return image('costume-' + cid, [CAST[cid][1] if CAST[cid][1].startswith('/') else LIB + CAST[cid][1]], costume_prompt(cid), 'costume')


if __name__ == '__main__':
    cmd, only = sys.argv[1], sys.argv[2:]
    with ThreadPoolExecutor(6) as ex:
        if cmd == 'costume': fs = [ex.submit(costume, c) for c in CAST if not only or c in only]
        elif cmd == 'plates':
            import shots
            fs = [ex.submit(image, k, v[1], v[0] + shots.STYLE) for k, v in shots.PLATES.items() if not only or k in only]
        else:
            import shots
            sel = [s for s in shots.SHOTS if not only or s['key'] in only]
            fs = [ex.submit(getattr(shots, cmd), s) for s in sel]
        for f in fs: print(*f.result(), flush=True)
