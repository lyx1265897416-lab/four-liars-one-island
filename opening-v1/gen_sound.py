# -*- coding: utf-8 -*-
"""开场的环境声、配乐和几个点位音效（waku gen sfx / music）。生成过的跳过。"""
import subprocess, os, concurrent.futures
from pathlib import Path
os.environ['PATH'] = '/Users/vicky/.local/bin:/Users/vicky/.waku/bin:/opt/homebrew/bin:' + os.environ['PATH']
S = Path(__file__).resolve().parent / 'sound'; (S / 'fx').mkdir(parents=True, exist_ok=True)
JOBS = {
    S / 'amb.mp3': ['sfx', 'warm tropical night outdoors at a luxury villa pool party: gentle ocean waves, crickets, crackling fire pit and torch flames, palm leaves in a light breeze, faint distant murmur of a small crowd, no music, no clear words', '--duration', '20'],
    S / 'fx/sting.mp3': ['sfx', 'a short dramatic reality TV reveal sting: a deep bass hit with a shimmering riser tail, cinematic, punchy', '--duration', '2'],
    S / 'fx/whoosh.mp3': ['sfx', 'a soft quick cinematic whoosh transition, airy, short', '--duration', '1'],
    S / 'bgm.mp3': ['music', 'sultry modern reality TV dating show underscore: slow tropical deep-house groove, warm plucked synths, soft four-on-the-floor kick, sly and flirtatious, a hint of suspense, instrumental only, no vocals', '--duration', '45'],
}
def one(item):
    out, args = item
    if out.exists() and out.stat().st_size > 1000: return out.name, 'cached'
    r = subprocess.run(['waku', 'gen', *args, '--out', str(out)], capture_output=True, text=True, timeout=900)
    return out.name, 'ok' if out.exists() else 'FAIL ' + (r.stdout + r.stderr)[-300:]
with concurrent.futures.ThreadPoolExecutor(4) as e:
    for k, s in e.map(one, JOBS.items()): print(k, s, flush=True)
