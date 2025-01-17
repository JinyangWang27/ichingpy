# %%
import importlib.resources
import json

from ichingpy.divination.base import DivinationEngineBase
from ichingpy.model.hexagram import Hexagram
from ichingpy.model.interpretation.hexagram.iching_hexagram import IChingHexagramInterp


class IChingDivinationEngine(DivinationEngineBase):

    def __init__(self):
        self._load_interpretation_data()

    def _load_interpretation_data(self) -> None:
        with importlib.resources.files("ichingpy.data").joinpath("iching_zh.json").open(encoding="utf8") as f:
            self._data = json.load(f)["hexagrams"]

    def execute(self, hexagram: Hexagram) -> None:
        key = str(tuple([v % 2 for v in hexagram.values]))
        interp = IChingHexagramInterp.model_validate(self._data[key])
        for line, line_interp in zip(hexagram.lines, interp.lines):
            line_interp.status = line.status
        hexagram.interpretation = interp


# %%
