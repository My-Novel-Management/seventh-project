# -*- coding: utf-8 -*-
"""Episode: 8-2.カノープス
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
def ep_canopus(w: World):
    return w.episode("8-2.カノープス",
            ## NOTE
            ##  - 追い詰められた襲撃者はベガを人質に取った
            ##  - ベガを人質にとった襲撃者を何とか撃退し、捕まえる
            ##  - 襲撃者は自分が別のセブンスの生き残りだと名乗った
            note="$altairたちを襲ったのは別のセブンスの生き残り、$canopusだった")
