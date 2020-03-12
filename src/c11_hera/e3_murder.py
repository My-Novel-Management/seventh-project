# -*- coding: utf-8 -*-
"""Episode: 11-3.殺人鬼の正体
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
def ep_murder_true(w: World):
    return w.episode("11-3.正体",
            ## NOTE
            ##  - 最下位になったカペラが姿を消した
            ##  - リゲルはアルにわざと最下位になるとメッセージを残し、消える
            ##  - アルはわざと最下位になり、殺人犯人を確かめようとするが
            note="$capellaが姿を消し、不審に思った$rigelはわざと最下位になり消える。$altairはその謎を解く為にわざと最下位になる")
