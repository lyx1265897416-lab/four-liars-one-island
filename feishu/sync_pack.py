"""把 8️⃣ 里会随资料包变化的块换成 build_pack_xml.py 新生成的内容。块按代码块标题、表头文字在 8️⃣ 这一节里现找（block_replace 后 id 会变，不写死）。
先跑 build_pack_xml.py。只做 block_replace，不插不删；任何失败就停，先 fetch 核对。用法：python3 sync_pack.py"""
import re, subprocess, sys
from pathlib import Path
DOC = 'G4ojwsQrDiK3gikgYHUcv7y8nQc'; D = Path(__file__).resolve().parent
C = ''.join((D / 'chunks' / f'{k}.xml').read_text(encoding='utf-8') for k in ('05', '06', '07', '08'))
PRES = ['世界观与背景', '自我看法和优先事项', '性格与行为', '对话示例', '当前生活环境', '故事方向', '场景、道具连续性约束', '预设选项 PE', '通用视频生成', '声音方案 PE', 'ILA_PEAK_01']
TABLES = ['形象图', '需要保留的连续信息', '地点与推荐轮次']
def cli(*a):
    r = subprocess.run(['lark-cli', *a, '--as', 'user'], capture_output=True, text=True, timeout=280); return r.stdout + r.stderr
sec = cli('docs', '+fetch', '--doc', DOC, '--detail', 'with-ids').replace('\\"', '"'); sec = sec[sec.index('8️⃣ 三真四假'):]
def new_pre(cap): m = re.search(r'<pre caption="' + re.escape(cap) + r'[^"]*"[^>]*>.*?</pre>', C, re.S); return m.group(0)
def new_table(head): return next(m.group(0) for m in re.finditer(r'<table\b.*?</table>', C, re.S) if head in m.group(0)[:600])
def old_pre(cap): ids = re.findall(r'<pre id="([^"]+)" caption="' + re.escape(cap), sec); assert len(ids) == 1, (cap, ids); return ids[0]
def old_table(head):
    ids = [m.group(1) for m in re.finditer(r'<table id="([^"]+)"', sec) if head in sec[m.end():m.end() + 900]]; assert len(ids) == 1, (head, ids); return ids[0]
jobs = [(old_pre(c), new_pre(c), c) for c in PRES] + [(old_table(h), new_table(h), h) for h in TABLES]
for bid, x, name in jobs:
    out = cli('docs', '+update', '--doc', DOC, '--command', 'block_replace', '--block-id', bid, '--content', x)
    ok = '"result": "success"' in out or '"ok": true' in out
    print(name, bid, 'ok' if ok else 'FAIL ' + out[:200], flush=True)
    if not ok: sys.exit(1)
