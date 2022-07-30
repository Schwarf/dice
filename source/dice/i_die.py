from abc import ABC, abstractmethod


class IDie(ABC):
    @property
    @abstractmethod
    def type(self) -> str:
        pass

    @abstractmethod
    def roll(self) -> int:
        pass
