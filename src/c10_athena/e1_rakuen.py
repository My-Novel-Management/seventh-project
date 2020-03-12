# -*- coding: utf-8 -*-
"""Episode: 10-1.楽園
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
def ep_rakuen(w: World):
    return w.episode("10-1.楽園",
            ## NOTE
            ##  - 楽園へとやってくるアルたち。そこで待っていたのは教授とアトリアによく似たスタッフたちだった
            ##  - 楽園を案内される。以前の第七ラボによく似た形で、またラボでの暮らしが戻ると喜ぶアルたち
            ##  - 教授は施設での生活の規則を教えた。それは常に試験され成績が表示されるというものだった
            note="ついに楽園に到着した$altairたちを待っていたのは、教授たちだった")
