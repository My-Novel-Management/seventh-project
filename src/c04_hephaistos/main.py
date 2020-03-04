# -*- coding: utf-8 -*-
"""Chapter: 4.ヘパイストスの焦燥
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
## local files
from src.c04_hephaistos.e_breuccel import ep_breuccel
from src.c04_hephaistos.e_ticket import ep_ticket
from src.c04_hephaistos.e_train import ep_trans_railway
## defines
W = Writer
_ = W.getWho()


## main
def ch_hephaistos(w: World):
    return w.chapter("ヘパイストスの焦燥",
            ep_breuccel(w),
            ep_ticket(w),
            ep_trans_railway(w),
            ## NOTE
            ##  - ブロイセルの街にやってきた
            ##  - 何とかチケットを手に入れようとするが
            ##  - 大陸鉄道に乗り、首都を目指す
            note="ブロイセルの街にやってきたアルたちだったが、そこで初めての人の悪意を体験することになる")
