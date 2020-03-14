# -*- coding: utf-8 -*-
"""Episode: 1-3.残された子どもたち
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
def ep_left_children(w: World):
    return w.episode("1-3.残された子どもたち",
            ## NOTE
            ##  - 教授たち主要スタッフが出張でラボを出ていく
            ##  - 残されたアルたちはアトリアと共に楽しむ
            ##  - 翌朝、アトリアの部屋に行くと彼女は死んでいた
            note="教授たちが出ていった翌日、$atriaが殺されているのを発見した")
