# -*- coding: utf-8 -*-
"""《三真四假》开场 V1：海岛别墅，夜，篝火和泳池。13 镜，照 meet-me-third 确认版开场的做法：
对白一律近景单人、原生演出（Seedance 2.5 原声）、视线贴镜头一侧、画边留对方一缕虚焦；反应真人即时；每镜留原生音。
轴线和共用模板一致：男人在画左、看向画右；她在画右、看向画左。"""
from pathlib import Path
from cast import CAST, LIB
import gen
V = Path(__file__).resolve().parent
FR, CO = str(V / 'frames') + '/', str(V / 'costume') + '/'
def face(c): return CAST[c][1] if CAST[c][1].startswith('/') else LIB + CAST[c][1]
def suit(c): return CO + f'costume-{c}.png'
def refs(*cs): return [p for c in cs for p in (face(c), suit(c))]

STYLE = ("Photorealistic live-action reality-TV romance drama, shot on a cinema camera: natural skin texture, real fabric, true-to-life proportions, shallow depth of field. "
         "Night lighting: faces are well exposed by warm torch and string-light key light, the surroundings fall off into deep blue-black night, turquoise pool glow as rim light. "
         "Rich warm saturated colour, never grey, never washed out, never flat, not plastic, not CGI, not anime. No text, no captions, no logos, no watermark. 9:16 vertical.")
PLACE = ("PLACE: a luxury island villa terrace at night. A long infinity pool glowing turquoise, tall palm trees, tiki torches with real flames, warm string lights overhead, "
         "a round sunken fire pit with cream cushioned seating, white modern villa walls with an open-tread exterior stair going up to a roof deck, and the dark ocean with a bright moon path behind. ")
LOOK = {c: f"{CAST[c][0].upper()}: the exact person of the {CAST[c][0]} face reference, same face, hair and skin; wearing exactly the outfit of the {CAST[c][0]} costume reference: {CAST[c][4]}." for c in CAST}
LOOK['her'] = ("HER: the exact woman of her face reference (warm tan skin, long straight chestnut-brown hair with a centre part, dark brown eyes, small gold hoops); wearing exactly her costume reference: " + CAST['her'][4] + '.')
GUARD = ("One single continuous camera take: no cut, no dissolve, no morph, no zoom unless written. Faces, hair, clothes and props keep exactly the first frame's shape, colour and rendering in every frame. "
         "Real-time speed, natural weight, quick human reactions, never slow motion.")
ONLY = "Only the people named in this shot are in the picture, nobody else: no extra person, no extra hands."
VOICE = {
    'mei': 'A polished, warm, teasing early-forties American female TV-host voice, crisp diction, relishing the twist.',
    'her': 'A natural low-mid young American female voice, quick and quietly amused, unbothered.',
    'sloane': 'A bright, sugary young American female voice with a sharp edge under the sweetness.',
    'wes': 'A warm, easy young American male voice, relaxed, a smile in it.',
    'jasper': 'A low, quiet, unhurried young American male voice, few words, dry.',
}
# 近景单人：画边一缕对方虚焦；男人和 Sloane 在画左看画右，她在画右看画左（她看他们时视线在镜头左侧）
def cu(c, other_edge, look_side, bg):
    return (f"Close-up of {CAST[c][0] if c != 'her' else 'her'} alone, head and chest, face large and centred, turned almost straight to the camera. "
            f"At the very {other_edge} edge only a thin soft-focus sliver of {('her long chestnut hair and champagne-gold satin strap' if c != 'her' else 'the other person’s shoulder')} is visible, very close to the camera; nothing else of that person. "
            f"Behind, softly out of focus: {bg}. ")
def eye(look_side):
    return (f"EYE CONTACT: the eyes stay open and look at the other person, aimed just to the {look_side} of the camera lens, almost into the lens; this eye line holds through the whole shot. "
            "Never looks down or away, never closes the eyes; when smiling the eyes stay open. ")
BG_FIRE = 'the round fire pit with flames, tiki torches and the moonlit ocean'
BG_POOL = 'the glowing turquoise pool, palm trees, string lights and the white villa'
BG_STAIR = 'the white villa wall, the open-tread stair and string lights against the night sky'

PLATES = {
    'P_FIRE': ("Empty set, no people: " + PLACE + "Seen from the villa side toward the sea: the sunken fire pit in the middle ground with flames, cream cushions, torches around it, the ocean and moon behind. ", []),
    'P_POOL': ("Empty set, no people: " + PLACE + "Seen along the long side of the turquoise pool toward the white villa, palms and string lights, the fire pit glowing far away on the left. ", []),
}

# lines: (说话人, 英, 中)；ndur = Seedance 时长；take = 剪辑取用窗口（秒）
SHOTS = [
 dict(key='S01', plate=None, who=[], dur=5, take=(.3, 2.25), lines=[],
      frame="Wide aerial establishing view at night, composed for 9:16: " + PLACE + "Contestants are tiny silhouettes far away around the fire pit, no faces readable. ",
      act="A slow aerial drift forward and down toward the fire pit. Torch flames flicker, palm fronds move in the sea breeze, the pool water ripples, the moon path glitters on the sea."),
 dict(key='S03', plate='P_FIRE', who=['mei'], dur=6, take=None,
      lines=[('mei', "Seven gorgeous men. Three of them are millionaires looking for a wife.", "七个大帅哥。其中三个是来找老婆的千万富翁。")],
      frame="Mei alone, medium close-up, standing in front of the fire pit, facing the camera directly like a host presenting to the audience, holding the plain cream card at her waist; a knowing smile. ",
      act="She addresses the camera directly like a TV host, one eyebrow lifting, a small gesture of the card toward the off-screen men on the left."),
 dict(key='S02', plate='P_FIRE', who=['jasper', 'wes', 'ethan', 'brody', 'kian', 'jude', 'ravi'], dur=5, take=(.3, 3.0), lines=[],
      frame="Medium-wide shot of exactly seven men standing in one loose line in front of the fire pit, full figures from the knees up, each one a different person exactly as in his references, left to right: Jasper, Wes, Ethan, Brody, Kian, Jude, Ravi. They stand on the stone deck in front of the camera; the fire pit glows several metres BEHIND the line, small in the background, and nobody stands in, over or next to the fire. Torchlight on their faces, ocean and moon behind. ",
      act="Slow sideways dolly along the line from left to right. The men shift their weight, one smiles, one adjusts his collar, one glances at the next; small natural movements, nobody walks out of the line."),
 dict(key='S04', plate='P_FIRE', who=['mei'], dur=7, take=None,
      lines=[('mei', "The other four are broke… and faking it for a million dollars. Fall for a fake, and he's the one you fly home with.", "另外四个身无分文……装富豪，是为了一百万奖金。爱上假的，你就得跟他一起回家。")],
      frame="Mei alone, close-up framed from the chest up, standing upright in front of the fire pit (not sitting, not crouching, no knees or legs in the picture), facing the camera directly, her head tipped forward a little as if sharing a secret; card held near her chest. ",
      act="She lowers her voice for the reveal, then lands the last sentence with a wicked little smile straight into the camera."),
 dict(key='S05', plate='P_POOL', who=['her'], dur=5, take=(.4, 3.2), lines=[],
      frame="She walks along the edge of the glowing pool toward the camera, framed from the knees up, the long champagne-gold satin dress catching the light, chestnut hair moving, looking around the party with a calm, confident half smile. ",
      act="Handheld camera backs away in front of her as she walks toward it at a natural pace; she takes in the party, glances to screen left at something, and her half smile sharpens."),
 dict(key='S06', plate='P_POOL', who=['sloane'], dur=6, take=None,
      lines=[('sloane', "Champagne dress, night one? Bold. Shame you won't make it to Friday.", "第一晚就穿香槟色？真敢。可惜你撑不到周五。")],
      frame=cu('sloane', 'RIGHT', 'right', BG_POOL) + "She holds a coupe glass of champagne at chest height; a sweet smile that does not reach her eyes. ",
      act="She looks the other woman up and down once, quickly, then back to her face and says her line with sugary venom, a tiny tilt of the head."),
 dict(key='S07', plate='P_POOL', who=['her'], dur=4, take=None,
      lines=[('her', "Then I'd better work fast.", "那我得抓紧了。")],
      frame=cu('her', 'LEFT', 'left', BG_POOL) + "Unbothered, a small amused smile. ",
      act="She answers without missing a beat, amused, chin up, then holds the look."),
 dict(key='S08', plate='P_POOL', who=['wes'], dur=6, take=None,
      lines=[('wes', "Ignore her. I'm Wes. This one's yours — no tiny umbrella.", "别理她。我是 Wes。这杯给你，没插小伞的。")],
      frame=cu('wes', 'RIGHT', 'right', BG_POOL) + "He holds out a short glass of a pale cocktail with a lime wedge toward screen right at chest height; an easy, warm smile. ",
      act="He offers the glass toward her with a small easy nod and says his line, warm and a little self-deprecating."),
 dict(key='S09', plate='P_POOL', who=['her'], dur=5, take=None,
      lines=[('her', "So, Wes. Real or fake?", "那么，Wes。你是真的，还是假的？")],
      frame=cu('her', 'LEFT', 'left', BG_POOL) + "She holds the pale cocktail with the lime wedge at chest height, just taken from him. ",
      act="She takes one small sip, lowers the glass and asks, playful but testing, eyes holding his."),
 dict(key='S10', plate='P_POOL', who=['wes'], dur=6, take=None,
      lines=[('wes', "Ask me again in a week. I'll still be here.", "一周后再问我。我还会在这儿。")],
      frame=cu('wes', 'RIGHT', 'right', BG_POOL) + "His hands are out of the frame; open, steady expression. ",
      act="He doesn't flinch at the question; a small honest smile, and he answers simply, holding her gaze."),
 dict(key='S11', plate=None, who=['jasper'], dur=6, take=None,
      lines=[('jasper', "You want a straight answer? Not down there.", "想听实话？下面可没有。")],
      frame="Jasper alone, close-up from a low angle, standing a few steps up the open-tread exterior stair, one hand on the rail, looking down toward screen right; " + BG_STAIR + " behind him, softly out of focus. A cool, unreadable face. ",
      act="He looks down at her, says his line quietly, then tips his head once toward the roof above and turns to climb, a last glance back over his shoulder."),
 dict(key='S12', plate='P_POOL', who=['her'], dur=5, take=(.3, 3.0), lines=[],
      extra=[FR + 'S09.png'],
      frame=cu('her', 'LEFT', 'left', BG_POOL) + "The last image is the previous shot of her: keep exactly that same drink, a short clear tumbler of pale cocktail with a lime wedge, no straw, no flower, held the same way. Her eyes are lifted up toward the upper left where the stair is. ",
      act="Silent. Her eyes go up to the stair at the upper left, then come back down to the man in front of her at the left edge of the lens; a tiny intrigued smile, she weighs it. Quick, real-time."),
 dict(key='S13', plate='P_FIRE', who=['mei'], dur=5, take=None,
      lines=[('mei', "Ladies — at midnight, you couple up.", "女士们——午夜，选出你的搭档。")],
      frame="Mei alone, medium close-up at the fire pit, facing the camera, raising the cream card high like an announcement; torches behind her. ",
      act="She raises the card and announces the line with relish to everyone at the party, then smiles straight into the camera."),
]
for s in SHOTS:
    s['ndur'] = s['dur']
    if s['key'] in ('S06', 'S08', 'S10'): s['act'] += ' ' + eye('right')
    if s['key'] in ('S07', 'S09', 'S12'): s['act'] += ' ' + eye('left')

def plates(s=None):
    return [gen.image(k, v[1], v[0] + STYLE) for k, v in PLATES.items()]

def frames(s):
    rs = ([FR + s['plate'] + '.png'] if s['plate'] else []) + refs(*s['who']) + s.get('extra', [])
    head = ('Image 1 is the empty location plate of this exact set: keep its background, architecture, colours and light. The other images are identity (face) and costume references in pairs; do not copy their white background or framing. '
            if s['plate'] else ('The images are identity (face) and costume references in pairs; do not copy their white background or framing. ' if s['who'] else ''))
    who = ' '.join(LOOK[c] for c in s['who'])
    return gen.image(s['key'], rs, head + s['frame'] + PLACE + who + (' ' + ONLY if s['who'] else '') + ' ' + STYLE)

def native(s):
    who = ' '.join(LOOK[c] for c in s['who'])
    say = ''
    if s['lines']:
        c, en, _ = s['lines'][0]
        say = (f'{CAST[c][0] if c != "her" else "She"} says aloud, in English, exactly these words once, in order, with real acting and natural timing: "{en}" {VOICE[c]} '
               'Only this person speaks, only that line. Lips move with the words and close when finished. No music, no other voices. ')
    else:
        say = 'Nobody speaks. Natural ambient sound of the place only: torches, sea breeze, distant party murmur. No music. '
    p = s['act'] + ' ' + say + PLACE + who + (' ' + ONLY if s['who'] else '') + ' ' + GUARD + ' ' + STYLE
    return gen.run('native-' + s['key'], 'bytedance/seedance-2.5/image-to-video', 'multimodal.generate.video',
                   dict(image=gen.upload(V / 'frames' / f"{s['key']}.png"), prompt=p, duration=s['ndur'], resolution='720p', generate_audio=True),
                   V / 'takes' / f"{s['key']}.mp4")
