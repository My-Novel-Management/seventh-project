# -*- coding: utf-8 -*-
"""Episode: 3-3.爆発
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
def ep_explosion_labo(w: World):
    return w.episode("3-3.爆発",
            ## NOTE
            ##  - アルが抜け穴を一人で進む
            ##  - 途中で連絡も取れなくなるが、何とか出口を見つけて登る
            ##  - 外に出たところでラボは爆発した
            note="ラボの外に出た$altairは爆発し、折れてしまう建物を確認した")
