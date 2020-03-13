# -*- coding: utf-8 -*-
"""Episode: 4-2.チケット
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
def ep_ticket(w: World):
    return w.episode("4-2.チケット",
            ## NOTE
            ##  - 偽チケットを掴まされ、有り金がなくなったアルたち
            ##  - 何とかチケットを手に入れる方法を模索するも見つからない
            ##  - 質屋でギアを質入れして、闇チケットを手に入れた
            note="何とか大陸鉄道のチケットを手に入れようと店を巡るが、どこも扱っていない。そんな中、$denebが質屋に行くことを提案する")
