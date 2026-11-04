"""内容包配图：转 jpg（长边 ≤1400）放 feishu/img/，再复制到公开仓库 realtime-drama-test-log 的 v/ila-pack/，飞书 <img href> 用 Pages 公网地址。尺寸写 sizes.json，地址写 urls.json。只加图片，不动仓库里别的文件。"""
import json, shutil, sys
from pathlib import Path
from PIL import Image
D = Path(__file__).resolve().parent; R = D.parent; O = R / 'opening-v1'; M = R / 'masters'
sys.path.insert(0, str(O))
from cast import CAST, LIB
REPO = Path('/Users/vicky/Interactive storyline/projects/realtime-drama-test-log'); SUB = 'v/ila-pack'
BASE = 'https://lyx1265897416-lab.github.io/realtime-drama-test-log/' + SUB + '/'
def face(c): return Path(CAST[c][1] if CAST[c][1].startswith('/') else LIB + CAST[c][1])
F = {'cover': R / 'docs/media/poster.jpg'}
for c in CAST: F[f'{c}_front'] = face(c); F[f'{c}_suit'] = O / 'costume' / f'costume-{c}.png'
F.update({'L1': O / 'frames/P_FIRE.png', 'L4': O / 'frames/P_POOL.png', 'S01': O / 'frames/S01.png', 'S11': O / 'frames/S11.png',
          'key_wes': M / 'open-key-wes.png', 'key_jasper': M / 'open-key-jasper.png', 'stage_wes': M / 'staging-wes.png', 'stage_jasper': M / 'staging-jasper.png',
          'scooter': M / 'vehicle.png', 'S04': O / 'frames/S04.png'})
(D / 'img').mkdir(exist_ok=True); (REPO / SUB).mkdir(parents=True, exist_ok=True)
sizes, urls = {}, {}
for k, src in F.items():
    im = Image.open(src).convert('RGB'); s = min(1, 1400 / max(im.size))
    if s < 1: im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    out = D / 'img' / f'{k}.jpg'; im.save(out, quality=88); shutil.copy(out, REPO / SUB / out.name)
    sizes[k] = im.size; urls[k] = BASE + out.name
(D / 'sizes.json').write_text(json.dumps(sizes)); (D / 'urls.json').write_text(json.dumps(urls, indent=1))
print(len(F), 'images')
