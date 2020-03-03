# -*- coding: utf-8 -*-
"""Episode: 9-2.互いの気持ち
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
def ep_eachthought(w: World):
    return w.episode("2.互いの気持ち",
            ## NOTE
            )
