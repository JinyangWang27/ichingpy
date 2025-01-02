import random
from enum import Enum

from yi.model.stem_branch import EarthlyBranch, HeavenlyStem


class Yao(int, Enum):
    Yang = 1
    Yin = 0

    def __repr__(self) -> str:
        return f"▅▅▅▅▅▅" if self.value else f"▅▅  ▅▅"

    def transform(self) -> "Yao":
        return Yao(not self.value)

    @classmethod
    def random(cls) -> "Yao":
        return Yao(random.getrandbits(1))

    @property
    def is_transform(self) -> bool:
        """bool: Whether the Yao needs to be transformed (变爻)"""
        return self._is_transform

    @is_transform.setter
    def is_transform(self, value: bool) -> None:
        self._is_transform = value

    @property
    def stem(self) -> HeavenlyStem:
        return self._stem

    @stem.setter
    def stem(self, value: HeavenlyStem) -> None:
        self._stem = value

    @property
    def branch(self) -> EarthlyBranch:
        return self._branch

    @branch.setter
    def branch(self, value: EarthlyBranch) -> None:
        self._branch = value
