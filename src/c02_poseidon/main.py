# -*- coding: utf-8 -*-
"""Chapter: 2.ポセイドンの憤怒
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
def ch_poseidon(w: World):
    return w.chapter("ポセイドンの憤怒",
            ## NOTE
            )
