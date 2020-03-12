# -*- coding: utf-8 -*-
"""Episode: 6-1.崩壊都市
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
def ep_collapsed_city(w: World):
    return w.episode("6-1.崩壊都市",
            ## NOTE
            )
