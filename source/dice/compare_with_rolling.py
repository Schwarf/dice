import numpy
import pandas
from matplotlib import pyplot as plt

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


str_number_of_dice = 'number_of_dice'
str_die_type = 'die_type'
str_kth = 'kth'
str_target_value = 'target_value'
str_probability = 'probability'

data_frame = pandas.DataFrame({str_number_of_dice: [],
                               str_die_type: [],
                               str_kth: [],
                               str_target_value: [],
                               str_probability: []}, dtype=int)

for kth in [1, 2, 3, 4]:
    for die_type in [10, 12, 20]:
        for number_of_dice in range(1, 6):
            if kth > number_of_dice:
                continue
            for target in range(1, die_type + 1):
                direct_result = get_probability_for_kth_highest_roll_using_n_dice(die_type, number_of_dice, target, kth)
                # test_with_rolling_dice(number_of_dice, die_type, target, direct_result)
                result_string = f"{number_of_dice}D{die_type} with {kth}th counting for target-value {target}: direct_result = {direct_result}"
                data_frame = data_frame.append(
                    {str_number_of_dice: number_of_dice, str_die_type: die_type, str_kth: kth, str_target_value: target,
                     str_probability: direct_result}, ignore_index=True)

data_frame[str_number_of_dice] = data_frame[str_number_of_dice].astype(int)
data_frame[str_die_type] = data_frame[str_die_type].astype(int)
data_frame[str_kth] = data_frame[str_kth].astype(int)
data_frame[str_target_value] = data_frame[str_target_value].astype(int)

sanity_check = data_frame.groupby([str_number_of_dice, str_die_type, str_kth])[str_probability].sum()
assert(numpy.all(sanity_check.values == 1.0))
data_frame.to_csv('result_July30th_22.csv', index=False)


z1 = data_frame[
    (data_frame[str_die_type] == 20) & (data_frame[str_kth] == 3) & (data_frame[str_number_of_dice] == 3)].plot(
    x=str_target_value, y=str_probability).plot()
z2 = data_frame[
    (data_frame[str_die_type] == 20) & (data_frame[str_kth] == 2) & (data_frame[str_number_of_dice] == 3)].plot(
    x=str_target_value, y=str_probability).plot()
z3 = data_frame[
    (data_frame[str_die_type] == 20) & (data_frame[str_kth] == 1) & (data_frame[str_number_of_dice] == 3)].plot(
    x=str_target_value, y=str_probability).plot()
plt.show()
