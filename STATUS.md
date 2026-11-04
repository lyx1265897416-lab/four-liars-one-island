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

## 封面 V2（2026-11-03，Vicky：把最帅的男主放中间）
- opening-v1/cover.py 出 3 张（Jasper 居中靠前、六人 V 字排在两侧、脸在上半、下半留给标题），选 COVER_2（最正中、七人都认得出）→ docs/media/poster.jpg（?v=2）；旧封面在 opening-v1/qa/rejected/poster-v1-lineup.jpg。
- 飞书 8️⃣ 封面图同步换成 cover-v2.jpg（realtime-drama-test-log v/ila-pack/）。

## 海报版封面（2026-11-03，Vicky：改成海报，女主 C 位，可加别的女生做对比，男生随机排列）
- opening-v1/poster.py：P1 只有她、P2 她 + Sloane、P3 她 + Sloane + Mei、P4 她 + Sloane + 两位新女嘉宾（黑色波波头祖母绿缎裙、红棕长卷发白色钩花短裙，未定装）。男生顺序按固定种子随机。每版一张带片名（FOUR LIARS, ONE ISLAND + 宣传语）、一张无字版（播放页用）。
- 对比板 ../casting/poster_v1.jpg。返修：P2 带字版她的左臂发白、P4 带字版 Sloane 穿成白色上衣 → 各重出一张，旧图在 opening-v1/qa/rejected/poster/。
- 等她选；选定后无字版进 docs/media/poster.jpg（?v=3）、带字版进飞书 8️⃣ 封面。播放页现在还是封面 V2（Jasper 居中）。
- 11-03 Vicky 选 P1（只有她，C 位）：无字版 → docs/media/poster.jpg（?v=3，已上线）；带字版 → 飞书 8️⃣ 封面 cover-v3.jpg。确认版存 casting/poster_P1_确认版.png、poster_P1_确认版_无字.png；封面 V2 存 opening-v1/qa/rejected/poster-v2-jasper.jpg。

## V3.0 复盘修正（2026-11-04，Vicky 测 Jasper 线 S231920f01 5 轮：节奏慢、内容少、男主被动、生成慢、第 5 轮报错）
- 复盘（tests/review/S231920f01/）：每 15 秒 2–4 句台词，大半是表情拍，第 3 轮第 1 段躺着 15 秒几乎不动；Jasper 用“Ask me tomorrow”拖；换场空镜空等；R1 卡片凭空出现、R4 套房中途换了样子、桨板穿模；R5 第 2 段开播前检查把 Sloane 的蓝裙当女主裙子变色，连拦三次后报错（143 秒）。
- 共用模板 → 第三视角 V3.0（tools/realtime-third，备份 backup-v29，skill D43，飞书 PE 已推）：台词加密（15 秒段 3–5 句）、表情拍整轮最多一拍、拖延台词打回、选项 2–3 步（14–36 字）、空镜 1 秒可带画外台词、提示词加节奏句；第 1 段里的配角由代码挪到第 2 段（换场时改画外声音）、同拍两个配角打回；开播前检查每秒 1 帧、320 宽、给每个人一句外形；地点空景 plates（urls.json）当换场参考。其他三部第三视角剧还没重启，重启后才用 V3.0（隔离副本已验证能合成、能编译）。
- 本剧（make_lines.py）：挑战改沙滩夺旗、套房样子写死、两位男主没有外套、配角一个一个拍且一轮最多两位、道具不凭空出现、夜景天空全黑；男主人设写明怎么主动推进；节奏目标加快（约 9 轮到最终仪式）。配角母版改单人定装图（两格合图会画出两个 Sloane、两个 Mei）；六个地点空景 masters/plate-*.jpg。补了缺的 dissolve.py（段内快检一直报 No module）。
- 实测：Jasper S000923768 3 轮、Wes S001455553 2 轮、Wes S002346f4c 2 轮全部成功，无误报重生成；台词 6–9 句/轮；开播前检查 5–8 秒（原 6–23）；导演层之后第 1 段 27–52 秒、第 2 段 46–67 秒出片（原第 2 段 62–143 秒、一轮报错）。冒烟脚本点得快、预写没完成，导演层还多等 16–43 秒；真人看完一轮再点时这段被预写盖住。
- 还剩：第 1 段 15 秒首帧续接里夜空有时会慢慢变成黄昏（模型漂移）；套房偶尔多一幅画；她手里偶尔多出道具。

## V3.1 等待时间排查（2026-11-04，Vicky：两段 15 秒不应该同时生成吗，等待太久）
- Vivix 实测（tests/vivix_probe.py，结果在 tests/vivix-probe/）：同一工作区两条 ultrafast 同时交是串行的（第 2 条在第 1 条出片时才开工）；ultrafast + fast、ultrafast + 标准 w1 能同时跑，但 fast/w1 的 15 秒段 33–37 秒，比串行还慢；a1、stream 档账号没开。HLS 能边生成边出片（ultrafast 约 3 倍实时），暂未用（开播前检查要整段）。
- 主因在开播逻辑：她测的那局第 1 段早好了也干等，开播只比第 2 段出片早 0–1 秒。第 2 段排队时 eta 估得太大（按马上开工 + 13 秒检查余量）。改：relay 的 seg_eta 串行估，检查余量 13→11 秒。今天 24 轮回放开播中位早约 14 秒；实测预写命中的轮次发送→开播 40.7、41.6、48.5 秒（原来 62–66 秒）。
- 有配角在画面时，只报衣服颜色的检查不再重生成（都是把 Sloane 的蓝裙当成女主的）。
- 检查本身：要先把 6–9 MB 的 mp4 从 Vivix 拉到本机（1.4–7.8 秒），再问模型（5–17 秒）。
- 根治：第二个 Vivix 工作区（或让 Vivix 把这个工作区开到 2 条并发）。relay 已支持，在 ~/.config/vicky-realtime/env 加 VIVIX_API_KEY_2，kickstart 两个中转即可；预计导演层之后约 25–28 秒开播。
- 偶发：一条任务在 Vivix 排队 129 秒不开工（另一条照常跑），没做重提。
