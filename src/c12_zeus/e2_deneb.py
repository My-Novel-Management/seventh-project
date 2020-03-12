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

## episode
def ep_deneb(w: World):
    return w.episode("12-2.デネブ：告白",
            ## NOTE
            ##  - 教授を殺したデネブは、自分がマザーであることを語る
            ##  - デネブは本当のセブンス・プロジェクトを語る
            ##  - アルとベガに新世界のアダムとイブとなるよう要請した
            note="セブンス・プロジェクトの真実を語った$denebは$altairと$vegaに新世界のアダムとイブになるよう要請した")