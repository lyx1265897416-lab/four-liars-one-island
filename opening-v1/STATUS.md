# 《三真四假》开场 V1（2026-11-03）· 待 Vicky 确认，未进资料包，实时版未搭

- 选角 V3（../casting/cast_v3.jpg），全部取自角色库；定装 costume/costume-*.png（白底全身正面，gpt-image-2/edit 从库图出），总览 ../casting/costume_v1.jpg。服装文字在 cast.py。
- 做法照 meet-me-third 确认版开场（V12A）：Seedance 2.5 image-to-video 原生演出（720p、原声），对白近景单人、视线贴镜头一侧、画边一缕对方虚焦；每镜留原生音；对白开口前静音、轻度降噪；amix normalize=0。
- 脚本：cast.py（选角和定装）、shots.py（空镜、13 镜首帧和视频提示词）、gen.py costume|plates|frames|native、words.py（本地 faster-whisper 词时间，用 asr-env 解释器）、gen_sound.py（环境声、配乐、音效）、edit.py（合成，分轨在 edit/）。
- 交付 delivery/ILA_OPENING_V1.mp4 + .zh-en.vtt + cues-V1.json，字幕不烧进画面。

首帧返修：S02 Brody 站在火上 → 写明篝火在队列后方几米（qa/rejected/S02-overfire.png）；S12 她手里的酒换成了橙色鸡尾酒加兰花 → 加 S09 首帧做参考（qa/rejected/S12-wrongdrink.png）。

确认后：两份 drama_slots.py（Wes、Jasper 各一份，接 tools/realtime-third）、资料包（真相代码抽定）、两场仪式和两种结局预制、实时母版（face_head、her_head）、中转和嫌疑板页面、中英测试链接。

## V1 交付（2026-11-03）
- delivery/ILA_OPENING_V1.mp4（49.6 秒 · 720×1280 · 24fps · -15.8 LUFS）+ ILA_OPENING_V1.zh-en.vtt + cues-V1.json。
- 自查：12 个切点逐一看过无跳变；成片转写台词全对、无多余人声；她在 S07/S09/S12 脸一致，S09→S12 酒杯一致；七人队列服装与定装一致。
- S01 原生音里有一句莫名人声（2.32 秒起），取用窗口截到 2.25 秒。转写把 S03/S04/S11/S13 开口判在 0 秒，按能量改（edit.py ONSET）。
- 还没做：调色统一（目前各镜色调已接近，未跑 grade）、动作音效（原生音已有呼吸和脚步）。

## 主持人换人（2026-11-03，Vicky：Mei 换一个形象，外国人优先但要有点亚裔感，可选可生成一批）
- 候选 costume/host-H1…H6（新生成，约 38–45 岁欧亚混血）、host-L1、L2（库里 white-portraits-24 #04、front-id-32 #14，较年轻）；脚本 host_cands.py；脸部拼板 ../casting/host_faces_v1.jpg，全身 ../casting/host_v1.jpg。
- L1 多了一条项链（定装只写了珍珠耳钉），选它的话要重出。
- 她选定后：换 cast.py 的 mei，重出 S03/S04/S13 首帧和视频，重剪 V2。

## V2（2026-11-03，Vicky 选主持人 H1）
- delivery/ILA_OPENING_V2.mp4（50.0 秒，-15.5 LUFS）+ .zh-en.vtt + cues-V2.json。只换 Mei 三镜（S03/S04/S13），其余镜头同 V1。
- Mei 身份参考 costume/mei-face.png（由 host-H1 出的白底头肩像），定装 costume/costume-mei.png = host-H1；旧 Mei 素材在 qa/rejected/mei-v1/。
- 返修：S04 首帧第一次蹲坐露膝 → 写明站立胸像；S03 第一条把 men 念成 twists（两个转写模型都听到）→ 同首帧重拍。
- S04 这条镜头在台词里缓慢推近到大特写、最后眨眼，没有跳切，保留。
- edit.py 开口时间：转写判 0 秒时自动按能量找（不再手写 ONSET）。
