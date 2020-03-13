# -*- coding: utf-8 -*-
"""Episode: 7-3.失恋
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
def ep_heartbreak(w: World):
    return w.episode("7-3.失恋",
            ## NOTE
            ##  - 姿を消した$spicaを探そうという$vegaと置いておこうという$altairで対立する
            ##  - 結局戻ってきた$spica。事情を少しだけ話す
            ##  - 再び七人になり、出発する
            note="戻ってきた$spicaと合流し、再び旅立つ$altairたち")
