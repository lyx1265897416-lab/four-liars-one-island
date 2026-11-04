<h1 align="center">三真四假 · Four Liars, One Island</h1>
<p align="center">女性向第三视角开放式实时互动剧 · 恋爱真人秀</p>
<p align="center"><a href="https://lyx1265897416-lab.github.io/four-liars-one-island/">▶ 打开体验页</a></p>

七个男人上了恋爱真人秀海岛：三个是来找老婆的千万富翁，四个是为一百万奖金装富豪的骗子。选到骗子，就得跟他一起回家。

只有开场是预制的（50 秒）。开场后她选今晚的搭档（Wes 或 Jasper，或者自己打一句话），之后每一段视频都根据她点的选项或打的话实时生成。

> 不带口令打开时只能看开场。实时生成要用带口令的测试链接，并且要这台 Mac 开着：中转和模型 key 都在本机，不在仓库里。

## 组成

- 开场：`opening-v1/`（脚本，STATUS.md 有每一版的返修记录），确认版是 V2，`docs/media/OPEN.mp4`。
- 两条线：`wes/`（中转 8906）、`jasper/`（中转 8907）。每条线的 `drama_slots.py` 和 `pack/ila_pack.json` 都由 `make_lines.py` 生成；`director.py`、`live_common.py`、`qa_guard.py`、`ila_*_relay.py` 由 `tools/realtime-third/render.py` 从第三视角共用模板合成，不要手改。
- 母版：`masters_build.py gen | upload`，每条线的地址在 `<线>/masters/urls.json`（不进仓库）。
- 播放页：`docs/index.html`（`build_site.py` 传 CDN、写开场字幕）；`docs/relay.json` 由 `sync_relay.py` 自动更新两条线的隧道地址。
- launchd：`com.vicky.realtime.ila-wes`、`ila-jasper`、`ila-wes-tunnel`、`ila-jasper-tunnel`、`ila-sync`。
