from ichingpy.enum.five_phase import FivePhase
from ichingpy.enum.mixed_enum import MixEnum


class Palace(MixEnum):

    HEAVEN = 1, "乾"
    LAKE = 2, "兑"  # TODO: find a better name in English
    FIRE = 3, "离"
    THUNDER = 4, "震"
    WIND = 5, "巽"
    WATER = 6, "坎"
    MOUNTAIN = 7, "艮"
    EARTH = 8, "坤"

    @property
    def phase(self) -> FivePhase:
        PALACE_PHASE_MAPPING = {
            1: FivePhase.METAL,  # "乾"
            2: FivePhase.METAL,  # "兑"
            3: FivePhase.FIRE,  # "离"
            4: FivePhase.WOOD,  # "震"
            5: FivePhase.WOOD,  # "巽"
            6: FivePhase.WATER,  # "坎"
            7: FivePhase.EARTH,  # "艮"
            8: FivePhase.EARTH,  # "坤"
        }
        return PALACE_PHASE_MAPPING[self.value]
