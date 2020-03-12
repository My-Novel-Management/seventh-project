# -*- coding: utf-8 -*-
"""Chapter: 1.ヘスティアの畏怖
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
## local files
from src.c01_hestia.e1_7th import ep_7th
from src.c01_hestia.e2_subjects import ep_subjects
from src.c01_hestia.e3_leftchildren import ep_left_children
## defines
W = Writer
_ = W.getWho()


## main
def ch_hestia(w: World):
    return w.chapter("ヘスティアの畏怖",
            ep_7th(w),
            ep_subjects(w),
            ep_left_children(w),
            ## NOTE
            ##  - 人類と機械が融合した第六世代が地表を覆っていた。そんな中で第七ラボと呼ばれる実験施設にワケアリの子どもたちが匿われていた
            ##  - アルたちは次なる世代セブンス・サピエンスの可能性を探る為の被験体だった
            ##  - 教授たちが出かけた翌日、スタッフの一人であるアトリアが何者かに殺されていた
            note="第七ラボ。そこではセブンス・サピエンスの研究と実験が行われていた")
