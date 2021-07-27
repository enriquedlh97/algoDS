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

    This solution works by creating an array of the maximum sum of non-adjacent elements up to a given index. For
    example, for the input array [75, 105, 120, 75, 90, 135], a helper array [0, 0, 0, 0, 0, 0] is creating. Then, at
    every position of the helper array the maximum non-adjacent sum up to that element is computed. At the end, the
    final sum is computed.

    The logic for computing the maximum sum is that it is defined by either the index i - 1, ie the previous sum, or by
    the index (i - 2) + i, meaning that the previous element is omitted, and the current one is added. There
    are two bases cases. When the index i is 0, then the maximum sum is the current element. When the index i is 1, then
    the maximum sum is max(i, i - 1). From index 2 and onwards, the previously stated formula is used. That is
    max(i - 1, (i - 2) + i).

    This means that the array is travered only once.

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

    This solution works exactly the same as the previous one. The only difference is that to avoid extra space, and
    since only the elements i - 1 and i - 2 are needed for computing the maximum sum, these two elements are saved and
    updated at every iteration. Consequently, this results in constant space O(1).

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

    This solution works the same as my brute force solution.

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

    This solution works the same as my optimal solution. 

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
