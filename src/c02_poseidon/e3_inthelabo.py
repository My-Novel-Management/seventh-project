# -*- coding: utf-8 -*-
"""Episode: 2-3.研究室
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
def ep_in_the_labo(w: World):
    return w.episode("2-3.研究室",
            ## NOTE
            ##  - 決して入ってはいけなかった研究室を調べようと言い出す
            ##  - あとは研究室しか残っていない。何とかして研究室に入ろうとする
            ##  - 研究室に入ったアルたちを待っていたのは教授の映像だった
            note="$atriaを殺した犯人がいる、と踏み込んだ研究室で教授の映像が喋りだした")
