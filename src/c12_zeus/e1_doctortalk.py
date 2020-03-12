# -*- coding: utf-8 -*-
"""Episode: 12-1.教授の話
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
def ep_doc_talk(w: World):
    return w.episode("12-1.教授の話",
            ## NOTE
            ##  - 現れた教授はアルが選ばれたセブンスだと告げる
            ##  - 教授はセブンス・プロジェクトがセブンス・サピエンスを選抜する為の試験だったと告げる
            ##  - ベガがそこに現れ、教授を殺した
            note="教授は$altairが勝ち残ったことを伝え、セブンス・プロジェクトの全容を語る")
