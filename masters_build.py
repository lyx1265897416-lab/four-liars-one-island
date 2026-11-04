# -*- coding: utf-8 -*-
"""实时版母版（两条线共用一套人物，站位图和第 1 轮关键帧各一张）。
用法：python3 masters_build.py gen     生成站位图、第 1 轮关键帧、小摩托（gpt-image-2/edit，复用 opening-v1/gen.py）
      python3 masters_build.py upload  裁头像、拼合图、取开场末帧，上传 Vivix，写 wes/ 和 jasper/ 的 masters/urls.json"""
import json, shutil, subprocess, sys
from pathlib import Path
from PIL import Image
D = Path(__file__).resolve().parent; M = D / 'masters'; M.mkdir(exist_ok=True); O = D / 'opening-v1'
sys.path.insert(0, str(O))
from cast import CAST, LIB
FF = '/Users/vicky/Interactive storyline/.media-runtime/imageio_ffmpeg/binaries/ffmpeg-macos-aarch64-v7.1'
OPEN = O / 'delivery/ILA_OPENING_确认版.mp4'
def face(c): return Path(CAST[c][1] if CAST[c][1].startswith('/') else LIB + CAST[c][1])
def suit(c): return O / 'costume' / f'costume-{c}.png'
STYLE = ('Photorealistic live-action reality-TV romance drama, the same look as the reference frames: natural skin texture, real fabric, true-to-life proportions. '
         'Rich warm saturated colour, never grey, never flat. No text, no logo, no watermark. Adults.')
NIGHT = O / 'frames/S09.png'  # 开场里她在泳池边的近景：夜景光线、她的脸和裙子
def two(he):
    n = CAST[he][0]
    return (f'{n.upper()}: exactly the face and hair of the man in his face reference, wearing exactly his costume reference: {CAST[he][4]}. '
            f'HER: exactly the face and hair of the woman in her face reference, wearing exactly her costume reference: {CAST["her"][4]}.')
JOBS = {}
for he in ('wes', 'jasper'):
    JOBS[f'staging-{he}'] = ([face(he), suit(he), face('her'), suit('her')],
        f'Full-body two-shot on a plain mid-grey studio background. Images 1–2 are his face and costume, images 3–4 are her face and costume. {CAST[he][0]} on the LEFT of the frame, she on the RIGHT, standing facing each other half an arm apart, both in three-quarter view toward each other, both faces clearly visible, head to toe in frame, he is a head taller. Hands relaxed. ' + two(he) + ' ' + STYLE)
    JOBS[f'open-key-{he}'] = ([O / 'frames/P_FIRE.png', face(he), suit(he), face('her'), suit('her'), NIGHT],
        'Image 1 is this place: the night fire-pit terrace of the island villa, keep its fire pit, cream cushions, torches, string lights, pool glow and moonlit sea. Images 2–3 are his face and costume, images 4–5 are her face and costume, image 6 shows her face, dress and the night light exactly. '
        f'A waist-up two-shot at midnight by the fire pit: {CAST[he][0]} on the LEFT of the frame, she on the RIGHT, standing facing each other about an arm apart, both in three-quarter view toward each other with both faces clearly visible and large, both heads complete with headroom. '
        'She holds one short clear tumbler of pale cocktail with a lime wedge at her waist; he has empty hands. The fire pit glows behind them, slightly out of focus. Faces lit warm by the fire and torches, surroundings deep blue night. Only these two people. ' + two(he) + ' ' + STYLE)
JOBS['vehicle'] = ([O / 'frames/P_POOL.png'],
    'Use image 1 only as the place and the light. Picture of exactly one small white electric step-through scooter with a round headlight and a beige seat, parked on a palm-lined path by the villa at night, side view, whole scooter in frame. No people, no text, no logo, no number plate. ' + STYLE)

def sheet(paths, out, h=1100):
    ims = [Image.open(p).convert('RGB') for p in paths]; ims = [x.resize((int(x.width * h / x.height), h), Image.LANCZOS) for x in ims]
    s = Image.new('RGB', (sum(i.width for i in ims), h), 'white'); x = 0
    for i in ims: s.paste(i, (x, 0)); x += i.width
    s.save(out, quality=92)
def crop(src, out, top, bot, left=0.0, right=1.0):
    im = Image.open(src).convert('RGB'); W, H = im.size; im.crop((int(W * left), int(H * top), int(W * right), int(H * bot))).save(out, quality=93)

if sys.argv[1] == 'gen':
    import gen as G
    from concurrent.futures import ThreadPoolExecutor
    def one(k):
        refs, p = JOBS[k]; r = G.image('M_' + k, [str(x) for x in refs], p)
        shutil.copy(O / 'frames' / f'M_{k}.png', M / f'{k}.png'); return r
    with ThreadPoolExecutor(5) as ex:
        for r in ex.map(one, [k for k in JOBS if not (M / f'{k}.png').exists()]): print(*r, flush=True)
elif sys.argv[1] == 'upload':
    for c in ('wes', 'jasper', 'her'): crop(face(c), M / f'{c}-head.jpg', 0, .62, .08, .92)
    for c in ('wes', 'jasper'): crop(suit(c), M / f'{c}-upper.jpg', 0, .55, .15, .85)
    sheet([face('her'), suit('her'), NIGHT], M / 'her-sheet.jpg')
    for c in ('mei', 'sloane', 'wes', 'jasper', 'ethan', 'brody'): sheet([face(c), suit(c)], M / f'{c}-sheet.jpg')
    subprocess.run([FF, '-y', '-v', 'error', '-sseof', '-0.15', '-i', str(OPEN), '-frames:v', '1', '-q:v', '2', str(M / 'idle-key.jpg')], check=True)
    for k in ('staging-wes', 'staging-jasper', 'open-key-wes', 'open-key-jasper', 'vehicle'):
        Image.open(M / f'{k}.png').convert('RGB').save(M / f'{k}.jpg', quality=93)
    sys.path.insert(0, '/Users/vicky/Interactive storyline')
    import os; os.environ.setdefault('MAG_PUBLIC', '1')
    for _l in open('/Users/vicky/Interactive storyline/.env.vivix', encoding='utf-8'):
        if '=' in _l and _l.split('=', 1)[0].strip() == 'VIVIX_API_KEY': os.environ.setdefault('VIVIX_API_KEY', _l.split('=', 1)[1].strip().strip('"\''))
    from vivix_w1 import W1Client
    cl = W1Client(); F = M / 'urls-shared.json'; U = json.loads(F.read_text()) if F.exists() else {}
    files = {'her': M / 'her-sheet.jpg', 'her_head': M / 'her-head.jpg', 'look_she_on': suit('her'), 'vehicle': M / 'vehicle.jpg', 'idle_key': M / 'idle-key.jpg',
             **{c: suit(c) for c in ('mei', 'sloane', 'wes', 'jasper', 'ethan', 'brody')},  # V3.0：配角母版用单人定装全身图。原来的“头像 + 全身”两格合图被模型当成两个人，画出两个 Sloane、两个 Mei（S2351533a4）
             **{f'face-{c}': face(c) for c in ('wes', 'jasper')}, **{f'face_head-{c}': M / f'{c}-head.jpg' for c in ('wes', 'jasper')},
             **{f'outfit-{c}': M / f'{c}-upper.jpg' for c in ('wes', 'jasper')},
             **{f'staging-{c}': M / f'staging-{c}.jpg' for c in ('wes', 'jasper')}, **{f'open_key-{c}': M / f'open-key-{c}.jpg' for c in ('wes', 'jasper')}}
    for key, f in files.items():
        if key in U: continue
        U[key] = cl.upload(str(f))['url']; F.write_text(json.dumps(U, indent=1)); print(key, U[key], flush=True)
    for he in ('wes', 'jasper'):  # 每条线自己的 urls.json：face / outfit / staging / open_key 是这条线男主的
        T = {k: v for k, v in U.items() if '-' not in k}
        T.update(face=U[f'face-{he}'], face_head=U[f'face_head-{he}'], outfit=U[f'outfit-{he}'], staging=U[f'staging-{he}'], open_key=U[f'open_key-{he}'])
        (D / he / 'masters' / 'urls.json').write_text(json.dumps(T, indent=1)); shutil.copy(M / f'open-key-{he}.jpg', D / he / 'masters' / 'open-key.jpg')
        print(he, 'urls ok', len(T))
