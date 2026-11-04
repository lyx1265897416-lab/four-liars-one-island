# -*- coding: utf-8 -*-
"""《三真四假》选角 V3 + 定装。库图是身份来源，定装图（costume/<id>.png，白底全身正面）是之后所有镜头和实时母版的服装来源。"""
LIB = '/Users/vicky/Documents/waku内容/vicky-character-library/assets/realistic/'
W, A, B = 'western-male-white-28-v3-20260923/', 'male-white-portraits-23-v2-20260923/', 'male-white-portraits-31-v2-20260923/'
F = 'front-id-32-20260923/'

# id: (名字, 库图, 年龄, 身份要点, 定装英文, 定装中文)
CAST = {
    'jasper': ('Jasper Vance', W + '01.png', 29, 'cold lead',
               'a midnight-navy silk-blend shirt with a soft camp collar, top two buttons open, sleeves rolled to the forearm, tucked into slim black tailored trousers, black leather loafers; no jewellery, no watch',
               '午夜藏蓝丝感衬衫（开两粒扣、袖子卷到小臂）塞进黑色修身西裤，黑色乐福鞋；不戴首饰和手表'),
    'wes': ('Wes Callahan', W + '11.png', 28, 'warm lead',
            'a soft sky-blue linen shirt, sleeves rolled, collar open, untucked over stone-beige linen trousers, tan suede loafers; one thin brown leather bracelet on his left wrist, no watch',
            '浅天蓝亚麻衬衫（袖子卷起、领口敞开、不塞）配石米色亚麻长裤，棕色麂皮乐福鞋；左腕一条细棕皮绳手链，不戴手表'),
    'ethan': ('Ethan Moss', W + '16.png', 27, 'nervous real millionaire',
              'a sage-green short-sleeve knit polo buttoned to the top, khaki chino shorts to the knee, white canvas sneakers; no jewellery',
              '鼠尾草绿短袖针织 polo（扣到最上）、及膝卡其短裤、白色帆布鞋；不戴首饰'),
    'brody': ('Brody Keane', W + '02.png', 28, 'too-smooth player',
              'an open short-sleeve shirt with a bold coral-and-white hibiscus print over a fitted white tank top, white shorts, tan leather slides; a thin gold chain',
              '珊瑚红白大朵扶桑花短袖衬衫敞开，里面白色贴身背心，白色短裤，棕色皮拖鞋；一条细金链'),
    'kian': ('Kian Mercer', A + 'character-03.png', 30, 'confident',
             'a terracotta linen shirt open at the collar, sleeves rolled, tucked into cream trousers, brown leather belt, brown loafers; no jewellery',
             '赤陶色亚麻衬衫（领口敞开、袖子卷起）塞进奶油色长裤，棕皮带，棕色乐福鞋；不戴首饰'),
    'jude': ('Jude Larsen', W + '27.png', 27, 'aloof',
             'a cream short-sleeve knit polo with an open collar, black linen trousers, black leather sandals; no jewellery',
             '奶油色短袖针织 polo（领口敞开）、黑色亚麻长裤、黑色皮凉鞋；不戴首饰'),
    'ravi': ('Ravi Sethi', B + 'character-26.png', 29, 'quiet observer',
             'an unlined light-grey linen blazer over a plain white crew-neck T-shirt, light-grey linen trousers, white leather sneakers; no jewellery',
             '浅灰亚麻无衬里西装外套，里面纯白圆领 T 恤，浅灰亚麻长裤，白色皮质运动鞋；不戴首饰'),
    'her': ('She', F + 'character-11.png', 26, 'heroine',
            'a champagne-gold satin slip midi dress with thin spaghetti straps and a soft cowl neckline, bias-cut to mid-calf, nude strappy flat sandals; the same small gold hoop earrings as her reference; short rounded nude nails; no necklace, no rings, no bracelet',
            '香槟金缎面细吊带垂坠领中长裙（斜裁到小腿中部），裸色细带平底凉鞋；和参考一样的小金圈耳环；短圆裸色指甲；不戴项链、戒指、手链'),
    'mei': ('Mei', '/Users/vicky/Interactive storyline/output/island-liars-live-v1/opening-v1/costume/mei-face.png', 42, 'host',  # 11-03 Vicky 选 H1（host_cands.py 新生成，欧亚混血），原库图白底女 32 组 16 退役
            'a tailored ivory-white blazer dress with a single button, sleeves pushed slightly up, nude pointed heels; small pearl stud earrings; she holds a plain cream card with nothing written on it',
            '象牙白单扣西装连衣裙（袖子微微推起），裸色尖头高跟鞋；小珍珠耳钉；手里一张素面奶油色卡片'),
    'sloane': ('Sloane', F + 'character-23.png', 26, 'rival',
               'an electric-blue satin halter-neck mini dress, silver strappy heeled sandals, small silver drop earrings; long glossy almond nails in pale pink',
               '电光蓝缎面挂脖短裙，银色细带高跟凉鞋，小银色垂坠耳环；淡粉色长杏仁形亮面指甲'),
}

def costume_prompt(cid):
    name, _, age, _, en, _ = CAST[cid]
    he = cid not in ('her', 'mei', 'sloane')
    who, pos, sub = ('man', 'his', 'He') if he else ('woman', 'her', 'She')
    return (f'Full-body costume reference photo of the exact same {age}-year-old {who} as in the reference image: '
            f'keep {pos} identical face, bone structure, eyes, skin tone, hair colour, hairstyle and hair length exactly; the face must be instantly recognisable as the same person. '
            f'Wardrobe: {en}. '
            f'{sub} stands straight facing the camera, relaxed natural pose, arms loosely at the sides, whole body visible from the top of the head to the shoes, centred, '
            'on a seamless pure white studio background with soft even light and a faint floor shadow. '
            'Photorealistic live-action photograph, natural skin texture, true-to-life proportions (about 7.5 heads tall), sharp focus, 85mm lens look. '
            'No text, no logos, no brand marks, no extra people.')
