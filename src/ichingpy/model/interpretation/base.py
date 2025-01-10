from abc import ABC, abstractmethod

from pydantic import BaseModel


class InterpretationBase(BaseModel, ABC):
    @abstractmethod
    def __repr__(self) -> str:
        pass
