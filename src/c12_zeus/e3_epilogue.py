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

## episode
def ep_epilogue(w: World):
    return w.episode("12-3.エピローグ：決断",
            ## NOTE
            ##  - デネブ（マザー）の要求を受け入れないアルたち
            ##  - 楽園を出て、荒廃した世界で自分たちのように残る者を探して旅に出た。一方楽園は宇宙へと飛び立つ
            note="デネブの要請を断り、アルとベガは二人で生き残った人々を探して旅立った")
