# -*- coding: utf-8 -*-
"""Chapter: 1.ヘスティアの畏怖
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
def ch_hestia(w: World):
    return w.chapter("ヘスティアの畏怖",
            ## NOTE
            note="第七ラボ。そこではセブンス・サピエンスの研究と実験が行われていた")
