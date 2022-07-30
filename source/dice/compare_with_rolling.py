import numpy
import pandas

from compute_probability import get_probability_for_kth_highest_roll_using_n_dice
from throw_dice import ThrowDice


def compare_with_rolling_dice(number_of_dice: int, die_type: int, target, direct_result: float):
    experiments = 1000000
    error = 1 / numpy.sqrt(experiments)
    list_dices = []
    for i in range(number_of_dice):
        list_dices.append(die_type)
    throw_object = ThrowDice(list_dices)
    count = 0
    for experiment in range(experiments):
        result = throw_object.throw()
        if result[kth - 1] == target:
            count += 1.
    rolling_result = count / experiments
    agreement = numpy.abs(1. - (rolling_result) / direct_result)
    if agreement > 3 * error:
        error_string = f"Bad agreement within {error} with rolling_result: {rolling_result}"
        print(error_string)

    return rolling_result


data_frame = pandas.DataFrame({'number_of_dice': [],
                               'die_type': [],
                               'kth': [],
                               'target_value': [],
                               'probability': []}, dtype=int)

for kth in [1, 2, 3]:
    for die_type in [10, 12, 20]:
        for number_of_dice in range(3, 6):
            for target in range(1, die_type + 1):
                direct_result = get_probability_for_kth_highest_roll_using_n_dice(die_type, number_of_dice, target, kth)
                # test_with_rolling_dice(number_of_dice, die_type, target, direct_result)
                result_string = f"{number_of_dice}D{die_type} with {kth}th counting for target-value {target}: direct_result = {direct_result}"
                data_frame = data_frame.append(
                    {'number_of_dice': number_of_dice, 'die_type': die_type, "kth": kth, 'target_value': target,
                     "probability": direct_result}, ignore_index=True)

data_frame['number_of_dice'] = data_frame['number_of_dice'].astype(int)
data_frame['die_type'] = data_frame['die_type'].astype(int)
data_frame['kth'] = data_frame['kth'].astype(int)
data_frame['target_value'] = data_frame['target_value'].astype(int)
print(data_frame)
data_frame.to_csv('result_July30th_22.csv', index=False )
