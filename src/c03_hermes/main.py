# -*- coding: utf-8 -*-
"""Chapter: 3.ヘルメスの驚愕
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
def ch_hermes(w: World):
    return w.chapter("ヘルメスの驚愕",
            ## NOTE
            note="教授の衝撃のメッセージにより脱出することになったアルたち。だがラボの外には大量の蟲型が迫っていた")
