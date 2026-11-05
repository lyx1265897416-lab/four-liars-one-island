"""导演层换模型对照（OpenRouter 对 Anthropic 403 期间）：同一开场，选 Jasper → “嗯”两轮，记耗时、打回次数、遗留问题、台词归属。用法：DIRECTOR_MODEL=<id> python3 tests/model_ab.py <输出 json>"""
import json, sys, time
from pathlib import Path
D = Path(__file__).resolve().parent.parent / 'jasper'; sys.path.insert(0, str(D))
import director
src = next(D.glob('ila_*_relay.py')).read_text(encoding='utf-8'); OPEN_STATE = OPEN_NEXT = None
exec(src[src.index('OPEN_STATE ='):src.index('OPEN_NEXT =')]); exec('OPEN_NEXT =' + src.split('OPEN_NEXT =', 1)[1].split('\n\n', 1)[0])
director.FALLBACK_MODEL = director.MODEL  # 对照时不许悄悄退回 GLM
s = dict(history=[], state=OPEN_STATE, place='篝火露台', place_rounds=0, cards=[], stall=0, set=director.OPEN_SET, wardrobe={}); out = []
for text, kind in ((OPEN_NEXT['A']['zh'], 'option'), ('嗯', 'free')):
    t0 = time.time()
    try: sp, sec = director.direct(list(s['history']), s['state'], text, kind, 'auto', place=s['place'], place_rounds=s['place_rounds'], done=tuple(s['cards']), stall=s['stall'], set_now=s['set'], wardrobe={}, cont={'posture': '', 'holding': '', 'looks': {}, 'items': [], 'left': {}, 'outfits': []})
    except Exception as e: out.append({'text': text, 'err': repr(e)[:300], 'sec': round(time.time() - t0, 1)}); break
    out.append({'text': text, 'sec': sec, 'model': sp.get('director_model'), 'attempts': sp.get('director_attempts'), 'lint_left': sp.get('lint_left'), 'seg1': sp.get('seg1'), 'seg2': sp.get('seg2'), 'pending': sp.get('pending_move'), 'next': sp.get('next'), 'did': sp.get('did')})
    s['history'].append({'input': text, 'kind': kind, 'lines': [b[1] for b in sp['seg1']] + [b[1] for b in sp['seg2']], 'did': sp.get('did'), 'ask': sp.get('ask'), 'delivered': True, 'hook_type': sp.get('hook_type'), 'place': sp.get('location'), 'set': sp.get('set'), 'input_type': sp.get('input_type'), 'kiss': bool(sp.get('kiss')), 'surprise': bool(sp.get('surprise')), 'pending': sp.get('pending_move') or {}, 'closed': str(sp.get('closed') or ''), 'opts': []})
    s['state'] = sp.get('state') or s['state']; changed = bool(sp.get('scene_changed')); s['place'] = sp.get('location') or s['place']; s['place_rounds'] = 0 if changed else 1
    if changed: s['set'] = sp.get('set') or s['set']
    s['cards'] += [k for k in (sp.get('cards_done') or []) if k not in s['cards']]
Path(sys.argv[1]).write_text(json.dumps(out, ensure_ascii=False, indent=1))
