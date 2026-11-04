"""播放页素材：开场确认版、待机循环、封面、等待配乐传 GCS，写 cdn.json，并把 CDN 地址和开场字幕写进 docs/index.html。换开场后重跑。"""
import json, re, subprocess, time
from pathlib import Path
D = Path(__file__).resolve().parent; S = D / 'docs'; C = D / 'cdn.json'
cdn = json.loads(C.read_text()) if C.exists() else {}
sig = {}
for rel in ('media/OPEN.mp4', 'media/IDLE0.mp4', 'media/poster.jpg', 'audio/WAIT.mp3'):
    f = S / rel; key = f'{f.stat().st_size}-{int(f.stat().st_mtime)}'
    if cdn.get(rel) and cdn.get('_sig', {}).get(rel) == key: sig[rel] = key; continue
    for _ in range(4):
        r = subprocess.run(['waku', 'persist', str(f)], capture_output=True, text=True, timeout=600)
        m = re.search(r'"url":\s*"([^"]+)"', r.stdout)
        if m: cdn[rel] = m.group(1); sig[rel] = key; break
        time.sleep(5)
    else: raise SystemExit('persist failed ' + rel + r.stdout[-200:] + r.stderr[-200:])
    print(rel, cdn[rel], flush=True)
cdn['_sig'] = {**cdn.get('_sig', {}), **sig}; C.write_text(json.dumps(cdn, indent=1))
WHO = {'mei': 'Mei', 'her': 'Her', 'sloane': 'Sloane', 'wes': 'Wes', 'jasper': 'Jasper'}
cues = [dict(s=c['s'], e=c['e'], zh=c['zh'], en=c['en'], who=WHO.get(c['who'], c['who'])) for c in json.load(open(D / 'opening-v1/delivery/cues-确认版.json'))['cues']]
h = (S / 'index.html').read_text(encoding='utf-8')
h = re.sub(r'const CDN = \{.*?\};', lambda m: 'const CDN = ' + json.dumps({k: v for k, v in cdn.items() if not k.startswith('_')}) + ';', h, count=1, flags=re.S)
h = re.sub(r'const OPEN_CUES = \[.*?\];', lambda m: 'const OPEN_CUES = ' + json.dumps(cues, ensure_ascii=False) + ';', h, count=1, flags=re.S)
(S / 'index.html').write_text(h, encoding='utf-8'); (S / 'open_cues.json').write_text(json.dumps(cues, ensure_ascii=False)); print('index ok', len(cues), 'cues')
