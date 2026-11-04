# -*- coding: utf-8 -*-
"""主持人换人（Vicky 11-03：外国人优先，但要有点亚裔的感觉）。H1–H6 新生成，L1–L2 取自角色库；都穿同一套象牙白西装裙，白底全身。
用法：python3 host_cands.py → costume/host-*.png，拼板 ../casting/host_v1.jpg"""
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
V = Path(__file__).resolve().parent
sys.path.insert(0, str(V))
import gen
from cast import CAST, LIB
SUIT = CAST['mei'][4]
BASE = ('Full-body costume reference photo of an original fictional woman, a polished TV host, {age}. Eurasian, mixed European and East Asian heritage: '
        'she reads as Western at first glance, with a subtle East Asian quality in the eyes and cheekbones. {face} '
        'Wardrobe: ' + SUIT + '. She stands straight facing the camera, relaxed confident pose, whole body visible from head to shoes, centred, '
        'on a seamless pure white studio background with soft even light and a faint floor shadow. Photorealistic live-action photograph, natural skin texture with fine lines appropriate to her age, '
        'true-to-life proportions, sharp focus, 85mm lens look. Not a celebrity, not any real person. No text, no logos, no extra people.')
NEW = {
    'H1': ('about 42', 'Sleek chin-length jet-black bob with a sharp side part, light olive skin, hooded almond-shaped hazel eyes, high cheekbones, a defined jaw, red-brown lipstick; sharp, witty, in control.'),
    'H2': ('about 40', 'Long glossy dark-brown waves past the shoulders with a centre part, warm light skin, soft almond grey-green eyes with a slight upward tilt, a straight nose, nude-rose lips; warm and knowing.'),
    'H3': ('about 45', 'Dark-chocolate hair in a low sleek chignon, fair skin with light freckles, narrow honey-brown eyes, strong brows, wide cheekbones, a confident closed smile; elegant and amused.'),
    'H4': ('about 38', 'Shoulder-length soft caramel-brown hair with face-framing layers, golden light skin, large dark-brown almond eyes with a single-lid fold, a small chin, glossy coral lips; playful and teasing.'),
    'H5': ('about 44', 'A sharp asymmetric black lob with one side tucked behind the ear, pale neutral skin, light-brown hooded eyes, angular cheekbones, a long neck, deep berry lips; cool and dry-humoured.'),
    'H6': ('about 41', 'Voluminous blow-dried dark auburn hair to the collarbone, medium warm skin, dark almond eyes with a slight epicanthic fold, full brows, a broad bright smile; charismatic showbiz energy.'),
}
LIBP = {  # 角色库里偏混血感的两位（都较年轻）
    'L1': LIB + 'white-portraits-24-20260922/character-04.png',
    'L2': LIB + 'front-id-32-20260923/character-14.png',
}
def lib_prompt():
    return ('Full-body costume reference photo of the exact same woman as in the reference image, styled about 35 as a polished TV host: keep her identical face, eyes, skin tone and hair colour; '
            'the face must be instantly recognisable as the same person. Hair styled sleek and glossy. Wardrobe: ' + SUIT + '. She stands straight facing the camera, relaxed confident pose, whole body visible from head to shoes, centred, '
            'on a seamless pure white studio background with soft even light and a faint floor shadow. Photorealistic live-action photograph, natural skin texture, true-to-life proportions, sharp focus, 85mm lens look. No text, no logos, no extra people.')
if __name__ == '__main__':
    with ThreadPoolExecutor(8) as ex:
        fs = [ex.submit(gen.image, 'host-' + k, [], BASE.format(age=a, face=f), 'costume') for k, (a, f) in NEW.items()]
        fs += [ex.submit(gen.image, 'host-' + k, [p], lib_prompt(), 'costume') for k, p in LIBP.items()]
        for f in fs: print(*f.result(), flush=True)
