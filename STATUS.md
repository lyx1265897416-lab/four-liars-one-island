# 《三真四假 Four Liars, One Island》第三视角实时版（2026-11-03）

开场 = 确认版 V2（opening-v1/delivery/ILA_OPENING_确认版.mp4，50 秒，Vicky 11-03 确认），播完停在 Mei 举卡的近景（docs/media/IDLE0.mp4，末帧缓推循环）。之后全部实时。

- 两条线：wes/（中转 ila_wes_relay.py 8906）、jasper/（ila_jasper_relay.py 8907）。drama_slots.py 和 pack/ila_pack.json 由 make_lines.py 生成（以 meet-me-third 的 slots 为底改写）；director/live_common/qa_guard/relay 由 tools/realtime-third/render.py 合成，不手改。
- 真相（每条线固定，在资料包和编剧 PE 里）：真富豪 Jasper、Ethan、Kian；骗子 Wes、Brody、Jude、Ravi。改编方案里的“每局代码抽定”还没做。
- 母版 masters_build.py gen|upload：站位图、第 1 轮关键帧（午夜篝火边男左女右）各线一张，其余共用；配角 Mei、Sloane、另一位男主、Ethan、Brody 是“头像 + 定装”合图。地址 <线>/masters/urls.json（不进仓库）。
- 播放页 docs/index.html：开场后第一个选择点是页面自己的（我选 Wes／我选 Jasper），选了谁就在谁的中转上开会话并发选项 A；自由输入提到 Jasper／楼梯／天台走 Jasper 线，其余走 Wes 线。relay.json = {wes, jasper}，sync_relay.py 自动更新。
- launchd：com.vicky.realtime.ila-wes、ila-jasper、ila-wes-tunnel、ila-jasper-tunnel、ila-sync（tools/realtime-relays/run.sh 里加了这五项，备份 run.sh.before-ila）。口令在 wes/token.txt（两条线同一个），不进仓库。
- 公开仓库 lyx1265897416-lab/four-liars-one-island，Pages https://lyx1265897416-lab.github.io/four-liars-one-island/ （带 ?k=口令&lang=zh|en 才能实时生成）。
- 飞书「角色样例」8️⃣ 三真四假（脚本 feishu/：prep_images.py 配图推 realtime-drama-test-log v/ila-pack/，build_pack_xml.py → chunks，write.py 插在 7️⃣ 末尾，media.py 插视频音频和压缩包）。社交关系网表格的 4 张头像第一次没写进去，已补插。

## 测试（2026-11-03，模拟，Vicky 还没人工测）
- 导演层干跑 tests/dry_open.py wes|jasper：开场后 A、B、自由输入都对，Jasper 线自己埋了“手上有茧”的线索。
- 本机冒烟 tests/smoke.py：Wes 2 轮（S201309b0f）、Jasper 1 轮（S20130978a），全部 15+15，两段生成完 125–166 秒。人物、服装、配角（Sloane、Mei、另一位男主）和母版一致。问题：Wes 第 1 轮第 1 段开头一个过肩镜左右对调；Wes 第 2 轮换场到套房，第 2 段中途回到泳池边。
- Pages 线上 1 轮（自由输入“配对前，我先上天台找他要那句实话” → 正确走 Jasper 线，到了天台）：导演层 42.9 秒，第 1 段 108.5 秒、第 2 段 129.9 秒出片；浏览器窗格隐藏时测的开播 228.8 秒、接缝停 9.2 秒，不可信。
- 慢：auto 几乎都选 15+15，比别的第三视角剧（约 55 秒）慢一倍。

## 待做
Vicky 人工测后复盘；时延（考虑默认 5+15）；嫌疑板页面、预制仪式和结局、每局抽真相；测试记录页、即兴剧场 APP。
