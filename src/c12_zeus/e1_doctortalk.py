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
def sc_selection(w: World):
    alt, vega, deneb = W(w.altair), W(w.vega), W(w.deneb)
    return w.scene("選ばれし者",
            camera=w.altair,
            stage=w.on_rakuen_int,
            day=w.in_rakuen7, time=w.at_morning,
            )

def sc_purpose(w: World):
    return w.scene("プロジェクトの目的",
            )

def sc_true_culprit(w: World):
    return w.scene("真犯人",
            )

## episode
def ep_doc_talk(w: World):
    return w.episode("12-1.教授の話",
            sc_selection(w),
            sc_purpose(w),
            sc_true_culprit(w),
            ## NOTE
            ##  - 現れた教授はアルが選ばれたセブンスだと告げる
            ##  - 教授はセブンス・プロジェクトがセブンス・サピエンスを選抜する為の試験だったと告げる
            ##  - ベガがそこに現れ、教授を殺した
            note="教授は$altairが勝ち残ったことを伝え、セブンス・プロジェクトの全容を語る")
