# -*- coding: utf-8 -*-
"""Episode: 8-1.山道
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
def ep_mount_path(w: World):
    return w.episode("8-1.山道",
            ## NOTE
            ##  - 山岳地帯に入ったアルたち。しかし野営中に荷物を何者かに盗まれた
            ##  - その後も何度も荷物がなくなり、仲間を疑う声も出始める
            ##  - スピカは襲撃者の足音を聞いた
            note="山岳地帯に入った$altairたちだったが何度か荷物が奪われる事件が発生する")
