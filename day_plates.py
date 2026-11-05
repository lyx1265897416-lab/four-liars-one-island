"""V3.11：白天的地点空景（原来的空景都是夜景，白天的泳池、套房、吧台戏照着夜景拍成了夜里）。
用法：python3 day_plates.py gen   以夜景空景为参考，gpt-image-2/edit 出同一地点的白天版 → masters/plate-P_*_DAY.png
      python3 day_plates.py upload  传 Vivix，写进两条线 masters/urls.json 的 plates（键名带 @day，按地点和时间挑，见共用模板 plate_for）"""
import json, shutil, sys
from pathlib import Path
D = Path(__file__).resolve().parent; M = D / 'masters'; sys.path.insert(0, str(D / 'opening-v1'))
DAY = {'P_POOL': ('泳池', 'the long turquoise infinity pool with white loungers and umbrellas'),
       'P_SUITE': ('套房', 'the white suite: white plaster walls, light wood floor, one white linen bed, a white daybed sofa by the window, sheer white curtains'),
       'P_BAR': ('吧台', 'the outdoor bar: rattan bar stools, wooden bar counter, a row of label-free bottles')}
STYLE = 'Photorealistic live-action reality-TV look, natural colour, no text, no logo, no watermark.'
if sys.argv[1] == 'gen':
    import gen as G
    from concurrent.futures import ThreadPoolExecutor
    def one(k):
        prompt = (f'Image 1 is this exact place at night. Show the same place from the same camera angle with the same layout, architecture and furniture ({DAY[k][1]}), '
                  'but in bright late-morning tropical daylight: clear blue sky, strong sunlight and soft shadows, the sea bright turquoise, string lights and torches switched off. '
                  'Empty set, no people, no hands, no animals. ' + STYLE)
        r = G.image(f'{k}_DAY', [str(M / f'plate-{k}.jpg')], prompt); shutil.copy(D / 'opening-v1' / 'frames' / f'{k}_DAY.png', M / f'plate-{k}_DAY.png'); return r
    with ThreadPoolExecutor(3) as ex:
        for r in ex.map(one, DAY): print(*r, flush=True)
else:
    import os
    from PIL import Image
    sys.path.insert(0, '/Users/vicky/Interactive storyline'); os.environ.setdefault('MAG_PUBLIC', '1')
    for _l in open('/Users/vicky/Interactive storyline/.env.vivix', encoding='utf-8'):
        if '=' in _l and _l.split('=', 1)[0].strip() == 'VIVIX_API_KEY': os.environ.setdefault('VIVIX_API_KEY', _l.split('=', 1)[1].strip().strip('"\''))
    from vivix_w1 import W1Client
    cl = W1Client(); add = {}
    for k, (kw, _) in DAY.items():
        j = M / f'plate-{k}_DAY.jpg'; Image.open(M / f'plate-{k}_DAY.png').convert('RGB').save(j, quality=92); add[kw + '@day'] = cl.upload(str(j))['url']; print(k, add[kw + '@day'])
    for he in ('wes', 'jasper'):
        f = D / he / 'masters' / 'urls.json'; U = json.loads(f.read_text()); U.setdefault('plates', {}).update(add); f.write_text(json.dumps(U, indent=1)); print(he, 'plates', list(U['plates']))
