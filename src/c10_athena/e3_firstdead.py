# -*- coding: utf-8 -*-
"""Episode: 10-3.最初の死者
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
def ep_firstdead(w: World):
    return w.episode("10-3.最初の死者",
            ## NOTE
            ##  - カペラが最下位になる
            ##  - 翌日、カペラが姿を消していた
            note="試験結果が悪い$capellaが最下位となったその翌日、姿を消した")
