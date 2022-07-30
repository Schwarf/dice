from scipy import special


# q_{m,k}(y,z)=y^{m-k}(z-y)^k.
def helper_function(m: int, k: int, y: int, z: int) -> int:
    return y ** (m - k) * (z - y) ** k


def get_probability_for_kth_highest_roll_using_n_dice(die_type: int, number_of_dice: int, target_value: int,
                                                      kth_die: int) -> float:
    denominator: float = die_type ** number_of_dice
    numerator: float = 0.
    for i in range(kth_die, number_of_dice + 1):
        numerator += special.binom(number_of_dice, i) * (
                    helper_function(number_of_dice, i , target_value - 1, die_type) -
                    helper_function(number_of_dice, i , target_value, die_type))

    return numerator / denominator
