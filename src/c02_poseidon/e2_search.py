# -*- coding: utf-8 -*-
"""Episode: 2-2.犯人探し
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
def ep_search(w: World):
    return w.episode("2-2.捜索",
            ## NOTE
            ##  - 犯人を手分けして探すアルたち
            ##  - 蟲型に襲われていたベガを助け出す
            ##  - イザールも亡くなっていた
            note="ラボ施設内をくまなく手分けして探す$altairたち。しかし誰も見つけられない")
