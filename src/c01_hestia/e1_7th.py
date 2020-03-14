# -*- coding: utf-8 -*-
"""Episode: 1-1.第七世代
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
def ep_7th(w: World):
    return w.episode("1-1.第七世代",
            ## NOTE
            ##  - 第六世代により地表が埋め尽くされ、数多のドローンが生活を支えている世界
            ##  - ラボと呼ばれる実験施設に集められた一人、アルは盲目の少年だった
            ##  - それぞれ欠陥のある子どもたちにギアと呼ばれる補助ツールを与え、次なる世代セブンスを生み出す為に日々研究と勉強が続けられていた
            note="人類と機械が融合したシンギュラリティにより第六世代と呼ばれる新人類が地表を覆っていた。そんな中、次なる世代セブンス・サピエンスを育成すべくラボに少年少女が集められていた")
