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
            )
