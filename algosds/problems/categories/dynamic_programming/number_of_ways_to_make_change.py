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
    """ My solution with matrix to keep track of sub-problems (brute force in space)

    To understand the general approach watch:
    https://www.youtube.com/watch?v=xCbYmUPvc2Q

    This approach is then adjusted for the current problem, the explanation is here:
    https://www.youtube.com/watch?v=DJ4a7cmjZY0

    The time complexity is O(n * d), where n is the target sum and d the number of coin denominations, because n * d
    sub-problems are solved. The space complexity is the same because a matrix os size n * d is used to keep track of
    the answer for each sub-problem.

    :param n: integer representing the target sum
    :param denoms: array of non-negative integers corresponding to the available coin denominations
    :return: integer representing the maximum number of ways in which the change summing up to n can be given
    """
    # This takes O(n * d) time
    results = initialize_results(n, denoms)

    # This takes O(n * d) time
    answer = get_number_of_ways(n, denoms, results)

    return answer


# Time: O(n * d) time, where n is the target sum and d the number of coin denominations
# Space: O(n * d) space
def get_number_of_ways(n, denoms, results):
    """ Helper function, handles logic for def number_of_ways_to_make_change_matrix(n, denoms)

    This function performs the actual logic

    :param n: integer representing the target sum
    :param denoms: array of non-negative integers corresponding to the available coin denominations
    :param results: two-dimensional array representing matrix keeping track of the sub-problems solutions
    :return: integer representing the maximum number of ways in which the change summing up to n can be given
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


# Time: O(n * d) time, where n is the target sum and d the number of coin denominations
# Space: O(n * d) space
def initialize_results(n, denoms):
    """ Helper function to initialize matrix of sub-problem results

    This helper function initializes the matrix.

    :param n: integer representing the target sum
    :param denoms: array of non-negative integers corresponding to the available coin denominations
    :return: two-dimensional array representing initialized with zeroes and a 1 in position [0][0]
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
    """ My solution using array to keep track of sub-problems

    This solution follows the same logic as the one above, the difference is that a not all answers for every
    sub-problem are saved, instead only the answer for n + 1 sub-problems are saved. That is why here the space
    complexity is O(n), the time complexity stays the same because the number of sub-problems solved does not change.

    For more details on the solution see the videos from first solution and AE video explanation.

    :param n: integer representing the target sum
    :param denoms: array of non-negative integers corresponding to the available coin denominations
    :return: integer representing the maximum number of ways in which the change summing up to n can be given
    """
    # Initialize results array
    results = [1 if idx == 0 else 0 for idx in range(0, n + 1)]

    # Get number of ways
    answer = get_ways(n, denoms, results)

    return answer


# Time: O(n * d) time, where n is the target sum and d the number of coin denominations
# Space: O(n) space
def get_ways(n, denoms, results):
    """ Helper function, handles logic for number_of_ways_to_make_change_linear_space(n, denoms)

    This function contains the actual logic explained in the videos form the other fucntions.

    :param n: integer representing the target sum
    :param denoms: array of non-negative integers corresponding to the available coin denominations
    :param results: array of integers containing the most current solution to the sub-problems
    :return: :return: integer representing the maximum number of ways in which the change summing up to n can be given
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
    """ Original solution

    This solution is the exact same one as the number_of_ways_to_make_change_linear_space(n, denoms) solution, the
    impl is just a little different.

    :param n: integer representing the target sum
    :param denoms: array of non-negative integers corresponding to the available coin denominations
    :return: integer representing the maximum number of ways in which the change summing up to n can be given
    """
    ways = [0 for _ in range(n + 1)]
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]

    return ways[n]
