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
            )
