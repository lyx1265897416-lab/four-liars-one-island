"""导演层连跑（不花视频钱）：从开场后的第一个选择开始，每轮点 A，跑 N 轮，看每轮的拍数、台词数、news、he_move、选项和耗时。用法：python3 tests/dry_chain.py wes|jasper [轮数]"""
import json, sys, time
from pathlib import Path
LINE = sys.argv[1]; N = int(sys.argv[2]) if len(sys.argv) > 2 else 4; D = Path(__file__).resolve().parent.parent / LINE; sys.path.insert(0, str(D))
import director
src = next(D.glob('ila_*_relay.py')).read_text(encoding='utf-8'); OPEN_STATE = OPEN_NEXT = None
exec(src[src.index('OPEN_STATE ='):src.index('OPEN_NEXT =')]); exec('OPEN_NEXT =' + src.split('OPEN_NEXT =', 1)[1].split('\n\n', 1)[0])
s = dict(history=[], state=OPEN_STATE, place='篝火露台', place_rounds=0, cards=[], stall=0, set=director.OPEN_SET, wardrobe={})
text, kind = OPEN_NEXT['A']['zh'], 'option'
out = []
for n in range(1, N + 1):
    t0 = time.time()
    sp, sec = director.direct(list(s['history']), s['state'], text, kind, 'auto', place=s['place'], place_rounds=s['place_rounds'], done=tuple(s['cards']), stall=s['stall'], set_now=s['set'], wardrobe=dict(s['wardrobe']), cont={'posture': '', 'holding': '', 'looks': {}, 'items': [], 'left': {}, 'outfits': []})
    lines = [b[1] for k in ('seg1', 'seg2') for b in sp.get(k, []) if len(b) > 1 and b[1]]
    print(f"\n### R{n} [{kind}] {text} | {sec}s try={sp.get('director_attempts')} {sp.get('dur_mode')} beats={len(sp.get('seg1', []))}+{len(sp.get('seg2', []))} lines={len(lines)} loc={sp.get('location')} cards_done={sp.get('cards_done')}")
    print('  he_move', sp.get('he_move')); print('  news', sp.get('news'))
    for k in ('seg1', 'seg2'):
        for b in sp.get(k) or []: print('   ', k[-1], str(b[2])[:10], '|', str(b[0])[:80], '|', str(b[1])[:60], '|', (b[3] if len(b) > 3 else ''))
    nx = sp.get('next') or {}; print('  A', (nx.get('A') or {}).get('zh'), '| B', (nx.get('B') or {}).get('zh')); print('  lint_left', [x[:60] for x in sp.get('lint_left') or []][:3], flush=True)
    out.append(dict(n=n, text=text, sec=sec, sp=sp))
    s['history'].append({'input': text, 'kind': kind, 'lines': [b[1] for b in sp['seg1']] + [b[1] for b in sp['seg2']], 'did': sp.get('did'), 'ask': sp.get('ask'), 'delivered': bool(sp.get('delivered')), 'hook_type': sp.get('hook_type'),
                         'reveal': sp.get('reveal') or [], 'intimacy': sp.get('intimacy') or 0, 'place': sp.get('location'), 'set': sp.get('set'), 'extras': sp.get('extras') or [], 'input_type': sp.get('input_type'), 'kiss': bool(sp.get('kiss')), 'staging': sp.get('staging'), 'opts': [((sp.get('next') or {}).get(k) or {}).get('zh', '') for k in ('A', 'B')]})
    changed = bool(sp.get('scene_changed')); s['state'] = sp.get('state') or s['state']; s['place'] = sp.get('location') or s['place']; s['place_rounds'] = 0 if changed else s['place_rounds'] + 1
    if changed: s['set'] = sp.get('set') or s['set']
    s['wardrobe'] = sp.get('wardrobe_end') or {}
    new = [str(k).strip().upper() for k in (sp.get('cards_done') or []) if str(k).strip().upper() not in s['cards']]; s['cards'] += new
    s['stall'] = 0 if (new or changed) else s['stall'] + 1
    text = (nx.get('A') or {}).get('zh') or text
(Path(__file__).parent / f'dry_chain_{LINE}.json').write_text(json.dumps(out, ensure_ascii=False, indent=1))
