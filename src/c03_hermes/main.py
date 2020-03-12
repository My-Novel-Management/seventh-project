# -*- coding: utf-8 -*-
"""Chapter: 3.ヘルメスの驚愕
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
## local files
from src.c03_hermes.e1_message import ep_message
from src.c03_hermes.e2_escape import ep_escape_labo
from src.c03_hermes.e3_explosion import ep_explosion_labo
## defines
W = Writer
_ = W.getWho()


## main
def ch_hermes(w: World):
    return w.chapter("ヘルメスの驚愕",
            ep_message(w),
            ep_escape_labo(w),
            ep_explosion_labo(w),
            ## NOTE
            ##  - 教授のメッセージで脱出しなければならないと知る
            ##  - 出入り口は蟲型により封鎖され、別の出口を探さなければならなくなる
            ##  - ラボの外に脱出したアルが見たのは、爆発する建物だった
            note="教授の衝撃のメッセージにより脱出することになったアルたち。だがラボの外には大量の蟲型が迫っていた")
