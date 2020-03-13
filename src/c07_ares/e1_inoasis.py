# -*- coding: utf-8 -*-
"""Episode: 7-1.オアシス
"""
## path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer


## define alias
W = Writer
_ = W.getWho()


## scenes

## episode
def ep_in_oasis(w: World):
    return w.episode("7-1.オアシス",
            ## NOTE
            ##  - 砂漠をバギーで横断していたが、途中で調子悪くなる
            ##  - オアシスの村に立ち寄る。そこは砂漠の遊牧民が暮らす集落だった
            ##  - 遊牧民のリーダーに頼られ、バギーの修理を頼む代わりに村の仕事をいくつか手伝う
            note="砂漠を横断する途中で、$altairたちはオアシスの集落に入る")
