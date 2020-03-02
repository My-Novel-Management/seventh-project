# -*- coding: utf-8 -*-
"""Chapter: 6.アルテミスの後悔
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
def ch_artemis(w: World):
    return w.chapter("アルテミスの後悔",
            ## NOTE
            note="首都に到着したアルたち。そこで再び蟲型に襲われるも、デネボラによって助けられた")
