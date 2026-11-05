"""导演层对照（Sonnet 5.5 vs Opus 5.5，OpenRouter 拒绝 Anthropic 期间经本机 Claude Code 调用）：同一组输入跑 N 轮，记每轮耗时、打回次数、遗留问题和整份 spec。
用法：python3 tests/cli_director.py <模型：claude-sonnet-5-5 | claude-opus-5-5 | openrouter:<id>> <线 jasper|wes> <输出 json> <输入序列，逗号分隔，A/B 是点选项>"""
import json, os, subprocess, sys, tempfile, time
from pathlib import Path
MODEL, LINE, OUT, PLAN = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4].split(',')
D = Path(__file__).resolve().parent.parent / LINE; sys.path.insert(0, str(D))
import director
CALLS = []
if MODEL.startswith('openrouter:'):
    director.MODEL = director.FALLBACK_MODEL = MODEL.split(':', 1)[1]
else:
    def _cli(msgs, timeout, model=None):
        sysm = msgs[0]['content']; sysm = ''.join(x['text'] for x in sysm) if isinstance(sysm, list) else sysm
        conv = msgs[1:]; prompt = conv[0]['content']
        for k in range(1, len(conv), 2):  # 打回重写：把上一次输出和要改的地方接在后面
            prompt += '\n\n【你上一次输出的 JSON】\n' + conv[k]['content'] + '\n\n【要改】\n' + conv[k + 1]['content']
        with tempfile.NamedTemporaryFile('w', suffix='.txt', delete=False) as f: f.write(sysm); sp = f.name
        env = {k: v for k, v in os.environ.items() if k != 'ANTHROPIC_BASE_URL'}
        t0 = time.time()
        r = subprocess.run(['claude', '-p', '--model', MODEL, '--system-prompt-file', sp, '--tools', '', '--output-format', 'json', '--no-session-persistence',
                            '--strict-mcp-config', '--effort', 'low', prompt], capture_output=True, text=True, timeout=600, env=env, cwd=tempfile.gettempdir())
        os.unlink(sp)
        j = json.loads(r.stdout); txt = j.get('result') or ''
        CALLS.append({'sec': round(time.time() - t0, 1), 'api_ms': j.get('duration_api_ms'), 'cost': j.get('total_cost_usd'), 'out_tokens': (j.get('usage') or {}).get('output_tokens')})
        i = txt.find('{')
        if i < 0: raise ValueError('没有返回 JSON：' + txt[:200])
        obj, _ = json.JSONDecoder().raw_decode(txt[i:])
        return obj, txt, {'model': MODEL}
    director._call = _cli
src = next(D.glob('ila_*_relay.py')).read_text(encoding='utf-8'); OPEN_STATE = OPEN_NEXT = None
exec(src[src.index('OPEN_STATE ='):src.index('OPEN_NEXT =')]); exec('OPEN_NEXT =' + src.split('OPEN_NEXT =', 1)[1].split('\n\n', 1)[0])
s = dict(history=[], state=OPEN_STATE, place='篝火露台', place_rounds=0, cards=[], stall=0, set=director.OPEN_SET, wardrobe={}); nx = OPEN_NEXT; out = []
for n, inp in enumerate(PLAN, 1):
    kind = 'option' if inp in ('A', 'B') else 'free'; text = (nx.get(inp) or {}).get('zh') if kind == 'option' else inp
    c0 = len(CALLS); t0 = time.time()
    try: sp, sec = director.direct(list(s['history']), s['state'], text, kind, 'auto', place=s['place'], place_rounds=s['place_rounds'], done=tuple(s['cards']), stall=s['stall'], set_now=s['set'], wardrobe=dict(s['wardrobe']), cont={'posture': '', 'holding': '', 'looks': {}, 'items': [], 'left': {}, 'outfits': []})
    except Exception as e: out.append(dict(n=n, text=text, err=repr(e)[:300], sec=round(time.time() - t0, 1))); print('ERR', n, e, flush=True); break
    out.append(dict(n=n, text=text, kind=kind, sec=round(time.time() - t0, 1), calls=CALLS[c0:], sp=sp)); print(MODEL, 'R', n, round(time.time() - t0, 1), 's', flush=True)
    s['history'].append({'input': text, 'kind': kind, 'lines': [b[1] for b in sp['seg1']] + [b[1] for b in sp['seg2']], 'did': sp.get('did'), 'ask': sp.get('ask'), 'delivered': bool(sp.get('delivered')), 'hook_type': sp.get('hook_type'),
                         'reveal': sp.get('reveal') or [], 'intimacy': sp.get('intimacy') or 0, 'place': sp.get('location'), 'set': sp.get('set'), 'extras': sp.get('extras') or [], 'input_type': sp.get('input_type'), 'kiss': bool(sp.get('kiss')), 'surprise': bool(sp.get('surprise')), 'staging': sp.get('staging'),
                         'pending': sp.get('pending_move') if isinstance(sp.get('pending_move'), dict) else {}, 'closed': str(sp.get('closed') or ''), 'opts': [((sp.get('next') or {}).get(k) or {}).get('zh', '') for k in ('A', 'B')]})
    changed = bool(sp.get('scene_changed')); s['state'] = sp.get('state') or s['state']; s['place'] = sp.get('location') or s['place']; s['place_rounds'] = 0 if changed else s['place_rounds'] + 1
    if changed: s['set'] = sp.get('set') or s['set']
    s['wardrobe'] = sp.get('wardrobe_end') or {}
    new = [str(k).strip().upper() for k in (sp.get('cards_done') or []) if str(k).strip().upper() not in s['cards']]; s['cards'] += new
    s['stall'] = 0 if (new or changed) else s['stall'] + 1
    nx = sp.get('next') or nx
    Path(OUT).write_text(json.dumps(out, ensure_ascii=False, indent=1))
Path(OUT).write_text(json.dumps(out, ensure_ascii=False, indent=1))
