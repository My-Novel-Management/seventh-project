# -*- coding: utf-8 -*-
"""Episode: 8-3.新しい仲間
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
def ep_new_member(w: World):
    return w.episode("8-3.新しい仲間",
            ## NOTE
            ##  - カノープスをどうするか、相談になる
            ##  - カノープスを一緒に連れて行くことが決まり、街で雪山を超えなければならないと知る
            note="$canopusを仲間として迎え、一緒に楽園を目指すことになった")
