# -*- coding: utf-8 -*-
"""合成开场：对白镜头按转写词时间取窗（开口前留 lead、说完留 tail），其余按 take 窗口；每镜留原生音（Seedance 原声）。
分轨 edit/dialogue.wav、ambience.wav、sfx.wav、bgm.wav；字幕不烧进画面，出 zh-en VTT。用法：python3 edit.py [版本号]"""
import json, subprocess, sys
from pathlib import Path
import numpy as np
V = Path(__file__).resolve().parent
sys.path.insert(0, str(V))
from shots import SHOTS
TAG = sys.argv[1] if len(sys.argv) > 1 else 'V1'
FF = '/Users/vicky/Interactive storyline/.media-runtime/imageio_ffmpeg/binaries/ffmpeg-macos-aarch64-v7.1'
WORDS = json.load(open(V / 'qa/native_words.json'))
LEAD, TAIL = {}, {'S04': .45, 'S11': 1.4, 'S13': .8}  # S11 留他转身上楼；S13 留 Mei 的笑
def energy_onset(src):  # 转写常把开口误判在 0 秒（同 meet-me V9）：按能量找第一个超过峰值 25% 的 50ms 窗
    q = subprocess.run([FF, '-v', 'error', '-i', src, '-ac', '1', '-ar', '16000', '-f', 'f32le', '-'], capture_output=True).stdout
    a = np.frombuffer(q, np.float32); r = np.sqrt((a[:len(a) // 800 * 800].reshape(-1, 800) ** 2).mean(1))
    return round(float(np.argmax(r > max(r.max() * .25, .01)) * .05), 2)
E = V / 'edit'; E.mkdir(exist_ok=True)
def ff(*a): subprocess.run([FF, '-y', '-v', 'error', *map(str, a)], check=True)
SC = 'scale=720:1280:force_original_aspect_ratio=increase:flags=lanczos,crop=720:1280,fps=24,'
ENC = ['-c:v', 'libx264', '-preset', 'slow', '-crf', 17, '-bf', 0, '-r', 24]
parts, t, cues, dlg, wins = [], 0.0, [], [], {}
for s in SHOTS:
    k = s['key']; src = V / 'takes' / f'{k}.mp4'
    if s['lines']:
        w = [list(x) for x in WORDS[k]['words']]; w[0][1] = energy_onset(src) if w[0][1] < .1 else w[0][1]; a = max(0, w[0][1] - LEAD.get(k, .3)); b = min(WORDS[k]['dur'] - .05, w[-1][2] + TAIL.get(k, .35))
    else:
        a, b = s['take'] or (0, s['dur'])
    nf = round((b - a) * 24); dur = nf / 24; o = E / f'{k}.mp4'
    ff('-i', src, '-an', '-vf', SC + f'trim=start_frame={round(a*24)},setpts=PTS-STARTPTS,tpad=stop_mode=clone:stop=4,setsar=1,format=yuv420p', '-frames:v', nf, *ENC, o)
    parts.append(o); wins[k] = (a, t)
    gate = max(0, w[0][1] - a - .12) if s['lines'] else 0
    dlg.append((src, a, dur, t, 1.0, gate))
    if s['lines']:
        c, en, zh = s['lines'][0]
        cues.append(dict(s=round(t + w[0][1] - a, 2), e=round(t + w[-1][2] - a, 2), who=c, en=en, zh=zh))
    t += dur
TOTAL = t
ff(*sum([['-i', p] for p in parts], []), '-filter_complex', ''.join(f'[{i}:v]' for i in range(len(parts))) + f'concat=n={len(parts)}:v=1:a=0,fps=24[v]', '-map', '[v]', '-c:v', 'libx264', '-preset', 'slow', '-crf', 16, '-pix_fmt', 'yuv420p', '-bf', 0, E / 'video.mp4')
def bed(items, out):  # amix normalize=0：不然片段结束后增益会抬高
    a = ['-f', 'lavfi', '-t', TOTAL, '-i', 'anullsrc=r=48000:cl=stereo']; ch = []; lb = ['[0:a]']
    for i, (p, at, gain) in enumerate(items, 1):
        a += ['-i', p]; ch.append(f'[{i}:a]aresample=48000,volume={gain}dB,adelay={int(at*1000)}|{int(at*1000)}[d{i}]'); lb.append(f'[d{i}]')
    ff(*a, '-filter_complex', ';'.join(ch + [''.join(lb) + f'amix=inputs={len(lb)}:duration=first:normalize=0[o]']), '-map', '[o]', '-ac', 2, '-ar', 48000, out)
segs = []
for i, (p, a, d, at, g, gate) in enumerate(dlg):  # 对白镜头开口前静音，全部原生轨轻度降噪
    fade = f'afade=t=in:st={gate:.3f}:d=0.08' if gate else 'afade=t=in:d=0.02'
    o = E / f'dlg{i}.wav'; ff('-ss', a, '-t', d, '-i', p, '-vn', '-af', f'afftdn=nf=-30,volume={g},{fade},afade=t=out:st={d-.04:.3f}:d=0.04', '-ac', 2, '-ar', 48000, o); segs.append((o, at, 0))
bed(segs, E / 'dialogue.wav')
S = V / 'sound'
ff('-stream_loop', -1, '-i', S / 'amb.mp3', '-t', TOTAL, '-af', f'aresample=48000,volume=-16dB,afade=t=in:st=0:d=1,afade=t=out:st={TOTAL-1.2:.2f}:d=1.2', '-ac', 2, E / 'ambience.wav')
def peak_gain(f, peak):
    q = subprocess.run([FF, '-v', 'error', '-i', f, '-ac', '1', '-f', 'f32le', '-'], capture_output=True).stdout
    return round(float(20 * np.log10(peak / max(1e-4, float(np.abs(np.frombuffer(q, np.float32)).max())))), 1)
def at(k, src_t): return wins[k][1] + src_t - wins[k][0]
def end_of_line(k): return at(k, WORDS[k]['words'][-1][2])
BEATS = [(S / 'fx/sting.mp3', end_of_line('S04') + .05, peak_gain(S / 'fx/sting.mp3', .35)),
         (S / 'fx/whoosh.mp3', wins['S02'][1] - .15, peak_gain(S / 'fx/whoosh.mp3', .18)),
         (S / 'fx/sting.mp3', end_of_line('S13') + .05, peak_gain(S / 'fx/sting.mp3', .3))]
bed(BEATS, E / 'sfx.wav')
ff('-i', S / 'bgm.mp3', '-t', TOTAL, '-af', f'aresample=48000,volume=-19dB,afade=t=in:st=0:d=1.5,afade=t=out:st={TOTAL-2.5:.2f}:d=2.5', '-ac', 2, E / 'bgm.wav')
out = V / f'delivery/ILA_OPENING_{TAG}.mp4'
ff('-i', E / 'video.mp4', '-i', E / 'dialogue.wav', '-i', E / 'ambience.wav', '-i', E / 'sfx.wav', '-i', E / 'bgm.wav', '-filter_complex',
   '[4:a][1:a]sidechaincompress=threshold=0.03:ratio=8:attack=25:release=500[b];[1:a][2:a][3:a][b]amix=inputs=4:duration=first:normalize=0,loudnorm=I=-16:TP=-1.5:LRA=11[a]',
   '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', 48000, '-movflags', '+faststart', out)
def ts(x): return '%02d:%02d:%06.3f' % (x // 3600, x // 60 % 60, x % 60)
(V / f'delivery/ILA_OPENING_{TAG}.zh-en.vtt').write_text('WEBVTT\n\n' + ''.join(f"{ts(c['s'])} --> {ts(c['e'])}\n{c['zh']}\n{c['en']}\n\n" for c in cues))
(V / f'delivery/cues-{TAG}.json').write_text(json.dumps(dict(total=round(TOTAL, 3), shots={k: round(v[1], 3) for k, v in wins.items()}, cues=cues), ensure_ascii=False, indent=1))
print('TOTAL', round(TOTAL, 2), {k: round(v[1], 2) for k, v in wins.items()})
