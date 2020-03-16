# -*- coding: utf-8 -*-
"""Episode: 11-1.抗議
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
def sc_vanish_capella(w: World):
    alt, vega, deneb = W(w.altair), W(w.vega), W(w.deneb)
    return w.scene("$capellaの消失",
            camera=w.altair,
            stage=w.on_rakuen_int,
            day=w.in_rakuen2, time=w.at_morning,
            )

def sc_rebellion(w: World):
    return w.scene("疑念と反抗",
            )

def sc_vanish_spica(w: World):
    return w.scene("そして$spicaも消えた",
            )

## episode
def ep_exception(w: World):
    return w.episode("11-1.抗議",
            sc_vanish_capella(w),
            sc_rebellion(w),
            sc_vanish_spica(w),
            ## NOTE
            ##  - カペラが姿を消して動揺するアルたち
            ##  - スピカはカペラを探そうとするが邪魔され、反抗して全部の授業をさぼった
            ##  - 最下位になったスピカも姿を消してしまった
            note="カペラが姿を消し、反抗的な態度のスピカは翌日最下位になり、姿を消した")
