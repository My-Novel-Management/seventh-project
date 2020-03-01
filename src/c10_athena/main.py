# -*- coding: utf-8 -*-
"""Chapter: 10.アテナの優越
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
def ch_athena(w: World):
    return w.chapter("アテナの優越",
            ## NOTE
            )
