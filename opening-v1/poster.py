# -*- coding: utf-8 -*-
"""海报版封面（Vicky 11-03：改成海报形式，女主在前面 C 位，可以加其他女生做不同版本对比，后面男生随机排列）。
四版：P1 只有她；P2 她 + Sloane；P3 她 + Sloane + 主持人 Mei；P4 她 + Sloane + 两位别的女嘉宾。每版男生顺序随机（固定种子，可复现）。
带片名和一句宣传语（英文），播放页用的是同一张的无字版。用法：python3 poster.py [P1 P2 ...]"""
import random, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
V = Path(__file__).resolve().parent; sys.path.insert(0, str(V))
import gen
from cast import CAST, LIB
def face(c): return CAST[c][1] if CAST[c][1].startswith('/') else LIB + CAST[c][1]
def suit(c): return str(V / 'costume' / f'costume-{c}.png')
MEN = ['jasper', 'wes', 'ethan', 'brody', 'kian', 'jude', 'ravi']
DESC = {'jasper': 'JASPER (dark curly hair, midnight-navy silk shirt)', 'wes': 'WES (tousled dark-blond hair, sky-blue linen shirt)', 'ethan': 'ETHAN (brown curls, sage-green knit polo)',
        'brody': 'BRODY (sandy curls, coral hibiscus shirt over white tank)', 'kian': 'KIAN (dark hair, terracotta linen shirt)', 'jude': 'JUDE (blond, cream knit polo)', 'ravi': 'RAVI (black hair, light-grey linen blazer)'}
HER = 'HER: ' + CAST['her'][4]
WOMEN = {
 'P1': [],
 'P2': ['sloane'],
 'P3': ['sloane', 'mei'],
 'P4': ['sloane'],
}
FRONT = {
 'P1': 'She stands alone in the front row, dead centre, the largest and sharpest figure, framed from mid-thigh up.',
 'P2': 'She stands in the front row dead centre, the largest and sharpest figure; SLOANE stands half a step behind her on screen right, arms folded, a sweet smile with an edge, smaller than her.',
 'P3': 'She stands in the front row dead centre, the largest and sharpest figure; SLOANE stands half a step behind her on screen right with a sly smile; the host MEI stands half a step behind her on screen left holding up a plain cream card, amused. Both are smaller than her.',
 'P4': 'She stands in the front row dead centre, the largest and sharpest figure; flanking her half a step behind, three other female contestants: SLOANE on screen right, and two more original women on screen left (one with a glossy black bob in an emerald satin slip dress, one with long auburn waves in a white crochet mini dress). All three are smaller than her.',
}
TEXT = ('At the top of the poster, the title "FOUR LIARS, ONE ISLAND" in bold glowing hot-pink condensed capital letters with a soft neon glow, spelled exactly like that; '
        'under it in small white capitals: "SEVEN MEN. FOUR ARE LYING. WHO DO YOU TRUST?". No other text anywhere.')
NOTEXT = 'Leave the top fifth of the frame as dark night sky with the moon and string lights, no text at all.'
def prompt(k, text=True):
    rnd = random.Random({'P1': 11, 'P2': 22, 'P3': 33, 'P4': 44}[k]); men = MEN[:]; rnd.shuffle(men)
    row = ', '.join(DESC[m] for m in men)
    women = WOMEN[k]
    refs_txt = ('Image 1 is the place. Images 2–3 are HER face and outfit. '
                + ''.join(f'Images {4 + 2 * i}–{5 + 2 * i} are {w.upper()} face and outfit. ' for i, w in enumerate(women))
                + f'The last seven images are the seven men in this order: {", ".join(m.upper() for m in MEN)}; each shows his face and outfit.')
    return ('Glossy key-art poster for a reality-TV dating show, 9:16 vertical, night on the island villa fire-pit terrace (image 1): string lights, palm trees, torches, the infinity pool glow and a full moon over the sea. ' + refs_txt + ' '
            + 'HER is the star of the poster. ' + FRONT[k] + ' She looks straight into the camera with a knowing, confident half smile, one hand resting on her hip, the champagne-gold satin catching the firelight. ' + HER + ' '
            + f'Behind her, a loose staggered row of the seven men, left to right exactly in this order: {row}. They are a little out of focus and smaller, some looking at her, some at the camera; every man is the exact person of his reference, no two look alike. '
            + 'Her face sits at about 40% from the top; the bottom fifth of the poster falls into dark shadow. Photorealistic live-action key art, natural skin texture, rich warm saturated colour, cinematic rim light. '
            + (TEXT if text else NOTEXT) + ' Adults only.')
def refs(k): return [str(V / 'frames/P_FIRE.png'), face('her'), suit('her')] + [x for w in WOMEN[k] for x in (face(w), suit(w))] + [suit(m) for m in MEN]
if __name__ == '__main__':
    ks = sys.argv[1:] or list(WOMEN)
    with ThreadPoolExecutor(8) as ex:
        fs = [ex.submit(gen.image, f'POSTER_{k}', refs(k), prompt(k, True)) for k in ks] + [ex.submit(gen.image, f'POSTER_{k}_clean', refs(k), prompt(k, False)) for k in ks]
        for f in fs: print(*f.result(), flush=True)
