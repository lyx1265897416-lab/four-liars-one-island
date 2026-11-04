"""播放页封面（Vicky 11-03：把最帅的男主放中间）。Jasper 居中靠前、最清楚，其他六人在两侧稍后；脸都在画面上半部，下半部留给标题。用法：python3 cover.py [份数]"""
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
V = Path(__file__).resolve().parent; sys.path.insert(0, str(V))
import gen
from cast import CAST, LIB
def face(c): return CAST[c][1] if CAST[c][1].startswith('/') else LIB + CAST[c][1]
def suit(c): return str(V / 'costume' / f'costume-{c}.png')
REFS = [str(V / 'frames/P_FIRE.png'), face('jasper'), suit('jasper'), face('wes'), suit('wes')] + [suit(c) for c in ('kian', 'ethan', 'brody', 'jude', 'ravi')]
P = ('Poster for a glossy reality-TV dating show, 9:16 vertical. Image 1 is the place: the island villa fire-pit terrace at night with string lights, palm trees, torches and a full moon over the sea; keep its look. '
     'Images 2–3 are JASPER (face, then outfit: ' + CAST['jasper'][4] + '). Images 4–5 are WES (face, then outfit: ' + CAST['wes'][4] + '). '
     'Images 6–10 are the outfits and faces of five more men: KIAN (terracotta linen shirt), ETHAN (sage-green knit polo), BRODY (coral hibiscus shirt over white tank), JUDE (cream knit polo, blond), RAVI (light-grey linen blazer). '
     'Composition: exactly seven men in a V formation, framed from the waist up. JASPER stands dead centre, one step in front of everyone, the tallest and largest in frame, sharpest focus, looking straight into the camera with a cool, confident, magnetic half smile, warm firelight on his face. '
     'WES stands just behind him to his right (screen left), smiling; KIAN and ETHAN further left, BRODY, JUDE and RAVI on the right, each a little further back and slightly softer. Every face is the exact person of his reference, recognisable, no two men look alike. '
     'All seven faces sit in the upper half of the frame (Jasper\'s eyes at about 38% from the top); the lower 40% of the frame falls into dark shadow and warm bokeh so a title can sit over it. The moon and string lights glow above them. '
     'Photorealistic live-action key art, natural skin texture, rich warm saturated colour, cinematic rim light from the pool. No text, no logo, no women, exactly seven men.')
n = int(sys.argv[1]) if len(sys.argv) > 1 else 3
with ThreadPoolExecutor(n) as ex:
    for r in ex.map(lambda i: gen.image(f'COVER_{i}', REFS, P), range(1, n + 1)): print(*r, flush=True)
