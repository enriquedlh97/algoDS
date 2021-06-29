"""
Problem:

Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.

An array is said to be monotonic if its elements, from left to right, are entirely non-decreasing or entirely
non-increasing.

Non-increasing elements are not necessarily exclusively decreasing; they simply do not increase. Similarly,
non-decreasing elements are not necessarily exclusively increasing; they simply do not decrease.

Empty arrays and arrays of one element are monotonic.

Input:

    array: [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

Output:

    True

"""


# Time O(n), where n is the length of the input array
# Space O(1)
def is_monotonic(array):
    """ My solution

    This solution works by first assuming that the input array is both non-decreasing and non-increasing. Then, it
    iterates over the array, if it finds a condition that violates the non-increasing or non-decreasing assumptions it
    updates a variable representing this assumption.

    When it is found that it is not monotonic, the iteration stops and False is returned. Otherwise, at the end of the
    iteration True is returned. 

    :param array: Array of integers
    :return: Boolean value
    """
    monotonically_increasing = True
    monotonically_decreasing = True

    if len(array) <= 1:
        return True

    for idx in range(1, len(array)):
        if array[idx] > array[idx - 1]:
            monotonically_decreasing = False

        elif array[idx] < array[idx - 1]:
            monotonically_increasing = False

        if not (monotonically_decreasing or monotonically_increasing):
            return False

    return True


# Time O(n), where n is the length of the input array
# Space O(1)
def is_monotonic_original(array):
    """ Original solution

    This solution works exactly the same as the previous solution. It is just implemented a little different.

    :param array: Array of integers
    :return: Boolean value
    """
    is_non_decreasing = True
    is_non_increasing = True
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            is_non_decreasing = False
        if array[i] > array[i - 1]:
            is_non_increasing = False

    return is_non_decreasing or is_non_increasing
