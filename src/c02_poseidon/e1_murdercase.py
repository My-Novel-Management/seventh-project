# -*- coding: utf-8 -*-
"""Episode: 2-1.殺人事件
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
def ep_murdercase(w: World):
    return w.episode("2-1.殺人事件",
            ## NOTE
            ##  - アトリアが殺されていることを知り、アルはリゲルと共に犯人を探すことに
            ##  - リゲルと共にイザールの部屋に向かうが開かない
            ##  - ベガが蟲型に襲われていた
            note="$atriaが殺されていた。$altairは犯人を探して施設を回るが")
