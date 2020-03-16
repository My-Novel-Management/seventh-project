# -*- coding: utf-8 -*-
"""Episode: 11-3.殺人鬼の正体
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
def sc_hismessage(w: World):
    alt, vega, deneb = W(w.altair), W(w.vega), W(w.deneb)
    return w.scene("$rigelのメッセージ",
            camera=w.altair,
            stage=w.on_rakuen_int,
            day=w.in_rakuen5, time=w.at_morning,
            )

def sc_testing(w: World):
    return w.scene("$altairの挑戦",
            )

def sc_waiting_the_murder(w: World):
    return w.scene("犯人を待ちながら",
            )

## episode
def ep_murder_true(w: World):
    return w.episode("11-3.正体",
            sc_hismessage(w),
            sc_testing(w),
            sc_waiting_the_murder(w),
            ## NOTE
            ##  - 最下位になったカペラが姿を消した
            ##  - リゲルはアルにわざと最下位になるとメッセージを残し、消える
            ##  - アルはわざと最下位になり、殺人犯人を確かめようとするが
            note="$capellaが姿を消し、不審に思った$rigelはわざと最下位になり消える。$altairはその謎を解く為にわざと最下位になる")
