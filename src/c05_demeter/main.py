# -*- coding: utf-8 -*-
"""Chapter: 5.デメテルの信頼
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
## local files
from src.c05_demeter.e_fakenews import ep_fake_news
from src.c05_demeter.e_illeagal import ep_illeagal_way
from src.c05_demeter.e_insect_attack import ep_insect_attack
## defines
W = Writer
_ = W.getWho()


## main
def ch_demeter(w: World):
    return w.chapter("デメテルの信頼",
            ep_insect_attack(w),
            ep_fake_news(w),
            ep_illeagal_way(w),
            ## NOTE
            ##  - 大陸鉄道が蟲型に襲われ、首都に行く手段を失う
            ##  - 立ち寄った街で情報屋から仕入れるが、騙されるアルたち
            ##  - 運搬用の自走トラックに乗り込み、首都を目指すアルたち
            note="大陸横断鉄道で首都に向かう一行だったが、途中で蟲型に襲われる")
