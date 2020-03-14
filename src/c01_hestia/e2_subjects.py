# -*- coding: utf-8 -*-
"""Episode: 1-2.被験者
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
def ep_subjects(w: World):
    return w.episode("1-2.被験者",
            ## NOTE
            ##  - 実習を終え、アルはアトリアを探していた
            ##  - ベガの悲鳴に駆けつけると、そこには小さな蜘蛛に似たマシンがいた
            ##  - アトリアからこの世界の管理について教わる
            note="施設内を歩いていた$altairは$vegaが奇妙なものを見つけたところに遭遇する。それはとても小さな$w_mushiと呼ばれるドローンだった")
