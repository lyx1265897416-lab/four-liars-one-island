# -*- coding: utf-8 -*-
"""本地 faster-whisper 转写对白镜头（不走 waku transcribe，那个每次 252 credits）→ qa/native_words.json。
用法：~/Documents/waku内容/off-script/tools/asr-env/bin/python words.py [key..]"""
import json, sys, glob, os, subprocess, tempfile
from pathlib import Path
from faster_whisper import WhisperModel
V = Path(__file__).resolve().parent
FF = '/Users/vicky/Interactive storyline/.media-runtime/imageio_ffmpeg/binaries/ffmpeg-macos-aarch64-v7.1'
M = WhisperModel(glob.glob(os.path.expanduser('~/.cache/huggingface/hub/models--Systran--faster-whisper-small.en/snapshots/*'))[0], compute_type='int8')
out = V / 'qa' / 'native_words.json'
W = json.loads(out.read_text()) if out.exists() else {}
for mp4 in sorted((V / 'takes').glob('S*.mp4')):
    k = mp4.stem
    if sys.argv[1:] and k not in sys.argv[1:]: continue
    wav = Path(tempfile.mkdtemp()) / 'a.wav'
    subprocess.run([FF, '-v', 'error', '-y', '-i', str(mp4), '-ac', '1', '-ar', '16000', str(wav)], check=True)
    dur = float(subprocess.run([FF, '-i', str(mp4)], capture_output=True, text=True).stderr.split('Duration: ')[1].split(',')[0].split(':')[-1])
    segs, _ = M.transcribe(str(wav), word_timestamps=True, language='en')
    words = [[w.word.strip(), round(w.start, 2), round(w.end, 2)] for s in segs for w in s.words]
    W[k] = dict(dur=dur, text=' '.join(w[0] for w in words), words=words)
    print(k, round(dur, 2), W[k]['text'])
out.write_text(json.dumps(W, ensure_ascii=False, indent=1))
