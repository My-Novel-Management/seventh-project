# -*- coding: utf-8 -*-
"""Chapter: 9.アポロンの殺意
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
## local files
from src.c09_apollon.e1_division import ep_division
from src.c09_apollon.e2_eachthought import ep_eachthought
from src.c09_apollon.e3_porttown import ep_porttown
## defines
W = Writer
_ = W.getWho()


## main
def ch_apollon(w: World):
    return w.chapter("第九章　アポロンの殺意",
            ep_division(w),
            ep_eachthought(w),
            ep_porttown(w),
            ## NOTE
            ##  - 雪山に入り、ベガがギアの不調を訴え、動けなくなる
            ##  - 置いていくというカノープスと意見が割れ、二班に分かれて行動することになったアルたち
            ##  - 何とか下山すると、先行班にカノープスの姿はなかった
            note="カノープスを加えて雪山に向かったが、途中でベガのギアが不調になり、二班に分裂してしまう")
