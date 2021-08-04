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
    """ My brute force solution

    To understand the general approach watch:
    https://www.youtube.com/watch?v=xCbYmUPvc2Q
    and
    https://www.youtube.com/watch?v=DJ4a7cmjZY0

    This approach is then adjusted for the current problem, very similar to this:
    https://www.youtube.com/watch?v=jgiZlGzXMBw

    The time complexity is O(n * d), where n is the target sum and d the number of coin denominations, because n * d
    sub-problems are solved. The space complexity is the same because a matrix os size n * d is used to keep track of
    the answer for each sub-problem.

    :param n: non-negative integer representing the target amount of money
    :param denoms: array of positive integers representing coin denominations
    :return: integer representing the smallest number of coins needed to make change for (sum up to) the target amount
    """
    # Initialize results matrix
    results = initialize_results(n, denoms)

    # Get minimum number of coins
    answer = get_min_number(n, denoms, results)

    return answer if answer != float('inf') else -1


def get_min_number(n, denoms, results):
    """ Helper function that handles logic for min_number_of_coins_for_change() function

    This function performs the actual logic.

    :param n: non-negative integer representing the target amount of money
    :param denoms: array of positive integers representing coin denominations
    :param results: two-dimensional array corresponding to a matrix to save sub-problem results initialized with inf except for
                    the (0, 0) element containing 0
    :return: integer representing the smallest number of coins needed to make change for (sum up to) the target amount
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
    """ Helper function tu initialize results matrix

    This helper function initializes the matrix.

    :param n: non-negative integer representing the target amount of money
    :param denoms: array of positive integers representing coin denominations
    :return: two-dimensional array corresponding to a matrix to save sub-problem results initialized with inf except for
             the (0, 0) element containing 0
    """
    results = [[0 if idx == 0 else float('inf') for idx in range(n + 1)]]

    for row in range(len(denoms)):
        results.append([0 for _ in range(n + 1)])

    return results


# Time: O(n * d) time, where n is the target sum and d the number of coin denominations
# Space: O(n) space
def min_number_of_coins_for_change_linear_space(n, denoms):
    """ My optimal linear solution

    This solution follows the same logic as the one above, the difference is that not all answers for every
    sub-problem are saved, instead only the answer for n + 1 sub-problems are saved. That is why here the space
    complexity is O(n), the time complexity stays the same because the number of sub-problems solved does not change.

    For more details on the solution see the videos from first solution and AE video explanation.

    :param n: non-negative integer representing the target amount of money
    :param denoms: array of positive integers representing coin denominations
    :return: integer representing the smallest number of coins needed to make change for (sum up to) the target amount
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
    """ Original optimal linear solution

    This solution is the exact same one as the previous) solution, the implementation is just a little different.

    :param n: non-negative integer representing the target amount of money
    :param denoms: array of positive integers representing coin denominations
    :return: integer representing the smallest number of coins needed to make change for (sum up to) the target amount
    """
    num_of_coins = [float('inf') for _ in range(n + 1)]
    num_of_coins[0] = 0

    for denom in denoms:
        for amount in range(len(num_of_coins)):
            if denom <= amount:
                num_of_coins[amount] = min(num_of_coins[amount], num_of_coins[amount - denom] + 1)

    return num_of_coins[n] if num_of_coins[n] != float('inf') else -1
