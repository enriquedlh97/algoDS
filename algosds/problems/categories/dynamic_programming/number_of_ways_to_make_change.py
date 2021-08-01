"""
Problem:

    Given an array of distinct  positive integers representing coin denominations and a single non-negative integer n
    representing a target amount of money, write a function that returns the number of ways to make change for that
    target amount using the given coin denominations.

    Note that an unlimited amount of coins is available.

Input:

    n = 5
    denoms = [1, 5]

Output:

    2 computed as 1x1 + 1x5 and 6x1

"""


# Time: O(n * d) time, where n is the target sum and d the number of coin denominations
# Space: O(n * d) space
def number_of_ways_to_make_change_matrix(n, denoms):
    """

    :param n:
    :param denoms:
    :return:
    """
    results = initialize_results(n, denoms)

    answer = get_number_of_ways(n, denoms, results)

    return answer


def get_number_of_ways(n, denoms, results):
    """

    :param n:
    :param denoms:
    :param results:
    :return:
    """
    # Handle base case
    if n == 0:
        return 1

    for idx_coin in range(0, len(denoms)):
        for target in range(0, n + 1):

            if target - denoms[idx_coin] < 0:
                addition = 0
            else:
                addition = results[idx_coin + 1][target - denoms[idx_coin]]

            results[idx_coin + 1][target] = results[idx_coin][target] + addition

    return results[-1][-1]


def initialize_results(n, denoms):
    """

    :param n:
    :param denoms:
    :return:
    """
    first_result = [0 for _ in range(0, n)]
    first_result.insert(0, 1)

    results = [first_result]

    # Initialize results array
    for _ in range(0, len(denoms)):
        results.append([0 for _ in range(0, n + 1)])

    return results


# Time: O(n * d) time, where n is the target sum and d the number of coin denominations
# Space: O(n) space
def number_of_ways_to_make_change_linear_space(n, denoms):
    """

    :param n:
    :param denoms:
    :return:
    """
    # Initialize results array
    results = [1 if idx == 0 else 0 for idx in range(0, n + 1)]

    # Get number of ways
    answer = get_ways(n, denoms, results)

    return answer


def get_ways(n, denoms, results):
    """

    :param n:
    :param denoms:
    :param results:
    :return:
    """
    if n == 0:
        return 1

    for coin in denoms:
        for target in range(len(results)):
            results[target] += results[target - coin] if target - coin >= 0 else False
            # if target - coin >= 0: results[target] += results[target - coin]

    return results[-1]


# Time: O(n * d) time, where n is the target sum and d the number of coin denominations
# Space: O(n) space
def number_of_ways_to_make_change_original(n, denoms):
    """
    
    :param n:
    :param denoms:
    :return:
    """
    ways = [0 for _ in range(n + 1)]
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]

    return ways[n]
