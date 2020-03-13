# -*- coding: utf-8 -*-
"""Episode: 3-1.教授の伝言
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
def ep_message(w: World):
    return w.episode("3-1.メッセージ",
            ## NOTE
            ##  - 教授のメッセージが再生される
            ##  - ラボを脱出しなければならないと言われる
            ##  - 爆破までのカウントダウンが始まり、慌てて逃げ出すアルたち
            note="教授のメッセージで楽園を目指し、ラボを脱出しなければならないと知る")
