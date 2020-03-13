# -*- coding: utf-8 -*-
"""Episode: 4-1.ブロイセル
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
def ep_breuccel(w: World):
    return w.episode("4-1.ブロイセル",
            ## NOTE
            ##  - ラボを出たアルたちは初めての野営をこなし、何とか一番近い街を目指す
            ##  - 大陸鉄道の始発駅があるブロイセルにやってきた
            ##  - 大陸鉄道にはチケットを求める人が列を成していて、手に入らないと嘆いていた
            note="$on_breuccelに到着した$altairたちは大陸鉄道のチケットを手に入れようとするが")
