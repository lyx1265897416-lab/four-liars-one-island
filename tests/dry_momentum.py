"""V3.9 角色出招干跑（不花视频钱）：低输入为主的一串输入，看每轮结尾谁出招（pending_move）、有没有关闭疑问（closed）、选项是不是在回应那一招、配角有没有自己的目标。
用法：python3 tests/dry_momentum.py <合成好的线目录（可以是隔离副本）> <输出 json>"""
import json, sys, time
from pathlib import Path
D = Path(sys.argv[1]).resolve(); sys.path.insert(0, str(D))
import director
src = next(D.glob('ila_*_relay.py')).read_text(encoding='utf-8'); OPEN_STATE = OPEN_NEXT = None
exec(src[src.index('OPEN_STATE ='):src.index('OPEN_NEXT =')]); exec('OPEN_NEXT =' + src.split('OPEN_NEXT =', 1)[1].split('\n\n', 1)[0])
s = dict(history=[], state=OPEN_STATE, place='篝火露台', place_rounds=0, cards=[], stall=0, set=director.OPEN_SET, wardrobe={})
PLAN = [('A', 'option'), ('嗯', 'free'), ('嗯', 'free'), ('A', 'option'), ('为什么？', 'free'), ('好', 'free')]
nx = OPEN_NEXT; out = []
for n, (inp, kind) in enumerate(PLAN, 1):
    text = (nx.get('A') or {}).get('zh') if inp == 'A' else inp
    sp, sec = director.direct(list(s['history']), s['state'], text, kind, 'auto', place=s['place'], place_rounds=s['place_rounds'], done=tuple(s['cards']), stall=s['stall'], set_now=s['set'], wardrobe=dict(s['wardrobe']), cont={'posture': '', 'holding': '', 'looks': {}, 'items': [], 'left': {}, 'outfits': []})
    print(f"\n### R{n} [{kind}] {text} | {sec}s model={sp.get('director_model')} loc={sp.get('location')} cards={sp.get('cards_done')} surprise={sp.get('surprise')}")
    print('  pending', json.dumps(sp.get('pending_move'), ensure_ascii=False)); print('  closed', sp.get('closed')); print('  he_move', sp.get('he_move'), '| persona', sp.get('persona_beat'))
    for k in ('seg1', 'seg2'):
        for b in sp.get(k) or []: print('   ', k[-1], '|', str(b[0])[:70], '|', str(b[1])[:70], '|', (b[3] if len(b) > 3 else ''))
    nx = sp.get('next') or {}; print('  cue', (nx.get('cue') or {}).get('zh')); print('  A', (nx.get('A') or {}).get('zh'), '\n  B', (nx.get('B') or {}).get('zh')); print('  lint_left', [x[:50] for x in sp.get('lint_left') or []][:4], flush=True)
    out.append(dict(n=n, text=text, kind=kind, sec=sec, sp=sp))
    s['history'].append({'input': text, 'kind': kind, 'lines': [b[1] for b in sp['seg1']] + [b[1] for b in sp['seg2']], 'did': sp.get('did'), 'ask': sp.get('ask'), 'delivered': bool(sp.get('delivered')), 'hook_type': sp.get('hook_type'),
                         'reveal': sp.get('reveal') or [], 'intimacy': sp.get('intimacy') or 0, 'place': sp.get('location'), 'set': sp.get('set'), 'extras': sp.get('extras') or [], 'input_type': sp.get('input_type'), 'kiss': bool(sp.get('kiss')), 'surprise': bool(sp.get('surprise')), 'staging': sp.get('staging'),
                         'pending': sp.get('pending_move') if isinstance(sp.get('pending_move'), dict) else {}, 'closed': str(sp.get('closed') or ''), 'opts': [((sp.get('next') or {}).get(k) or {}).get('zh', '') for k in ('A', 'B')]})
    changed = bool(sp.get('scene_changed')); s['state'] = sp.get('state') or s['state']; s['place'] = sp.get('location') or s['place']; s['place_rounds'] = 0 if changed else s['place_rounds'] + 1
    if changed: s['set'] = sp.get('set') or s['set']
    s['wardrobe'] = sp.get('wardrobe_end') or {}
    new = [str(k).strip().upper() for k in (sp.get('cards_done') or []) if str(k).strip().upper() not in s['cards']]; s['cards'] += new
    s['stall'] = 0 if (new or changed) else s['stall'] + 1
Path(sys.argv[2]).write_text(json.dumps(out, ensure_ascii=False, indent=1))
