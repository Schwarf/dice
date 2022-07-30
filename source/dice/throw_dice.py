from typing import Dict, List

from die import Die
from i_die import IDie
from i_throw_dice import IThrowDice


class ThrowDice(IThrowDice):
    def __init__(self, dice_types: List[int]) -> None:
        self._dices: List[IDie] = []
        self._list_of_dice: Dict[str, int] = {}
        for die_type in dice_types:
            die = Die(die_type)
            self._dices.append(die);
            if not die.type in self._list_of_dice.keys():
                self._list_of_dice[die.type] = 0
            self._list_of_dice[die.type] += 1

    @property
    def list_of_dice(self) -> Dict[str, int]:
        return self._list_of_dice

    def throw(self) -> List[int]:
        result: List[int] = []
        for die in self._dices:
            result.append(die.roll())
        return sorted(result)[::-1]
