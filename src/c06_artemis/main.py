# -*- coding: utf-8 -*-
"""Chapter: 6.アルテミスの後悔
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
def ch_artemis(w: World):
    return w.chapter("アルテミスの後悔",
            ## NOTE
            ##  - 首都にやってきたアルたちは蟲型により壊滅的な状況を目の当たりにする
            ##  - 民間警備隊のデネボラに助けられ、話を聞くアルたち
            ##  - デネボラに見送られ、首都を旅立つ
            note="首都に到着したアルたち。そこで再び蟲型に襲われるも、デネボラによって助けられた")
