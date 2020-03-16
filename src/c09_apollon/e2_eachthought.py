# -*- coding: utf-8 -*-
"""Episode: 9-2.互いの気持ち
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
def sc_division(w: World):
    alt, vega, deneb = W(w.altair), W(w.vega), W(w.deneb)
    return w.scene("分裂",
            camera=w.altair,
            stage=w.on_mtsnow,
            day=w.in_division_party, time=w.at_afternoon,
            )

def sc_upset_vega(w: World):
    return w.scene("$vegaの不調",
            )

def sc_with_vega(w: World):
    return w.scene("みんなで一緒に",
            )

## episode
def ep_eachthought(w: World):
    return w.episode("9-2.互いの気持ち",
            sc_division(w),
            sc_upset_vega(w),
            sc_with_vega(w),
            ## NOTE
            ##  - 二手に分かれた
            ##  - ベガは途中で歩けなくなり、自分を置いていくように言う
            ##  - アルたちはベガを担いで一緒に行くことを選んだ
            note="別別に分かれて行動することになる。$vegaは自分を置いていって欲しいと懇願するが$altairたちは担いで連れて行く")
