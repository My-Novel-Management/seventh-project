# -*- coding: utf-8 -*-
"""Chapter: 11.ヘラの嫉妬
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
## local files

## defines
W = Writer
_ = W.getWho()


## main
def ch_hera(w: World):
    return w.chapter("ヘラの嫉妬",
            ## NOTE
            ##  - カペラが姿を消し、不審に思ったスピカはわざと最下位になる
            ##  - 消えたスピカから隠しメッセージをもらい、アルも最下位になる決意をする
            ##  - 最下位になったアルの前に教授が現れた
            note="最下位になったスピカが姿を消し、次々に脱落者が出る")
