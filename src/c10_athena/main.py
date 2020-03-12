# -*- coding: utf-8 -*-
"""Chapter: 10.アテナの優越
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
## local files
from src.c10_athena.e1_rakuen import ep_rakuen
from src.c10_athena.e2_competitive import ep_competitive
from src.c10_athena.e3_firstdead import ep_firstdead
## defines
W = Writer
_ = W.getWho()


## main
def ch_athena(w: World):
    return w.chapter("第十章　アテナの優越",
            ep_rakuen(w),
            ep_competitive(w),
            ep_firstdead(w),
            ## NOTE
            ##  - 楽園で、またラボのような生活が始まると思っていたら、始まったのは新たな試験だった
            ##  - 楽園にはアトリアによく似たスタッフたちがいたが、以前は感じなかった違和感をアルたちは覚えていた
            ##  - 最下位になったカペラが姿を消した
            note="ついに楽園へと到達したアルたち。そこでは教授やアトリアによく似たスタッフたちが待っていた")
