# -*- coding: utf-8 -*-
"""Main story.
"""
## path setting
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
## public libs
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
## assets
from storybuilder.assets import accessory, basic
from config import AREAS, DAYS, ITEMS, LAYERS, PERSONS, RUBIS, STAGES, TIMES, WORDS
## local files
from src.c01_hestia.main import ch_hestia
from src.c02_poseidon.main import ch_poseidon
from src.c03_hermes.main import ch_hermes
from src.c04_hephaistos.main import ch_hephaistos
from src.c05_demeter.main import ch_demeter
from src.c06_artemis.main import ch_artemis
from src.c07_ares.main import ch_ares
from src.c08_aphrodite.main import ch_aphrodite
from src.c09_apollon.main import ch_apollon
from src.c10_athena.main import ch_athena
from src.c11_hera.main import ch_hera
from src.c12_zeus.main import ch_zeus

## define alias
W = Writer
_ = Writer.getWho()

################################################################
#
# Sample step:
# 1) Create the world
#       世界を作成する。
# 2) Create a new chapter
#       章の作成。
# 3) Create a episode
#       エピソード作成。
# 4) Create a new scene
#       シーン作成。物語のベース。ここに様々なActionを追加する。
# 5) Create a new stage
#       舞台作成。シーンに必須要素
# 6) Create a new day and time
#       日時作成。シーンのサブ要素
# 7) Add a scene plot
#       シーンプロットの作成。概要のないシーンは原則使えない
# 8) Add scene actions
#       シーンアクションの追加。
#
################################################################


## main
def create_world():
    """Create a world.
    """
    w = World("セブンス・サピエンス")
    w.setCommonData()
    w.setAssets(basic.ASSET)
    w.setAssets(accessory.ASSET)
    w.buildDB(PERSONS,
            AREAS, STAGES, ITEMS, DAYS, TIMES, WORDS,
            RUBIS, LAYERS)
    # w.setBaseDate()
    # w.setBaseArea()
    # set textures
    # w.entryBlock()
    # w.entryHistory()
    # w.entryLifeNote()
    w.setOutline("機械と人類が融合し、第六人類と呼ばれる新しい人間たちが暮らしていた。しかしその研究所では次なる第七人類を目指し、子どもたちを集め、実験がなされていた。だがある日、通信網が一斉に途切れ、世界は混乱する")
    return w


def main(): # pragma: no cover
    w = create_world()
    return w.build(
            ch_hestia(w),
            ch_poseidon(w),
            ch_hermes(w),
            ch_hephaistos(w),
            ch_demeter(w),
            ch_artemis(w),
            ch_ares(w),
            ch_aphrodite(w),
            ch_apollon(w),
            ch_athena(w),
            ch_hera(w),
            ch_zeus(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

