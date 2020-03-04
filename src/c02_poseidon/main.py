# -*- coding: utf-8 -*-
"""Chapter: 2.ポセイドンの憤怒
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
## local files
from src.c02_poseidon.e_inthelabo import ep_in_the_labo
from src.c02_poseidon.e_murdercase import ep_murdercase
from src.c02_poseidon.e_search import ep_search
## defines
W = Writer
_ = W.getWho()


## main
def ch_poseidon(w: World):
    return w.chapter("ポセイドンの憤怒",
            ep_murdercase(w),
            ep_search(w),
            ep_in_the_labo(w),
            ## NOTE
            ##  - アトリアが殺され、その犯人を探すアル
            ##  - スタッフが全て殺され、アルたちだけが施設に残されていることを知る
            ##  - 意を確かめる為に研究室に入ったアルたちを待ち構えていたのは教授のメッセージ映像だった
            note="アトリアが殺された。だが教授たちはいない。残されたアルたちは犯人探しを始めるが")
