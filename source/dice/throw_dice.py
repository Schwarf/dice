from typing import Dict, List

import numpy

from die import Die
from i_die import IDie
from i_throw_dice import IThrowDice
from compute_probability import get_probability_for_kth_highest_roll_using_n_dice

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

"""
experiments = 1000000
error = 1 / numpy.sqrt(experiments)
for kth in [1, 2, 3]:
    for die_type in [3, 6, 8, 10, 12, 20]:
        list_dices = []
        for target in range(1, die_type + 1):
            for number_of_dice in range(3, 6):
                list_dices.append(die_type)
                throw_object = ThrowDice(list_dices)
                count = 0
                for experiment in range(experiments):
                    result = throw_object.throw()
                    if result[kth - 1] == target:
                        count += 1
                rolling_result = count / experiments
                direct_result = get_probability_for_kth_highest_roll_using_n_dice(die_type, number_of_dice, target, kth)
                result_string = f"{number_of_dice}D{die_type} with {kth}th die counting for target-value {target}: direct_result = {direct_result}"
                print(result_string)
                agreement = numpy.abs(1. - (rolling_result)/direct_result)
                if agreement > 3*error:
                    error_string = f"Bad agreement within {error} with rolling_result: {rolling_result}"
                    print(error_string)
"""
experiments = 1000000
count = 0
target = 1
target_index = 1
t = ThrowDice([3,3,3,3])
for i in range(experiments):
    throw = t.throw()
    # print(throw)
    if throw[target_index] == target:
        count += 1
print(get_probability_for_kth_highest_roll_using_n_dice(3,4,1,2))
result_d6_4 = 0.2407363
result_d20_10 = 0.0746995
resukt_d20_1 = 0.0072028
result_d20_20 = 0.0072114

result = count / experiments
print(result, 1 / numpy.sqrt(1000000))
