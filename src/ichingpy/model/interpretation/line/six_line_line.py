from ichingpy.enum.branch import EarthlyBranch
from ichingpy.enum.language import Language
from ichingpy.enum.stem import HeavenlyStem
from ichingpy.model.interpretation.line.base import LineInterpretationBase


class SixLineLineInterp(LineInterpretationBase):

    def __repr__(self) -> str:
        representation = f"-----" if self.is_yang else f"-- --"

        if self.is_transform:
            if self.is_yin:
                representation += f" X -> -----"
            else:
                representation += f" O -> -- --"

        has_stem = hasattr(self, "_stem")
        has_branch = hasattr(self, "_branch")
        match self.display_language:
            case Language.ENGLISH:
                stem = f"{self.stem.name.ljust(4)} ({self.stem.value}) " if has_stem else ""
                branch = f"{self.branch.name_en.ljust(4)} " if has_branch else ""
            case Language.CHINESE:
                stem = f"{self.stem.label} " if has_stem else ""
                branch = f"{self.branch.label_with_phase} " if has_branch else ""

        representation = f"{stem}{branch}{representation}"
        return representation

    @property
    def stem(self) -> HeavenlyStem:
        """The HeavenlyStem associated with the Line."""
        return self._stem

    @stem.setter
    def stem(self, value: HeavenlyStem) -> None:
        """Set the HeavenlyStem associated with the Line."""
        self._stem = value

    @property
    def branch(self) -> EarthlyBranch:
        """The EarthlyBranch associated with the Line."""
        return self._branch

    @branch.setter
    def branch(self, value: EarthlyBranch) -> None:
        """Set the EarthlyBranch associated with the Line."""
        self._branch = value
