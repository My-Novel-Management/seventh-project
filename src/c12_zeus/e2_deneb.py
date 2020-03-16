# -*- coding: utf-8 -*-
"""Episode: 12-2.デネブ
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
def sc_Immother(w: World):
    alt, vega, deneb = W(w.altair), W(w.vega), W(w.deneb)
    return w.scene("私がマザー",
            camera=w.altair,
            stage=w.on_rakuen_int,
            day=w.in_rakuen7, time=w.at_morning,
            )

def sc_trueproject(w: World):
    return w.scene("プロジェクトの真意",
            )

def sc_denebrequest(w: World):
    return w.scene("デネブの依頼",
            )

## episode
def ep_deneb(w: World):
    return w.episode("12-2.デネブ：告白",
            sc_Immother(w),
            sc_trueproject(w),
            sc_denebrequest(w),
            ## NOTE
            ##  - 教授を殺したデネブは、自分がマザーであることを語る
            ##  - デネブは本当のセブンス・プロジェクトを語る
            ##  - アルとベガに新世界のアダムとイブとなるよう要請した
            note="セブンス・プロジェクトの真実を語った$denebは$altairと$vegaに新世界のアダムとイブになるよう要請した")
