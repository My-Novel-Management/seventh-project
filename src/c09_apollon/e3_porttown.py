# -*- coding: utf-8 -*-
"""Episode: 9-3.港町
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
def sc_descent(w: World):
    alt, vega, deneb = W(w.altair), W(w.vega), W(w.deneb)
    return w.scene("下山",
            camera=w.altair,
            stage=w.on_mtsnow,
            day=w.in_descent, time=w.at_afternoon,
            )

def sc_vanish_canopus(w: World):
    return w.scene("$canopusは消えた",
            )

def sc_porttown(w: World):
    return w.scene("港町",
            )

## episode
def ep_porttown(w: World):
    return w.episode("9-3.港町",
            ## NOTE
            ##  - 下山して合流するとカノープスの姿がなかった
            ##  - デネブからカノープスが一人で先に行ったことを聞く
            ##  - 港町に入り、情報を集める。干潮時に現れる島が楽園と呼ばれていることを知る
            note="下山すると$canopusの姿はなく、合流して元の七人で港町に入った。そこで島に楽園があることを知る")
