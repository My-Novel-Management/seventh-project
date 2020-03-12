# -*- coding: utf-8 -*-
"""Chapter: 7.アレスの悲哀
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
## local files
from src.c07_ares.e1_inoasis import ep_in_oasis
from src.c07_ares.e2_admire import ep_admire
from src.c07_ares.e3_heartbreak import ep_heartbreak
## defines
W = Writer
_ = W.getWho()


## main
def ch_ares(w: World):
    return w.chapter("第七章　アレスの悲哀",
            ep_in_oasis(w),
            ep_admire(w),
            ep_heartbreak(w),
            ## NOTE
            ##  - 砂漠をバギーで横断するアルたちは、途中のオアシスの村に立ち寄る
            ##  - 遊牧民の若きリーダーに恋をしたスピカは駆け落ちしてしまう
            ##  - 結局戻ってきたスピカと共にオアシスを後にする
            note="砂漠を横断中、遊牧民の村にやってきたアルたち。そこでスピカは恋に落ちる")
