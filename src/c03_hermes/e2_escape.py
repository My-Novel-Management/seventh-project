# -*- coding: utf-8 -*-
"""Episode: 3-2.脱出
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
def ep_escape_labo(w: World):
    return w.episode("3-2.脱出",
            ## NOTE
            ##  - 出口が封鎖されていることが分かり、一旦食堂に引っ込む
            ##  - 何とか他の出口を探すアルたち
            ##  - アルは見つけた抜け穴を一人で進むことにした
            note="唯一の出口は$w_mushiにより封鎖され、別の出口を探さなければならなくなる")
