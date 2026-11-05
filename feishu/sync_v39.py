"""把 8️⃣ 里过时的块换成按当前资料包生成的新内容（V3.9，2026-11-05）：块 id 来自 docs +fetch，内容来自 chunks/*.xml。
先跑 build_pack_xml.py。只做 block_replace，不插不删；任何失败就停，先 fetch 核对。用法：python3 sync_v39.py [只换的 id 前缀...]"""
import re, subprocess, sys
from pathlib import Path
DOC = 'G4ojwsQrDiK3gikgYHUcv7y8nQc'; D = Path(__file__).resolve().parent
C = ''.join((D / 'chunks' / f'{k}.xml').read_text(encoding='utf-8') for k in ('05', '06', '07', '08'))
def pre(cap): m = re.search(r'<pre caption="' + re.escape(cap) + r'[^"]*"[^>]*>.*?</pre>', C, re.S); assert m, cap; return m.group(0)
def table(head):
    for m in re.finditer(r'<table\b.*?</table>', C, re.S):
        if head in m.group(0)[:600]: return m.group(0)
    raise KeyError(head)
def para(start): m = re.search(r'<p>' + re.escape(start) + r'.*?</p>', C, re.S); assert m, start; return m.group(0)
def box(start): m = re.search(r'<checkbox done="[a-z]+">' + re.escape(start) + r'.*?</checkbox>', C, re.S); assert m, start; return m.group(0)
JOBS = [
 ('doxcnxDu4zb6e6gvdX2U68sJFlb', pre('世界观与背景')),
 ('doxcnpO7oBOepJKQlOnuMht4KMb', pre('性格与行为')),
 ('doxcn13IM3w9e8ralobXXynBnKb', pre('对话示例')),
 ('doxcnyA9ixKD0LB0ZPXbheo3eob', pre('当前生活环境')),
 ('doxcnkxIdc4C8gqpi9lfJfv8l40', table('形象图')),
 ('doxcnjwdWJC2TiTrdgcFCnWS3Qe', pre('故事方向')),
 ('doxcnrscL9nEcZi6Bb8xkv6bHef', pre('场景、道具连续性约束')),
 ('doxcn2Zw2yxm4w1A08cgAWnhlVb', pre('预设选项 PE')),
 ('doxcnPmN86KG4GlvUtwXqLvTxNg', pre('通用视频生成')),
 ('doxcnD2EretkD4veAt4iihuSe2n', table('需要保留的连续信息')),
 ('doxcnVsv6mndMPW2ixbVAh0qfLd', table('地点与推荐轮次')),
 ('doxcnSgyDujzTgOFQGg6nRxoDvc', para('Jasper 线的 K03')),
 ('doxcn0WqayE4aC0ZAVeOaISmHdD', pre('声音方案 PE')),
 ('doxcnKQ9EOY2Q45PtRuqctmuXxe', pre('ILA_PEAK_01')),
 ('doxcnGQqIwyHVA1XBDzFGgrc7lc', box('现有角色图')),
]
only = sys.argv[1:]
for bid, x in JOBS:
    if only and not any(bid.startswith(o) for o in only): continue
    r = subprocess.run(['lark-cli', 'docs', '+update', '--doc', DOC, '--command', 'block_replace', '--block-id', bid, '--content', '-', '--as', 'user'], input=x, capture_output=True, text=True, timeout=280)
    ok = '"result": "success"' in r.stdout or '"ok": true' in r.stdout
    print(bid, 'ok' if ok else 'FAIL', (r.stdout[:160] + r.stderr[:200]).replace('\n', ' ') if not ok else len(x), flush=True)
    if not ok: sys.exit(1)
