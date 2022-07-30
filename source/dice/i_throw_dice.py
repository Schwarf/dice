from typing import Dict, List
from abc import abstractmethod, ABC


class IThrowDice(ABC):
    @property
    @abstractmethod
    def list_of_dice(self)-> Dict[str, int]:
        pass

    @abstractmethod
    def throw(self)-> List[int]:
        pass
