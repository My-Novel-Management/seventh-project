# -*- coding: utf-8 -*-
"""Episode: 10-3.最初の死者
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
def sc_fallingdown(w: World):
    alt, vega, deneb = W(w.altair), W(w.vega), W(w.deneb)
    return w.scene("落ちこぼれ",
            camera=w.altair,
            stage=w.on_rakuen_int,
            day=w.in_rakuen2, time=w.at_morning,
            )

def sc_lowest(w: World):
    alt, vega, deneb = W(w.altair), W(w.vega), W(w.deneb)
    return w.scene("最下位",
            )

def sc_vanish_capella(w: World):
    return w.scene("そして$capellaが消えた",
            )

## episode
def ep_firstdead(w: World):
    return w.episode("10-3.最初の死者",
            sc_fallingdown(w),
            sc_lowest(w),
            sc_vanish_capella(w),
            ## NOTE
            ##  - カペラが最下位になる
            ##  - 翌日、カペラが姿を消していた
            note="試験結果が悪い$capellaが最下位となったその翌日、姿を消した")
