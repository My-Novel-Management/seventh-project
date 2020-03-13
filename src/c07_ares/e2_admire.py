# -*- coding: utf-8 -*-
"""Episode: 7-2.憧れ
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
def ep_admire(w: World):
    return w.episode("7-2.憧れ",
            ## NOTE
            ##  - スピカはリーダーに惹かれていた
            ##  - ベガはスピカから恋愛の相談をされるが、うまく答えられなかった
            ##  - スピカとリーダーは明け方、村を出ていってしまった
            note="遊牧民のリーダーと共に駆け落ちして村を出ていってしまう$spica")
