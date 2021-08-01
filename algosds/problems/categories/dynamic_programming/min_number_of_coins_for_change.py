"""
Problem:

    Given an array of positive integers representing coin denominations and a single non-negative integer n representing
    a target amount of money, write a function that returns the smallest number of coins needed to make change for
    (sum up to) that target amount using the given coin denominations.

    Note that you have access to an unlimited amount of coins. In other words, if the denominations are [1, 5, 10], you
    have access to an unlimited amount of 1s, 5s and 10s.

    If it is impossible to make change for the target amount, return -1.

Input:

    n = 7
    denoms = [1, 5, 10]

Output:

    3 computed as 2x1 + 1x5

"""


# Time: O(n * d) time, where n is the target sum and d the number of coin denominations
# Space: O(n * d) space
def min_number_of_coins_for_change(n, denoms):
    """

    :param n:
    :param denoms:
    :return:
    """
    # Initialize results matrix
    results = initialize_results(n, denoms)

    # Get minimum number of coins
    answer = get_min_number(n, denoms, results)

    return answer if answer != float('inf') else -1


def get_min_number(n, denoms, results):
    """

    :param n:
    :param denoms:
    :param results:
    :return:
    """
    for idx_coin in range(len(denoms)):
        for target in range(1, n + 1):
            if target - denoms[idx_coin] >= 0:
                results[idx_coin + 1][target] = min(1 + results[idx_coin + 1][target - denoms[idx_coin]],
                                                    results[idx_coin][target])
            else:
                results[idx_coin + 1][target] = results[idx_coin][target]

    return results[-1][-1]


def initialize_results(n, denoms):
    """

    :param n:
    :param denoms:
    :return:
    """
    results = [[0 if idx == 0 else float('inf') for idx in range(n + 1)]]

    for row in range(len(denoms)):
        results.append([0 for _ in range(n + 1)])

    return results


# Time: O(n * d) time, where n is the target sum and d the number of coin denominations
# Space: O(n) space
def min_number_of_coins_for_change_linear_space(n, denoms):
    """

    :param n:
    :param denoms:
    :return:
    """
    # Initialize array
    results = [0 if idx == 0 else float('inf') for idx in range(n + 1)]

    # Get min number of coins
    for idx_coin in range(len(denoms)):
        for target in range(1, n + 1):
            if target - denoms[idx_coin] >= 0:
                results[target] = min(1 + results[target - denoms[idx_coin]], results[target])

    return results[-1] if results[-1] != float('inf') else -1


# Time: O(n * d) time, where n is the target sum and d the number of coin denominations
# Space: O(n) space
def min_number_of_coins_for_change_original(n, denoms):
    """
    
    :param n:
    :param denoms:
    :return:
    """
    num_of_coins = [float('inf') for _ in range(n + 1)]
    num_of_coins[0] = 0

    for denom in denoms:
        for amount in range(len(num_of_coins)):
            if denom <= amount:
                num_of_coins[amount] = min(num_of_coins[amount], num_of_coins[amount - denom] + 1)

    return num_of_coins[n] if num_of_coins[n] != float('inf') else -1
