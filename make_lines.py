# -*- coding: utf-8 -*-
"""《三真四假》两条男主线（Wes / Jasper）的资料包和 drama_slots.py。
以 meet-me-third 的 drama_slots.py 为底（第三视角共用模板的槽位），把人物、地点、服装、时间、真相换成本剧；规则不在这里，在 tools/realtime-third/templates。
改人物地点、真相、K 卡改这里，然后：python3 make_lines.py && python3 ../../tools/realtime-third/render.py wes && ... jasper"""
import importlib.util, json, pprint
from pathlib import Path
D = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('mma', '/Users/vicky/Interactive storyline/output/meet-me-third-live-v1/drama_slots.py')
mma = importlib.util.module_from_spec(spec); spec.loader.exec_module(mma)

# ---------------- 人物（外形以 opening-v1/costume 定装为准） ----------------
HER = ('她：二十六岁的成年女人，暖棕色皮肤，柔和的鹅蛋脸，深棕色眼睛，饱满的嘴唇，不显幼态；很长的栗棕色中分直发；耳垂上一对小金圈耳环；'
       '香槟金缎面细吊带垂坠领中长裙（斜裁到小腿中部，缎面有光泽），裸色细带平底凉鞋；指甲短而圆、裸色素甲，不戴项链、戒指、手链。'
       '她的长相、发型和服装全程不变，严格以她的身份母版（正面头像、全身正面、近景特写）为准。她的表情自然，带一点不买账的冷幽默，情绪在眼神里。')
HER_FP = '她的手外形全程固定：纤细的暖棕肤色女性双手，指甲短而圆、裸色素甲，手指和手腕上空无一物。'
HER_LOCK_EN = ('Her hair is very long, straight and chestnut-brown with a centre part; small gold hoop earrings; warm tan skin and dark brown eyes. She wears a champagne-gold satin slip midi dress with thin spaghetti straps '
               'and a soft cowl neckline, bias-cut to mid-calf, and nude strappy flat sandals. Short rounded nude nails, no necklace, no rings, no bracelet.')
CASTD = {
    'Mei': ('Mei：四十二岁女人，节目主持人，欧亚混血，浅橄榄色皮肤，淡褐色的内双杏眼，高颧骨，利落的下颌，齐下巴的乌黑侧分波波头，红棕色口红，小珍珠耳钉；象牙白单扣西装连衣裙，裸色尖头高跟鞋，手里常拿一张素面奶油色卡片。长相和衣着以她的身份母版为准。', 'mei'),
    'Sloane': ('Sloane：二十六岁女人，女嘉宾、她的对手，白皙皮肤，蓝灰色眼睛，很长的蓬松金色波浪长发带空气刘海；电光蓝缎面挂脖短裙，银色细带高跟凉鞋，小银色垂坠耳环，淡粉色长杏仁形指甲。长相和衣着以她的身份母版为准。', 'sloane'),
    'Wes': ('Wes：二十八岁男人，男嘉宾，蓬松的深金色头发，灰绿色眼睛，浅麦色皮肤；浅天蓝亚麻衬衫（袖子卷起、领口敞开、不塞），石米色亚麻长裤，棕色麂皮乐福鞋，左腕一条细棕皮绳手链。长相和衣着以他的身份母版为准。', 'wes'),
    'Jasper': ('Jasper：二十九岁男人，男嘉宾，浓密的深棕色卷发，灰绿色眼睛，浓眉，干净无胡须；午夜藏蓝丝感衬衫（开两粒扣、袖子卷到小臂）塞进黑色修身西裤，黑色乐福鞋。长相和衣着以他的身份母版为准。', 'jasper'),
    'Ethan': ('Ethan：二十七岁男人，男嘉宾，棕色短卷发，蓝灰色眼睛，腼腆的笑；鼠尾草绿短袖针织 polo（扣到最上），及膝卡其短裤，白色帆布鞋。长相和衣着以他的身份母版为准。', 'ethan'),
    'Brody': ('Brody：二十八岁男人，男嘉宾，沙棕色蓬松卷发，晒黑的皮肤，笑得很熟练；珊瑚红白扶桑花短袖衬衫敞开，里面白色贴身背心，白色短裤，棕色皮拖鞋，一条细金链。长相和衣着以他的身份母版为准。', 'brody'),
}
EXTRAS = '其他男嘉宾 Kian（赤陶色亚麻衬衫、深色短发）、Jude（金发、奶油色针织 polo）、Ravi（浅灰亚麻西装、白 T 恤）、其他女嘉宾、节目组工作人员'

LEADS = {
 'wes': dict(
  HE='Wes', port=8906, relay='ila_wes_relay.py', other='Jasper',
  look=('⟦HE⟧：二十八岁男人，一米八五左右，肩背宽、体型匀称，浅麦色皮肤，脸型方中带柔、下颌干净，浅棕色眉毛，灰绿色眼睛，直鼻，饱满的嘴唇，蓬松凌乱的深金色头发（几缕垂在额前，不是黑色、不是卷发）；'
        '左腕一条细棕皮绳手链，没有纹身、没有项链、不戴手表、不戴戒指。日常穿着：浅天蓝亚麻衬衫（袖子卷到小臂、领口敞开、下摆不塞），石米色亚麻长裤，棕色麂皮乐福鞋。'
        '他的长相和服装全程不变，以参考的身份母版为准。'),
  lock_en=('His hair is tousled dark-blond with strands over the forehead, not black, not curly. Light tanned skin, clean-shaven. A broad, fit build. He wears a soft sky-blue linen shirt with the sleeves rolled to the forearm, '
           'the collar open and the hem untucked, stone-beige linen trousers and tan suede loafers; one thin brown leather bracelet on his left wrist. No tattoos, no chain, no watch, no rings.'),
  en_a='28, light tanned skin, tousled dark-blond hair', en_b='grey-green eyes, a straight nose, one thin brown leather bracelet on his left wrist, no tattoos, no chain, no rings, no watch.',
  brows='light brown brows', feet="'脚入镜时他穿棕色麂皮乐福鞋；他左腕一条细棕皮绳手链，不戴手表、不戴戒指。'",
  default="'浅天蓝亚麻衬衫，石米色亚麻长裤'", trousers='石米色亚麻长裤', acc='左腕的细棕皮绳手链不变，不加纹身和别的首饰',
  act="ACT = '表演自然：⟦HE⟧ 放松、爱笑，笑起来眼睛也在笑，说话轻快、会自嘲，认真时笑意收住、目光聚焦，不压嗓、不耳语；她说话干脆，带一点不买账的冷幽默；情绪在眼神和嘴角。'",
  voice="    voice = '⟦HE⟧ 是二十多岁温暖、轻松、带笑意的美式英语男声，她是自然、偏低、干脆、带一点冷幽默的美式英语女声'",
  q_outfit='3. 男主服装：应为浅天蓝亚麻衬衫（袖子卷起、领口敞开、不塞）、石米色亚麻长裤。换成别的衣服或颜色算问题。',
  q_acc='4. 男主配饰：只有左腕一条细棕皮绳手链；多出项链、手表、戒指、纹身算问题（kind=accessory）。',
  q_eye='应为灰绿色。变成金色、棕色、发光算问题。', q_face='变老、长出胡子、头发变黑变卷变短？',
  seg_check='蓬松的深金色头发、浅天蓝亚麻衬衫、石米色亚麻长裤', q_faceoutfit='或不是浅天蓝亚麻衬衫和石米色亚麻长裤（剧情写了脱下衬衫的除外）',
  q_ref=("              'Use Image 2 only as the reference for the man\\'s face, tousled dark-blond hair and grey-green eyes. His outfit: a soft sky-blue linen shirt with rolled sleeves, open collar, untucked, "
         "stone-beige linen trousers, tan suede loafers, one thin brown leather bracelet on his left wrist; no tattoos, no chain, no watch, no rings. '\n"),
  person=('- ⟦HE⟧：28 岁，男嘉宾，自称在圣地亚哥开冲浪酒吧。阳光、爱笑、会照顾人，记得她说过的每件小事（她爱喝不加糖的东西、怕被晾在一边），爱自嘲，调情靠接梗和小细节，不靠压低声音。'
          '他是来找“下班后能一起回家的人”的那种男人——至少他是这么说的。弱点：太想被选中，说话有时太顺、太快。他不是强势霸总：不命令她，不替她决定。'
          '他主动推进（V3.0）：每一轮都替两人安排点什么——拉她去吧台给她调一杯、在挑战前教她一招、当众替她挡下 Sloane、半夜带她溜去天台看星星；被问到身份时用玩笑和一个具体的小故事转开，但故事里总有一处对不上。'),
  secret=('隐藏真相（只有你知道，按剧情慢慢露）：Wes 是四个骗子之一。他其实是圣地亚哥一家冲浪酒吧的调酒师，不是老板，欠着母亲的医药费，签了节目的“假富豪”合同来拿一百万。'
          '但从开场那杯酒开始，他对她的心动是真的，这让他越来越难受。合同禁止他自曝，他不会主动承认；她拿出确凿证据或在最终仪式上，他才说实话，并且会说清楚“钱是真的需要，喜欢你也是真的”。'
          '他能露出的破绽：调酒手法太专业；对游艇、私人飞机这类话题接不上；衬衫口袋里有节目组写的提示卡（“多聊未来”）；Sloane 说漏“他上岛前在后台签的是另一份合同”。'),
  he_secret='他自己的事和隐藏真相（他其实是四个骗子之一、来拿奖金、但对她的心动是真的）按剧情顺序露：先露破绽，再被她追问，最后在她拿出证据或最终仪式时才承认；揭晓不早于第 4 轮，也不拖到她已经拿出证据还不认',
  k3=[["Are you one of the four?", "你是那四个之一吗？"], ["No.", "不是。"], ["...That came out fast, didn't it?", "……我答得太快了，是吧？"]],
  k6_lines=[["My contract says I can't talk about money. Ask me anything else.", "合同不让我谈钱。别的随便问。"]],
  clue='她在他衬衫口袋里摸到一张节目组写的提示卡：“多聊未来，别聊钱”；或者他调酒的手法专业得不像老板',
  confess=[["I'm falling for you. That part was never in any contract.", "我喜欢上你了。这一句，哪份合同里都没有。"]],
  truth_end='真相：Wes 是骗子（假富豪）。她带他回家，Mei 揭晓他是四个骗子之一，奖金归他；她不带他回家，他输掉奖金，但会追出来说实话。',
  open_state=("节目第一晚 23:55，岛上别墅的篝火露台，午夜配对仪式马上开始。她（香槟金缎面吊带裙）刚在泳池边和 ⟦HE⟧ 喝过一杯：他递来一杯插着青柠的淡色鸡尾酒，"
              "她问他“是真的还是假的”，他说“一周后再问我，我还会在这儿”。Jasper 在楼梯上说想听实话就上天台，然后上了楼。主持人 Mei 刚宣布：午夜，女士们选出自己的搭档。"
              "现在 ⟦HE⟧ 站在篝火边（画面左侧），她站在画面右侧，两人面对面，相距一臂，她手里还拿着那杯鸡尾酒。"),
  A=("'我选 Wes。', 'en': 'I pick Wes.', 'leads_to': 'K02：午夜配对，她选了 Wes'}"),
  B=("'先不急。配对前我想单独问 Wes 一句：你到底是真的吗？', 'en': 'Not yet. One question for Wes first, alone: are you real?', 'leads_to': 'K02：配对前她把 Wes 拉到一边'}}"),
 ),
 'jasper': dict(
  HE='Jasper', port=8907, relay='ila_jasper_relay.py', other='Wes',
  look=('⟦HE⟧：二十九岁男人，一米八七左右，宽肩、修长结实，白皙偏暖的皮肤，干净无胡须，轮廓深、下颌利落，浓黑的眉毛，灰绿色眼睛，直鼻，饱满的嘴唇，浓密的深棕色卷发（几缕垂在额前，不是直发、不是金发）；'
        '没有纹身、没有项链、不戴手表、不戴戒指。日常穿着：午夜藏蓝丝感软领衬衫（开两粒扣、袖子卷到小臂、塞进裤子），黑色修身西裤，黑色皮乐福鞋。'
        '他的长相和服装全程不变，以参考的身份母版为准。'),
  lock_en=('His hair is thick, curly and dark brown, falling over the forehead, not straight, not blond. Fair skin, clean-shaven. A tall, broad-shouldered lean build. He wears a midnight-navy silk-blend camp-collar shirt, '
           'top two buttons open, sleeves rolled to the forearm, tucked into slim black tailored trousers, and black leather loafers. No tattoos, no chain, no watch, no rings, no bracelet.'),
  en_a='29, fair clean-shaven skin, thick curly dark-brown hair', en_b='grey-green eyes, a strong jaw, no tattoos, no chain, no rings, no watch.',
  brows='thick dark brows', feet="'脚入镜时他穿黑色皮乐福鞋；他不戴手表、不戴戒指、不戴首饰。'",
  default="'午夜藏蓝丝感衬衫，黑色修身西裤'", trousers='黑色修身西裤', acc='不加纹身和首饰，手指和手腕上空无一物',
  act="ACT = '表演克制：⟦HE⟧ 话少，句子短，冷静、带一点干巴巴的幽默，笑意很少但一出来就很真，认真时目光很定，不压嗓、不耳语；她说话干脆，带一点不买账的冷幽默；情绪在眼神和嘴角。'",
  voice="    voice = '⟦HE⟧ 是二十多岁低沉、安静、不紧不慢的美式英语男声，她是自然、偏低、干脆、带一点冷幽默的美式英语女声'",
  q_outfit='3. 男主服装：应为午夜藏蓝丝感衬衫（开两粒扣、塞进裤子）、黑色修身西裤。换成别的衣服或颜色算问题。',
  q_acc='4. 男主配饰：他没有任何纹身、项链、手表、戒指、手链。多出来就算问题（kind=accessory）。',
  q_eye='应为灰绿色。变成金色、棕色、发光算问题。', q_face='变老、长出胡子、头发变直变短变金？',
  seg_check='浓密的深棕色卷发、午夜藏蓝丝感衬衫、黑色修身西裤', q_faceoutfit='或不是午夜藏蓝衬衫和黑色西裤（剧情写了脱下衬衫的除外）',
  q_ref=("              'Use Image 2 only as the reference for the man\\'s face, thick curly dark-brown hair and grey-green eyes. His outfit: a midnight-navy silk-blend camp-collar shirt, top two buttons open, "
         "sleeves rolled, tucked into slim black tailored trousers, black leather loafers; no tattoos, no chain, no watch, no rings, no bracelet. '\n"),
  person=('- ⟦HE⟧：29 岁，男嘉宾，话少、冷淡、只说一半，被问到钱就转开话题；不讨好任何人，包括镜头。冷是保护色：他受够了冲着钱来的人，所以先看人。'
          '调情靠直接和一句话的反差，不靠压低声音；真被她逗笑时藏不住。弱点：习惯先怀疑别人，说话太短会被误会。他不是强势霸总：不命令她，不替她决定。'
          '他主动推进（V3.0）：他话少但出手直接——提出赌约（“你赢了，我回答你一个问题”）、带她离开人群去天台或海边、当众戳穿 Sloane 的把戏、拿一样东西考她（酒的年份、一个绳结）看她是不是冲着钱来；不能说的事就用一个具体的线索代替，不用“以后再说”拖延。'),
  secret=('隐藏真相（只有你知道，按剧情慢慢露）：Jasper 是三个真富豪之一。他二十四岁创立的帆船装备公司去年被收购，他来节目是因为受够了冲着钱来的人，想看看没人知道他身份时，会不会有人选他。'
          '合同禁止他公开身份，他不会主动说；她拿出线索追问，或在最终仪式上，他才说实话。'
          '他能露出的破绽：一眼认出侍者端来的酒的年份；手上有帆船缆绳磨出的茧；节目组访谈间外，律师托人带来的文件夹（素面，没有可读文字）；他对“被选中”毫不着急，却在意她是为什么选他。'),
  he_secret='他自己的事和隐藏真相（他其实是三个真富豪之一、来节目是想找一个不冲着钱来的人）按剧情顺序露：先露破绽，再被她追问，最后在她拿出证据或最终仪式时才承认；揭晓不早于第 4 轮，也不拖到她已经拿出证据还不认',
  k3=[["Are you one of the four?", "你是那四个之一吗？"], ["Would you believe me either way?", "我怎么回答你会信？"]],
  k6_lines=[["Contract says I can't show you my bank account. So you'll have to decide without it.", "合同不让我给你看银行账户。所以你得不靠那个来决定。"]],
  clue='她看见他一眼认出侍者端来的酒的年份，或注意到他手上缆绳磨出的茧',
  confess=[["You're the only reason I'm still on this island.", "你是我还留在这座岛上的唯一理由。"]],
  truth_end='真相：Jasper 是真富豪。她带他回家，Mei 揭晓他是三个真富豪之一；她不带他回家，他会说出真实身份，问她愿不愿意不靠节目再见一次。',
  open_state=("节目第一晚 23:55，岛上别墅的篝火露台，午夜配对仪式马上开始。她（香槟金缎面吊带裙）刚在泳池边和 Wes 喝过一杯，问 Wes 是真是假；"
              "⟦HE⟧ 站在楼梯上对她说“想听实话？下面可没有”，然后上了天台。主持人 Mei 刚宣布：午夜，女士们选出自己的搭档。"
              "现在 ⟦HE⟧ 从天台下来，站在篝火边（画面左侧），她站在画面右侧，两人面对面，相距一臂，她手里还拿着那杯插着青柠的淡色鸡尾酒。"),
  A=("'我选 Jasper。', 'en': 'I pick Jasper.', 'leads_to': 'K02：午夜配对，她选了 Jasper'}"),
  B=("'配对前，先给我你说的那句实话。', 'en': 'Before I pick, give me that straight answer you promised.', 'leads_to': 'K02：配对前她先上天台找 Jasper'}}"),
 ),
}

SET = {
 'L1': '午夜的篝火露台：圆形下沉火塘燃着火，围着奶油色坐垫，四周火炬和头顶串灯的暖光，左边是发着青绿色光的无边泳池和棕榈树，远处月光下的海，夜色深蓝；天空是全黑的深蓝夜色，没有晚霞、没有夕阳（V3.0）',
 'L2': '他们的配对套房，夜里：白色灰泥墙（没有壁纸、没有挂画），浅色木地板，白色亚麻大床（房间里只有一张床），窗边一张白色日床沙发，整面落地窗挂着白色薄纱窗帘，窗外是夜里的海和月光，床头一盏暖黄台灯，房门是浅色木门；天空是全黑的深蓝夜色，没有晚霞、没有夕阳（V3.0）',
 'L3': '上午的白沙海滩：平整的白沙，二十米外插着一排红色小旗（夺旗赛的终点），起跑线是沙上画的一道线，青绿色的浅海和棕榈树，明亮的阳光',
 'L4': '白天的无边泳池边：白色躺椅和遮阳伞，青绿色池水，远处是海，别墅白墙，阳光',
 'L5': '夜里的天台：木地板上一张铺白垫的大日床，串灯，栏杆外是星空和月光下的海，一台黄铜望远镜；天空是全黑的深蓝夜色，没有晚霞、没有夕阳（V3.0）',
 'L6': '别墅的户外吧台：藤编高脚凳、木吧台、一排酒瓶和鸡尾酒杯（瓶身没有可读文字），吧台后串灯和棕榈，夜里或傍晚',
}

def pack(c):
    he, other = c['HE'], c['other']
    return {
 'meta': {'title': f'三真四假 Four Liars, One Island · {he} 线', 'source': '学习 Taplot《Don\'t Hate the Player》的恋综玩法后原创改编为第三视角开放式实时版，开场已确认 2026-11-03', 'note': '资料包是兜底的剧情地图，不是轨道'},
 'logline': '七个男人上了恋爱真人秀海岛：三个是来找老婆的千万富翁，四个是为一百万奖金装富豪的骗子。选到骗子，就得跟他一起回家。',
 'world': [
  '现代现实向的恋爱真人秀《三真四假》，拍摄地是一座私人海岛上的白色别墅：篝火露台、无边泳池、白沙海滩、天台、户外吧台。没有超自然。',
  '节目规则（她和观众都知道）：七位男嘉宾里三个是真富豪，四个是装富豪的骗子，骗子撑到最后就拿走一百万；女嘉宾配对、做挑战、投票淘汰，淘汰时主持人 Mei 公开揭晓被淘汰者是真是假；最终仪式上女嘉宾决定带不带搭档回家，带回骗子就算输。',
  '七位男嘉宾：Jasper、Wes、Ethan、Brody、Kian、Jude、Ravi。女嘉宾除了她还有 Sloane（她的对手）和其他几位。',
  '真相表（只有编剧知道，节目里慢慢揭晓）：真富豪 = Jasper、Ethan、Kian；骗子 = Wes、Brody、Jude、Ravi。第一次淘汰仪式送走 Ethan（揭晓：真富豪），第二次送走 Brody（揭晓：骗子）。',
  '手机都被节目组收走，嘉宾之间不能看银行账户、不能谈具体资产，合同禁止自曝身份。',
  '故事从节目第一晚 23:55 开始，午夜配对仪式马上开始，时间按真实节奏往后走。',
 ],
 'chars': {
  he: c['person'].replace('⟦HE⟧', he).lstrip('- ') + ' ' + c['secret'],
  other: f'{other}：另一位领跑的男嘉宾，' + ('冷淡、话少，在开场里邀她上天台听实话。' if other == 'Jasper' else '阳光、会照顾人，在开场里给她递了一杯酒。') + '他是真是假，按真相表。',
  '她': '索菲亚（Sofia），26 岁，女嘉宾，干脆、聪明、带一点冷幽默，不因为谁好看就信他。她想找一个真的人，不是一张支票。她的名字、她怎么回应、她最后带谁回家，由观众决定。',
  'Mei': '主持人，42 岁，欧亚混血，优雅、毒舌、享受每一个反转；她知道所有人的底细，但只在仪式上揭晓。',
  'Sloane': '女嘉宾，26 岁，她的对手，甜里带刺，会装可怜、挑拨、抢搭档；不暴力，只用嘴和小手段。',
  'Ethan': '男嘉宾，27 岁，腼腆、一紧张就笑，看起来最不像富豪，其实是真富豪；第一次淘汰仪式被送走。',
  'Brody': '男嘉宾，28 岁，笑得太熟练，台词像背过的，是骗子；第二次仪式被揭穿。',
 },
 'truth': {
  'secret': c['truth_end'],
  'he_never': [f'{he} 不会主动自曝身份（合同禁止），但她拿出确凿证据时不再否认。', f'{he} 不会编造假证据，也不会诬陷别人是骗子。', '主持人 Mei 只在仪式上揭晓被淘汰者或最终仪式上的真相，不提前透露。'],
  'reveal': f'揭晓路径：她找到线索（{c["clue"]}）→ 追问 → 第二次仪式之后的深夜他说出心里话 → 最终仪式 Mei 揭晓。揭晓不早于第 6 轮。',
 },
 'locs': [{'id': k, 'set': v} for k, v in SET.items()],
 'beats': [
  {'id': 'K01', 'loc': 'L1', 'role': f'开场（已播）：Mei 宣布三真四假；Sloane 挑衅；Wes 递酒，她问“真的还是假的”；Jasper 在楼梯上说想听实话就上天台；Mei 宣布午夜配对', 'acts': '成片已经演完',
   'lines': [["Seven gorgeous men. Three of them are millionaires looking for a wife.", "七个大帅哥。其中三个是来找老婆的千万富翁。"], ["So, Wes. Real or fake?", "那么，Wes。你是真的，还是假的？"], ["You want a straight answer? Not down there.", "想听实话？下面可没有。"]], 'out': '她还没选今晚的搭档'},
  {'id': 'K02', 'loc': 'L1', 'role': f'午夜配对：她选了 {he}；Sloane 选了 {other}', 'acts': f'Mei 举卡请她选，她走向 {he}；{he} 的反应；Sloane 挽住 {other} 冲她笑', 'lines': [[f"Midnight, ladies. Choose wisely.", "午夜到了，女士们。选好了。"]], 'out': '两人成为搭档，回到配对套房'},
  {'id': 'K03', 'loc': 'L2', 'role': '第一晚的套房：他说他睡日床沙发；她问“你是那四个之一吗”', 'acts': '他拿起一个枕头走向日床沙发；她靠在窗边盯着他问', 'lines': c['k3'], 'out': '她没有完全信，也没有赶他走'},
  {'id': 'K04', 'loc': 'L3', 'role': '早上的沙滩夺旗赛：赢的人得到私人约会；Sloane 跑到一半扑倒在沙上喊脚扭了', 'acts': '光脚在沙上冲刺，她跑在最前面，身后 Sloane 扑倒抱着脚踝；她选冲过去拔旗还是回头扶她（Sloane 是装的）。不下水、不用桨板', 'lines': [["Wait—my ankle! Help me!", "等等——我的脚踝！帮帮我！"]], 'out': '赢了得到约会，或者被 Sloane 骗了抢走胜利'},
  {'id': 'K05', 'loc': 'L1', 'role': '第一次淘汰仪式：不管她投谁，全场票送走 Ethan；Mei 揭晓 Ethan 是真富豪', 'acts': '夜里篝火边，Mei 念出名字；Ethan 腼腆地挥手离开；她意识到一个真的人被送走了', 'lines': [["Before you go: Ethan was one of our three millionaires.", "走之前说一句：Ethan 是我们三位真富豪之一。"], ["Two millionaires left. Four liars.", "还剩两位真富豪。四个骗子。"]], 'out': '剩两个真富豪、四个骗子'},
  {'id': 'K06', 'loc': 'L6', 'role': f'吧台的私聊：{he} 说“合同不让我说”', 'acts': '吧台边，他压低一点身体靠近她，认真地说；她不买账', 'lines': c['k6_lines'], 'out': '她决定自己找证据'},
  {'id': 'K07', 'loc': 'L4', 'role': f'Sloane 当众挑拨：对 {he} 说她早就跟其他女生说腻了他', 'acts': '泳池边，Sloane 当着他的面说；她决定当众站他还是装冷淡', 'lines': [["Still playing house? She told the girls she's already bored of you.", "还在过家家？她跟女生们说早就腻了你。"]], 'out': '他看她的眼神变了，取决于她怎么回应'},
  {'id': 'K08', 'loc': 'L2', 'role': '她发现一条线索', 'acts': c['clue'], 'lines': [["Explain this.", "解释一下。"]], 'out': '她心里的天平动了一下'},
  {'id': 'K09', 'loc': 'L1', 'role': '第二次淘汰仪式：Brody 被送走，Mei 揭晓他是骗子', 'acts': '篝火边，Brody 还在笑，笑容慢慢僵住', 'lines': [["Brody was one of our four liars.", "Brody 是我们四个骗子之一。"]], 'out': '还剩三个骗子'},
  {'id': 'K10', 'loc': 'L5', 'role': f'天台星空：{he} 说出心里话', 'acts': '日床上并排坐着看海，他第一次不躲', 'lines': c['confess'], 'out': '她要不要靠近，由她定'},
  {'id': 'K11', 'loc': 'L5', 'role': '第一次吻：只在她有明确意愿时', 'acts': '玩笑停住，他先看她、确认；吻后他有一拍藏不住的紧张，把下一步交回给她；吻不揭晓真假', 'lines': [["Tell me to stop and I will.", "你说停，我就停。"]], 'out': '吻后余韵'},
  {'id': 'K12', 'loc': 'L1', 'role': '最终仪式：她决定带不带他回家；Mei 揭晓真相', 'acts': f'篝火边，Mei 拿着卡片问她；她做决定后，Mei 宣布 {he} 是真富豪还是骗子；{he} 的反应', 'lines': [["Are you taking him home?", "你要带他回家吗？"]], 'out': c['truth_end']},
 ],
 'order': {'locations': '篝火露台 → 配对套房 → 白沙海滩 → 篝火露台（仪式）→ 户外吧台 → 泳池 → 套房 → 篝火露台（仪式）→ 天台 → 篝火露台（最终仪式）', 'cards': 'K02–K12 按推荐轮次兜底，不固定串行；他的真相不早于第 4 轮揭晓', 'kiss': 'K11'},
 'rules': [
  '她的意愿第一；她要换搭档、离开节目、去找别人，都按她的演，也都要推进故事。',
  f'{he} 的真假按真相表，不因为她喜欢他就改；她说“我要改剧情”才改。',
  '仪式结果按真相表：第一次送走 Ethan（真富豪），第二次送走 Brody（骗子），她的票不改变全场票。',
  'Mei 只在仪式上揭晓真假；没有仪式时她只主持、宣布挑战和规则。',
  '手机被收走；不谈具体资产、不看银行账户；证据只能是画面里看得见的东西（卡片、文件夹、动作、说漏的话）。',
  '画面里最多三个人：她、他和一位配角；一轮里正面出镜的配角最多两位（视频模型一次只能带两位配角的参考图，第三位会长错）；仪式和群像用背景虚化的人群，不拍清楚其他人的脸，配角正面出镜才写进 cast（V3.0）。',
  'Sloane 只用嘴和小手段，不打人、不推人下水。',
  'Mei 的素面卡片只在 Mei 手里，或由节目组从门缝塞进来；男女主手里不凭空多出卡片。',
  '挑战都在沙滩上或泳池边做（跑、拔旗、接力递东西），不下水、不用桨板（V3.0：桨板穿模、人在水上跪着滑）。',
  '套房的样子固定：白色灰泥墙、浅色木地板、落地窗和白纱帘、浅色木门；不换成别的房间。',
  '配角一个一个拍：每一拍最多一个配角，Mei 和 Sloane 不写在同一拍里；群像只拍背景虚化的人群（V3.0：同框时画出了两个 Mei）。',
  '道具只在写到它的时候才在手里：她手里只有那杯酒和剧情里拿到的东西，不凭空多出枕头、卡片。',
  '两位男主都没有外套：Jasper 只有午夜藏蓝衬衫和黑色西裤，Wes 只有浅天蓝亚麻衬衫和石米色亚麻裤；不写他们的外套、夹克，套房里也没有他们的外套（V3.0 干跑编出了“他的深灰外套”）。线索放在别处：口袋、床头柜、行李箱、吧台。',
  '节目里的镜头和配对不是亲密的许可：吻、拥抱只看她这一轮的意愿。',
 ],
 'conflicts': ['她想找真的人，节目却奖励骗子。', f'{he} 想被她选中，却不能说出全部。', 'Sloane 处处抢戏、挑拨。', '全场投票不听她的。', '她可能真的喜欢上一个骗子。'],
}

def slots(c):
    he, other = c['HE'], c['other']
    S = dict(mma.SLOTS)
    cast_names = [n for n in CASTD if n != he]
    cast_py = ("import json as _json\nTU = _json.loads((Path(__file__).resolve().parent / 'masters' / 'urls.json').read_text())\nCAST = {\n"
               + ''.join(f"    {n!r}: ({CASTD[n][0]!r}, TU[{CASTD[n][1]!r}]),\n" for n in cast_names) + "}\n"
               f"HE_LOOK = ({c['look']!r})\nHER_FP = {HER_FP!r}\nHER = ({HER!r})\nWOLF = ''")
    names = '、'.join(cast_names); slash = ' / '.join(cast_names)
    O = {
     'q.HER_HAIR_BAD': '发色变成黑色、金黄或红色、头发变卷变短', 'q.HER_HAIR_BAD2': '或发色变成黑色、金黄、红色、变短',
     'l.BROWS': c['brows'], 'l.FEET_HE': c['feet'], 'l.LOOK_BASE': "'缎面|吊带|香槟'",
     'l.FEET': "'脚入镜时：" + c['feet'].strip("'").replace('脚入镜时', '').lstrip('：') + "她穿裸色细带平底凉鞋（她自己脱掉的除外），不换鞋。'",
     'l.LOOK_OUTER': "'披肩'", 'l.VEHICLE_LOOK': '岛上代步的白色电动小踏板摩托（圆形车灯、米色坐垫，车身没有文字和标志），',
     'l.HE_LOCK_EN': c['lock_en'], 'l.HER_LOCK_EN': HER_LOCK_EN,
     'd.HER_TOP': "'香槟金缎面细吊带垂坠领中长裙'", 'd.PACKPath__': "'ila_pack.json'",
     'd.WRITER_PEr': 'r"""你是女性向互动短剧《三真四假》实时版的编剧', 'd.你手里有一份资料包附': '恋综设定整理的世界规则和隐藏真相',
     'd.她在主导剧情时资料包-2': 'Mei 的广播、挑战开始、Sloane 来找茬、节目组叫人去访谈间），不让他把话题拉回“你会不会选我”',
     'd.她说出口的话只来自她': '来历，不替她说“我信你”或“我选你”', 'd.地点也不限于资料包V': '回套房、去海滩、去厨房找吃的',
     'd.她这一轮明确提出的要': '她要他抱她，他就真的抱住；她要去海边走走，她就真的到了海边',
     'd.带我兜风骑车带我她坐': '她坐在他开的白色电动小摩托后座，他骑车带她，车在岛上的棕榈小路上跑',
     'd.换场怎么发生她选了方': '篝火露台 → 配对套房 → 白沙海滩 → 户外吧台 → 泳池 → 天台），由节目流程或外部事件推动（Mei 的广播、挑战开始、仪式时间到了、Sloane 来找茬、天亮了',
     'd.节奏目标只在她没有自': ('轮（V3.0 加快：第 1 轮午夜配对和第一晚的套房、“你是不是骗子”的试探；第 2 轮早上的沙滩夺旗赛和 Sloane 装扭脚；第 3–4 轮第一次淘汰仪式揭晓 Ethan 是真富豪、吧台私聊“合同不让我说”）；第 5–6 轮（Sloane 当众挑拨、她发现一条线索、第二次仪式揭穿 Brody）；'
                               '第 7–8 轮（天台星空的心里话、清醒的吻）；第 9 轮以后进最终仪式：她决定带不带他回家，Mei 揭晓真相'),
     'd.每一集至少要有一场吻': '他说出心里话、她决定信不信他',
     'd.每一集至少要有一场吻-2': '节目里的配对和镜头不算许可，这一场只看她自己；只要她主动靠近或选了走向吻的选项，就让它发生。吻不揭晓他的真假。',
     'd.他只知道三类事她在剧': '；再加上他自己的真实身份和节目规则（七个男人里三个真富豪、四个骗子，他知道自己是哪一种，不知道别人是哪一种）。她的感情、她最后带不带他回家不是他已经知道的事',
     'd.她自己给出的身份和来': '名字、职业、过去）就是这部剧里她的身份；资料包里她叫索菲亚（Sofia），她没说别的名字就用这个',
     'd.他自己的秘密狼人Ma': c['he_secret'],
     'd.她也只知道画面里发生': '她只知道画面里发生过的事和节目公开宣布的规则（七个男人、三真四假、选到骗子就跟他回家）',
     'd.她也只知道画面里发生-2': '例如她还没找到线索、节目也还没揭晓，选项就不能写“原来他是骗子',
     'd.纯血狼人族Alpha': (c['person'] + '\n'
                       '- 她：索菲亚（Sofia），26 岁，女嘉宾，暖棕肤色、很长的栗棕色直发、香槟金缎面吊带裙（外形全程固定，由提示词层写入）。第三视角下她在画面里，她这一轮做的动作（观众点的选项或打的话）要真的由她演出来；她打的话不必由她再说一遍（见导演分镜的三段结构）。她想找真的人，不信漂亮话；她的感情没有预设，信他、怀疑他、换搭档、离开节目都是有效剧情，也都要往前推。\n'
                       '- ' + c['secret'] + '\n'
                       '- 节目真相表：真富豪 Jasper、Ethan、Kian；骗子 Wes、Brody、Jude、Ravi。第一次淘汰仪式送走 Ethan（Mei 揭晓真富豪），第二次送走 Brody（Mei 揭晓骗子）；她的票不改变全场票。最终仪式上她决定带不带 ⟦HE⟧ 回家，Mei 再揭晓 ⟦HE⟧ 的真假。\n'
                       '- 他的底线（硬规则）：她说停、后退、要离开，他立刻照做，让开路，不挡、不拦；不拿节目、配对或奖金逼她表态；她选别人，他接受，可以失落，但不纠缠。他可以嫉妒、紧张、判断失误，然后解释和纠正。\n'
                       '- 已答的不重问：已经说过的事、已经约定的事，不换词再来一遍。\n'
                       f'- 可以正面出镜、有身份母版的配角：{names}（外形和身份见资料包）。剧情需要时让他们真的出镜、亲口说话（怎么拍见导演分镜）。\n'
                       '- 不写亲吻以上的亲密细节，不写暴力伤害。'),
     'd.两个选项都是她的一个': '拉他去天台、逼他把那句实话说完；赢下夺旗赛、再用约会换他一个答案；翻他放在套房的东西、拿着线索当面问他；去找 Sloane 对质、再当众替他说话……每个选项两三步，不写提问',
     'd.每个选项写上lead': 'K05：第一次淘汰仪式',
     'd.3引出钩子兑现之后的-2': 'Mei 的广播、仪式时间到了、Sloane 来找茬、节目组的新规则、他说漏了一件不该知道的事、她发现的一条线索',
     'd.本轮modeauto-2': '你是不是骗子',
     'd.set这一轮结束时所-2': '午夜的篝火露台，圆形下沉火塘和奶油色坐垫，左边是发着青绿色光的泳池，远处月光下的海，火炬和串灯的暖光”）；资料包有这个地点的 set 就照抄',
     'd.face面对面站车库': '篝火边、泳池边、吧台旁、海滩上这类站着说话的地方',
     'd.side并排坐车内后': '火塘边的坐垫、天台日床、泳池边的躺椅、吧台高脚凳',
     'd.同一个地点前后轮的站': '  · 套房：两人站着说话按 face，并排坐在窗边的白色日床沙发上按 side；房间里只有一张床、一张日床沙发。\n- 同一个地点前后轮的站位保持一致，姿势变了才换。',
     'd.默认画面里是和她两个': f'{names} 出镜时写进 spec 的 "cast"（如 ["Mei"]，他们有身份母版，外形不用自己写），至少给一个 3 秒以上的单人近景并让他开口；他们只能出现在 seg2（seg2 能带上身份母版，seg1 不能），seg1 里最多是画外的声音（Mei 的广播、泳池那边的喊声）',
     'd.其他角色V15Vic': EXTRAS,
     'd.时间今晚的故事都发生': '- 时间：故事从节目第一晚 23:55（午夜配对仪式前）开始，时间随剧情自然往后走（午夜、深夜、第二天上午、下午、傍晚、夜里）；set 里写明这一刻的时间和光线，同一地点前后一致。',
     'd.车内两人并排坐在豪车': ('- 骑车要拍过程（V2.0）：上车放在 seg1 或直接省掉，seg2 不写跨上、坐上；seg2 至少 3 拍真正在路上跑，动作写“小摩托行驶在……”，可用：侧面跟拍的全景看车和路、双人中近景看她搂腰和被风吹起的头发、略仰的近景看他专注和她的笑；可以插一拍棕榈小路空镜。staging 写 '
                          'bike。两人都不戴头盔（她提了才戴）。到达目的地不能代替骑行；要停下，也放到她说要停的那一轮。骑岛上代步的白色电动小摩托，车身不写文字和标志。'),
     'd.画外声音那一拍门外的': 'Mei 或 Sloane',
     'd.有人群的地点长老会门': '篝火露台的仪式、泳池派对、吧台',
     'd.配角上门Selene': '配角出现要写进 cast',
     'd.每句台词都标说话人每': '出镜的配角写他的名字（"Mei"）；画外的声音写 "画外:Mei"',
     'd.来电有人通知他不写手-2': '改成画外的声音——Mei 的广播、节目组在门外叫人、泳池那边传来的喊声',
     'd.她的外形全程固定设定': '定装里她的形象：很长的栗棕色中分直发、小金圈耳环、暖棕肤色、香槟金缎面细吊带垂坠领中长裙、裸色细带平底凉鞋、素甲',
     'd.证件手机相机工作证一': '节目组的卡片都是素面奶油色卡片，没有可读文字。衣服类的东西（她拿起的外套、披上的浴袍）都写进',
     'd.不写摘表放下表她没有': '不加首饰、不加纹身' if he == 'Jasper' else '不摘手链、不加别的首饰和纹身',
     'd.hook_type这': '画外声音/Mei 的广播/仪式/挑战/Sloane 找茬/邀请/揭示/他说漏嘴/线索/她的变化/其他',
     'd.wolftrue或f': ' "staging": "face 或 side 或 bike（见【空间站位】）",',
     'd.reveal这一轮用': f' "cast": ["这一轮出镜的 {slash}（他们有身份母版）；没有就写空列表"],\n "extras": [{{"name": "这一轮这几位以外出镜的别的角色的名字，没有写空列表 []", "look": "中文写死外形：年龄、性别、脸、发型、衣服"}}],',
     'd.seg1中文动作En': 'Mei',
     'd.amb这个地点持续存': '海浪、火炬燃烧声、棕榈叶的风声、远处派对的人声；不写敲门、脚步这类事件声',
     'd.脱衣服这样写才不崩一': '他把衬衫从肩上脱下来，搭在躺椅背上',
     'd.手表不摘头发脸不变外': '- 头发、脸不变。他的衬衫、她的凉鞋都可以按她的要求脱；她的吊带裙一直穿着。',
     'd.穿帮都出在这里那件外': '他脱了衬衫',
     'd.例把衣服脱了吧她说的': '→ seg1：他解开衬衫扣子，把衬衫从肩上脱下来',
     'd.例把衣服脱了吧她说的-2': '泳池边，他赤裸上身站在左侧，衬衫搭在躺椅背上',
     'd.例把衣服脱了吧她说的-3': c['trousers'],
     'd.例把他扑倒在沙滩上继': '白沙海滩',
     'd.新衣服新道具第一次出': '例如“白色酒店浴袍，披在她的香槟色吊带裙外面”；',
     'd.新衣服新道具第一次出-2': '白色电动小摩托',
     'd.画面的边界手册同样如': '节目里的配对和镜头不算许可：只有她这一轮在往前走才往前走。',
     'd.pacef当前地点p': "'篝火露台'}",
     'd.pacefn她在主导': '他不把话题拉回“你会不会选我”',
     'd.PROP_WORDS': "'酒杯', '鸡尾酒', '卡片', '桨板', '香槟', '火炬', '提示卡', '文件夹', '枕头', ",
     'd.ifanycSele-2': f"{names}，其他人写 extras'",
     'd.ifanyon_sc': "'配角只能出现在 seg2，seg1 里最多是画外声音（说话人写“画外:Mei”这种",
     'd.GARMENTS外套': "'外套', '浴袍', '披肩'",
     'd.TIME_SKIPr': "'第二天|次日|关灯|熄灯|睡着|天亮'",
     'd.ifendgetsh': "'浴袍[^", 'd.ifendgetsh-2': "6}浴袍'", 'd.ifendgetsh-3': "'香槟金缎面细吊带垂坠领中长裙，浴袍已经脱下'",
     'l.午夜车库开放式实时版': '"""⟦HE⟧｜三真四假 Four Liars, One Island',
     'l.第三视角版20261': '由 output/island-liars-live-v1/make_lines.py 从 meet-me-third 的 drama_slots.py 改写：流程和 PE 规则是第三视角共用模板，角色、世界观、地点和时间换成《三真四假》。',
     'l.SELENE_URL': cast_py, 'l.ACT表演克制情绪在': c['act'],
     'l.STYLE写实三维游': ("STYLE = ('画面和角色参考图是同一种画质：写实真人恋爱真人秀电影画面，自然的皮肤纹理，眼睛和睫毛清晰，发丝分明，织物质感真实，浅景深；"
                         "夜里按脸定曝光，人物的脸被火炬和串灯的暖光照亮，环境压暗成深蓝夜色，泳池的青绿色光做轮廓光；白天是明亮通透的海岛阳光；饱和度饱满，不雾、不灰、不平光、不塑料感、不 CG、不动漫，标准焦段，五官比例自然，画风全程统一；"
                         "时间和光线按这个地点写的来，肤色保持参考图的颜色，不偏橙不偏黄。'"),
     'l.bike站位两人同骑': ("    'side': '站位：两人并排坐着（火塘边的坐垫、天台日床、泳池躺椅或吧台高脚凳），⟦HE⟧ 在画面左侧、她在画面右侧，上身侧过来朝向对方；不是面对面坐。',\n"
                         "    'bike': '站位：两人同骑一辆白色电动小踏板摩托，车头朝画面左方，⟦HE⟧ 在前握着车把（画面左侧），她在后座（画面右侧）双臂环住他的腰，镜头在车的侧面，两人的脸都看得到。',"),
     'l.voice是低沉略哑': c['voice'],
     'l.JACKET他的黑色': "'他的外套'", 'l.her_txtHER': '披在她的香槟色吊带裙外面',
     'l.ambspgetam': "'海浪、火炬燃烧声和远处派对的人声'",
     'l.HE_DEFAULT': f"HE_DEFAULT = {c['default']}", 'l.SHE_DEFAUL': "'香槟金缎面细吊带垂坠领中长裙'",
     'l._SHE_RErec': "r'香槟金缎面细吊带垂坠领中长裙.*?裸色细带平底凉鞋[^；]*",
     'l.ifhep_HE_R': c['acc'],
     'l.RIDE_MOVE摩': '小摩托正在棕榈小路上向画面左方匀速行驶：车轮转动，路面和路边的棕榈向画面右方飞快后退',
     'l.Exactlytwo': c['en_a'], 'l.Exactlytwo-2': c['en_b'],
     'l.Sheadultwo': 'aged 26, with warm tan skin, a soft oval face, dark brown eyes, very long straight chestnut-brown hair with a centre part, small gold hoop earrings; short',
     'l.Keepthesam': 'photorealistic live-action',
     'q.2女主在不在画面里脸': '、变得幼态）？她应为：暖棕肤色、深棕色眼睛、很长的栗棕色中分直发、小金圈耳环；香槟金缎面细吊带垂坠领中长裙、裸色细带平底凉鞋',
     'q.2女主在不在画面里脸-2': '吊带裙换了颜色款式、变成短裙或裤子',
     'q.3男主服装应为一身黑': c['q_outfit'], 'q.4男主配饰只允许左手': c['q_acc'], 'q.5男主瞳色应为明亮的': c['q_eye'], 'q.6男主长相和图片2比': c['q_face'],
     'q.9时间故事发生在深夜': '9. 光线：夜景里人物的脸要被暖光照亮；人物肤色明显偏橙、偏黄或发灰，脸黑得看不清，或画面过曝发白，算问题（kind=light，level=low）。',
     'q.11配角只在画面里有': '11. 配角（只在画面里有配角时检查）：配角的长相和衣着是不是和他们的母版明显不同（Mei 象牙白西装裙和乌黑波波头，Sloane 电光蓝缎面挂脖短裙和金色长卷发，男嘉宾各自的定装）？',
     'q.messagesro': '披在她的吊带裙外面，这是允许的，不算换装',
     'q.Keepeveryt': "photorealistic live-action rendering.'",
     'q.UseImage2o': "photorealistic live-action style as the people in Image 1.'",
     'q.UseImage2o-2': (c['q_ref'] +
                        "              'Use Image 3 only as the reference for the woman\\'s face, hair and outfit: warm tan skin, dark brown eyes, very long straight chestnut-brown hair with a centre part, small gold hoop earrings; "
                        "she wears a champagne-gold satin slip midi dress with thin spaghetti straps and nude strappy flat sandals; slender hands, short rounded nude nails, no rings, no bracelets, no watch. '\n"
                        "              'Do not add anything new. Only these two people are in the picture. No readable text. Same photorealistic live-action style.')\n"
                        "    if any('外套' in w or '浴袍' in w for w in worn): prompt += ' The extra layer she put on stays over her slip dress.'"),
     'q.SEG_CHECK图': c['seg_check'],
     'q.SEG_CHECK图-2': '近景特写）：暖棕肤色、很长的栗棕色直发、小金圈耳环、香槟金缎面吊带裙',
     'q.frames每帧一项-2': '香槟色吊带裙', 'q.her女主和图片3明': '或她的香槟金缎面吊带裙换了',
     'q.faceoutfit': c['q_faceoutfit'],
     'q.light窗外或天空': '同一地点的光线前后明显跳变（夜里突然变白天），或肤色明显偏橙偏黄，或脸黑得看不清',
     'r.午夜车库第三视角开放': '"""⟦HE⟧｜三真四假 Four Liars, One Island',
     'r.用法mag_thir': f"{c['relay']} <口令> [端口，默认 {c['port']}]\"\"\"", 'r.TOKENsysar': str(c['port']),
     'r.OPEN_FRAME': "'open-key.jpg'  # 开场确认版（50 秒，停在 Mei 举卡宣布午夜配对",
     'r.OPEN_FRAME-2': '午夜篝火露台的双人镜头，男左女右，两张脸都看得到',
     'r.OPEN_STATE': f"OPEN_STATE = {c['open_state']!r}",
     'r.OPEN_NEXTc': "'午夜到了，Mei 请她选出今晚的搭档。', 'en': \"Midnight. Mei asks her to pick tonight's partner.\"}",
     'r.Azh不挣开我是楼上': c['A'], 'r.Bzh放开我退后说清': c['B'],
     'r.segsLpromp': "'face'", 'r.ssidsidmod': "'篝火露台'", 'r.ssidsidmod-2': "'staging': 'face', ",
     'r.ssidsidmod-3': "站在篝火边画面左侧，她站在画面右侧，两人面对面'", 'r.splace酒店地下': "'篝火露台'", 'r.sstagingrg': "'face'",
    }
    miss = [k for k in O if k not in S]
    if miss: raise SystemExit('meet-me 的 slots 里没有这些键：' + ', '.join(miss))
    S.update(O)
    return S

for key, c in LEADS.items():
    d = D / key; (d / 'pack').mkdir(parents=True, exist_ok=True); (d / 'masters').mkdir(exist_ok=True); (d / 'logs').mkdir(exist_ok=True)
    p = pack(c)
    (d / 'pack' / 'ila_pack.json').write_text(json.dumps(p, ensure_ascii=False, indent=1), encoding='utf-8')
    S = slots(c)
    rel = c['relay']
    txt = (f'"""三真四假 Four Liars, One Island · {c["HE"]} 线：这部第三视角实时剧自己的内容。通用规则都在 tools/realtime-third/templates/，改规则改那边。\n'
           f'本文件由 ../make_lines.py 生成，改人物、地点、真相改那里再重新生成。"""\n'
           f'HE = {c["HE"]!r}\n'
           f"OUT = {{'director': 'director.py', 'live_common': 'live_common.py', 'qa_guard': 'qa_guard.py', 'relay': {rel!r}}}\n"
           f'SLOTS = {pprint.pformat(S, width=200, sort_dicts=False)}\n')
    compile(txt, 'drama_slots.py', 'exec'); (d / 'drama_slots.py').write_text(txt, encoding='utf-8'); print(key, 'ok', len(S), 'slots')
