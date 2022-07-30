from numpy import random

from i_die import IDie


class Die(IDie):
    def __init__(self, die_type: int) -> None:
        # Add +1 because interval is given in [x, y)
        self._die_type = f"D{die_type}"
        self._max_value = die_type + 1


    @property
    def type(self) -> str:
        return self._die_type

    def roll(self) -> int:
        return random.randint(low=1, high=self._max_value)
