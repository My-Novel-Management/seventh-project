# -*- coding: utf-8 -*-
"""Episode: 10-2.競争社会
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
def ep_competitive(w: World):
    return w.episode("10-2.競争社会",
            ## NOTE
            ##  - 楽園での生活が始まる。ただ以前と違い、常に試験され、成績が表示されるという有様
            ##  - アトリアによく似たスタッフがいたが、アルたちに対する態度が全然違っていた
            ##  - アルはこの生活に違和感を抱く
            note="楽園での生活が始まったが、よく似たスタッフたちと試験の日々は$altairたちに奇妙な感情を抱かせた")
