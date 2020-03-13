# -*- coding: utf-8 -*-
"""Episode: 5-1.蟲型襲来
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
def ep_insect_attack(w: World):
    return w.episode("5-1.蟲型襲来",
            ## NOTE
            ##  - 大陸鉄道で首都を目指しているが途中で蟲型に襲われた
            ##  - 何とか鉄道から逃げ出して最寄りの街に逃げ込む
            ##  - 鉄道以外の手段がなく、途方に暮れるアルたち
            note="大陸鉄道で首都に向かう途中、$w_mushiに襲われ大破してしまう")
