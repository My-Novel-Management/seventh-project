# -*- coding: utf-8 -*-
"""Episode: 11-2.リゲルの遺言
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
def ep_goodbye(w: World):
    return w.episode("11-2.別離",
            ## NOTE
            ##  - スピカが消えたことに不信感を持ったリゲルはある提案をする
            ##  - リゲルはわざと最下位になる
            ##  - 翌朝リゲルは姿を消した。アルにメッセージを残して
            note="$rigelは$spicaが消えたことで不信感を持ち、わざと最下位になろうとする")
