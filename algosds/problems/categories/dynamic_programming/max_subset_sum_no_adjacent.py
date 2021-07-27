"""
Problem:

    Write a function that takes in an array of positive integers and returns the maximum sum of non-adjacent elements in
    the array.

    If the input array is empty, the function should return 0.

Input:

    array: [75, 105, 120, 75, 90, 135]

Output:

    330

    gotten as 75 + 120 + 135

"""


# Time: O(n) time, where n is the length of input array
# Space: O(n) space
def max_subset_sum_no_adjacent_brute_force(array):
    """ My brute force solution

    :param array: array of integers
    :return: integer representing the maximum sum of non-adjacent elements
    """
    # Handle base case when array empty
    if not array:
        return 0

    array_sum = [0 for _ in array]

    for idx in range(len(array)):

        # Handle base cases
        if idx == 0:
            array_sum[idx] = array[idx]
        elif idx == 1:
            array_sum[idx] = max(array[idx], array[idx - 1])

        else:
            array_sum[idx] = max(array_sum[idx - 1], array_sum[idx - 2] + array[idx])

    return array_sum[-1]


# Time: O(n) time, where n is the length of input array
# Space: O(1) space
def max_subset_sum_no_adjacent_optimal(array):
    """ My optimal solution

    :param array: array of integers
    :return: integer representing the maximum sum of non-adjacent elements
    """
    # Handle base case when array empty
    if not array:
        return 0

    previous_one = 0
    previous_two = 0
    current = 0

    for idx in range(len(array)):

        # Handle base cases
        if idx == 0:
            current = array[idx]
            previous_one = 0
        else:
            current = max(previous_one, previous_two + array[idx])

        previous_two = previous_one
        previous_one = current

    return current


# Time: O(n) time, where n is the length of input array
# Space: O(n) space
def max_subset_sum_no_adjacent_brute_force_original(array):
    """ Original brute force solution

    :param array: array of integers
    :return: integer representing the maximum sum of non-adjacent elements
    """
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]
    max_sums = array[:]
    max_sums[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        max_sums[i] = max(max_sums[i - 1], max_sums[i - 2] + array[i])
    return max_sums[-1]


# Time: O(n) time, where n is the length of input array
# Space: O(1) space
def max_subset_sum_no_adjacent_optimal_original(array):
    """ Original optimal solution

    :param array: array of integers
    :return: integer representing the maximum sum of non-adjacent elements
    """
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]
    second = array[0]
    first = max(array[0], array[1])
    for i in range(2, len(array)):
        current = max(first, second + array[i])
        second = first
        first = current
    return first
