from typing import Any

from pydantic import model_validator

from ichingpy.enum.line_status import LineStatus
from ichingpy.model.interpretation.line.base import LineInterpretationBase


class IChingLineInterp(LineInterpretationBase):
    name: str
    text: str
    image: str | None

    @model_validator(mode="before")
    @classmethod
    def create_line_status(cls, value: dict[str, Any]) -> dict[str, Any]:
        name = value["name"]
        assert name is not None
        if "九" in name or "Nine" in name:
            value["status"] = LineStatus.STATIC_YANG
        elif "六" in name or "Six" in name:
            value["status"] = LineStatus.STATIC_YIN
        return value

    def __repr__(self) -> str:
        representation = f"-----" if self.is_yang else f"-- --"
        if self.is_transform:
            if self.is_yin:
                representation += f" X -> -----"
            else:
                representation += f" O -> -- --"

        return representation
