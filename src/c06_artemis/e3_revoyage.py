# -*- coding: utf-8 -*-
"""Episode: 6-3.再びの旅立ち
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
def ep_re_voyage(w: World):
    return w.episode("6-3.再びの旅立ち",
            ## NOTE
            ##  - デネボラは結局アルたちと一緒に行くことは選択せず、残ると言った
            ##  - デネボラに色々と食料などを分けてもらう
            ##  - バギーで砂漠横断に挑む
            note="$denebolaに見送られ、バギーを借りて砂漠へと向かう")
