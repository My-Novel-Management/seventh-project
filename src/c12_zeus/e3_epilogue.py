# -*- coding: utf-8 -*-
"""Episode: 12-3.エピローグ
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
def sc_decision(w: World):
    alt, vega, deneb = W(w.altair), W(w.vega), W(w.deneb)
    return w.scene("決断",
            camera=w.altair,
            stage=w.on_rakuen_int,
            day=w.in_rakuen7, time=w.at_morning,
            )

def sc_escape(w: World):
    return w.scene("脱出",
            )

def sc_voyage(w: World):
    return w.scene("新しい世界へ",
            )

## episode
def ep_epilogue(w: World):
    return w.episode("12-3.エピローグ：決断",
            sc_decision(w),
            sc_escape(w),
            sc_voyage(w),
            ## NOTE
            ##  - デネブ（マザー）の要求を受け入れないアルたち
            ##  - 楽園を出て、荒廃した世界で自分たちのように残る者を探して旅に出た。一方楽園は宇宙へと飛び立つ
            note="デネブの要請を断り、アルとベガは二人で生き残った人々を探して旅立った")
