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

## defines
W = Writer
_ = W.getWho()


## main
def ch_ares(w: World):
    return w.chapter("アレスの悲哀",
            ## NOTE
            ##  - 砂漠をバギーで横断するアルたちは、途中のオアシスの村に立ち寄る
            ##  - 遊牧民の若きリーダーに恋をしたスピカは駆け落ちしてしまう
            ##  - 結局戻ってきたスピカと共にオアシスを後にする
            note="砂漠を横断中、遊牧民の村にやってきたアルたち。そこでスピカは恋に落ちる")
