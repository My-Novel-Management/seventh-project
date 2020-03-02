# -*- coding: utf-8 -*-
"""Chapter: 11.ヘラの嫉妬
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
def ch_hera(w: World):
    return w.chapter("ヘラの嫉妬",
            ## NOTE
            note="最下位になったスピカが姿を消し、次々に脱落者が出る")
