from ichingpy.enum.branch import EarthlyBranch
from ichingpy.enum.language import Language
from ichingpy.enum.role import HexagramRole
from ichingpy.enum.six_relative import SixRelative
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
        has_relative = hasattr(self, "_relative")
        match self.display_language:
            case Language.ENGLISH:
                stem = f"{self.stem.name.ljust(4)} ({self.stem.value}) " if has_stem else ""
                branch = f"{self.branch.name_en.ljust(4)} " if has_branch else ""
                relative = f"{self.relative.name.ljust(9)}" if has_relative else ""
                role = f"{self.role.name.ljust(7)}" if self.role is not None else ""
            case Language.CHINESE:
                stem = f"{self.stem.label} " if has_stem else ""
                branch = f"{self.branch.label_with_phase} " if has_branch else ""
                relative = f"{self.relative.label} " if has_relative else ""
                role = f"{self.role.label} " if self.role is not None else ""

        representation = f"{relative}{stem}{branch}{representation}{role}"
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

    @property
    def relative(self) -> SixRelative:
        """The relative associated with the line, w.r.t. to the Palace"""
        return self._relative

    @relative.setter
    def relative(self, value: SixRelative) -> None:
        """Set the relative.
        装六亲"""
        self._relative = value

    @property
    def role(self) -> HexagramRole | None:
        """The role (世应) of the line in the hexagram."""
        return self._role if hasattr(self, "_role") else None

    @role.setter
    def role(self, value: HexagramRole) -> None:
        """Set the role (世应) of the line in the hexagram."""
        self._role = value
