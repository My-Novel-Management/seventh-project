# -*- coding: utf-8 -*-
"""Chapter: 8.アプロディテの疑念
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
def ch_aphrodite(w: World):
    return w.chapter("アプロディテの疑念",
            ## NOTE
            ##  - 山道に入ったアルたち。だが野営中に何者かに襲われる
            ##  - 襲ったのは別のセブンスの生き残り、カノープスだった
            ##  - カノープスを連れて行くか議論になる
            note="山岳地帯に入ったアルたちだが、野営中に誰かに襲われる。それは別のセブンスの生き残りだった")
