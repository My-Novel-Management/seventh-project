# -*- coding: utf-8 -*-
"""Chapter: 4.ヘパイストスの焦燥
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
def ch_hephaistos(w: World):
    return w.chapter("ヘパイストスの焦燥",
            ## NOTE
            )
