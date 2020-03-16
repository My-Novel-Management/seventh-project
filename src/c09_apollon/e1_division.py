# -*- coding: utf-8 -*-
"""Episode: 9-1.分断
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
def sc_entering(w: World):
    alt, vega, deneb = W(w.altair), W(w.vega), W(w.deneb)
    return w.scene("雪山へ",
            camera=w.altair,
            stage=w.on_mtsnow,
            day=w.in_entermount, time=w.at_morning,
            )

def sc_leaving_vega(w: World):
    return w.scene("$vegaを置いていくか",
            )

def sc_conference(w: World):
    return w.scene("$vegaの処遇",
            )

## episode
def ep_division(w: World):
    return w.episode("9-1.分断",
            sc_entering(w),
            sc_leaving_vega(w),
            sc_conference(w),
            ## NOTE
            ##  - 雪山に突入した
            ##  - ベガのギアが動かなくなり、カノープスは置いていこうと言い出す
            ##  - 相談した結果、二手に分かれることになる
            note="雪山に入り、ベガのギアが不調をきたして動かなくなる")
