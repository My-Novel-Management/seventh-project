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
from src.c12_zeus.e_deneb import ep_deneb
from src.c12_zeus.e_doctortalk import ep_doc_talk
from src.c12_zeus.e_epilogue import ep_epilogue
## defines
W = Writer
_ = W.getWho()


## main
def ch_zeus(w: World):
    return w.chapter("ゼウスの空虚",
            ep_doc_talk(w),
            ep_deneb(w),
            ep_epilogue(w),
            ## NOTE: 教授による説明
            ##  - 教授によりセブンス・プロジェクトの説明がされる
            ##  - 教授が殺され、デネブ＝マザーが真実を語る
            ##  - アルとベガが新世代のアダムとイブになると言われた
            ##  - アルとベガは生き残っている人々を探して再び旅立つ
            note="アルの前に現れた教授はセブンス・プロジェクトの本当の目的について語り始める")
