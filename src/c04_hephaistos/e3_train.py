# -*- coding: utf-8 -*-
"""Episode: 4-3.大陸横断鉄道
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
def ep_trans_railway(w: World):
    return w.episode("4-3.大陸横断鉄道",
            ## NOTE
            ##  - 何とかチケットを手に入れ、駅にやってくる
            ##  - 無事に席を確保し、大陸鉄道に乗車する
            ##  - 大陸鉄道に乗車し、首都を目指して発車した
            note="何とか大陸鉄道に乗り込み、首都を目指す")
