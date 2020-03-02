# -*- coding: utf-8 -*-
"""Chapter: 12.ゼウスの空虚
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
def ch_zeus(w: World):
    return w.chapter("ゼウスの空虚",
            ## NOTE: 教授による説明
            note="アルの前に現れた教授はセブンス・プロジェクトの本当の目的について語り始める")
