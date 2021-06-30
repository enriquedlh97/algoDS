"""
Problem:

Given an array of integers between 1 and n, inclusive, where n is the length of the array, write a function that returns
the first integer that appears more than once (when the array is read from left to right).

In other words, out of all the integers that might occur more than once in the input array, your function should return
the one whose first duplicate value has the minimum index.

if no integer appears more than once, your function should return -1 .

Note that you're allowed to mutate the input array.

Input:

    array: [2, 1, 5, 2, 3, 3, 4]

Output:

    2

Input:

    array: [2, 1, 5, 3, 3, 2, 4]

Output:

    3

"""


# Time O(n^2), where n is the length of the input array
# Space O(1)
def first_duplicate_value_original_brute_force(array):
    """ Original brute force solution

    This solutions works by using and outer and inner for loop. The inner for loop looks for a duplicate of the value
    from the outer loop. Once a duplicate value is found its index is saved. Everytime a new duplicate value is found,
    the smallest index from the current one and the new duplicate value found.

    Since the variable holding the minimum duplicate index is initialized to the length of the input array, at the end,
    if it still has the same value then -1 is returned; otherwise, the actual value is returned.

    :param array: array of integers between 1 and the length of the array
    :return: value of the first duplicate element in the array, -1 if no duplicate is found
    """
    minimum_second_index = len(array)
    for i in range(len(array)):
        value = array[i]
        for j in range(i + 1, len(array)):
            value_to_compare = array[j]
            if value == value_to_compare:
                minimum_second_index = min(minimum_second_index, j)

    if minimum_second_index == len(array):
        return -1

    return array[minimum_second_index]


# Time O(n), where n is the length of the input array
# Space O(n)
def first_duplicate_value_original_set(array):
    """ Original solution with set, uses keys

    This solution loops once over the input array. At each step, it checks if the current value already exists in the
    set of seen values, if it does exists, then the value is returned, otherwise it continues.

    If no duplicate value is found, then -1 s returned at the end of the for loop.

    :param array: array of integers between 1 and the length of the array
    :return: value of the first duplicate element in the array, -1 if no duplicate is found
    """
    seen = set()
    for value in array:
        if value in seen:
            return value
        seen.add(value)
    return -1


# Time O(n), where n is the length of the input array
# Space O(n)
def first_duplicate_value_set(array):
    """ My solution with set, uses length

    This solutions works almost the same as the previous one. The only difference is that instead of checking if a value
    exists in the set of seen values it just adds the value to the set and compares the new length of the set to the
    length of it before the value was added. I the length does not change it means the value was already seen and it is
    returned.

    :param array: array of integers between 1 and the length of the array
    :return: value of the first duplicate element in the array, -1 if no duplicate is found
    """
    seen_elements = set()

    for element in array:
        previous_length = len(seen_elements)
        seen_elements.add(element)
        current_length = len(seen_elements)

        if current_length == previous_length:
            return element

    return -1


# Time O(n), where n is the length of the input array
# Space O(1)
def first_duplicate_value_original_indices(array):
    """ Original bets solution, uses indices

    This is the most optimal solution. To keep track of seen values, the same input array is used and mutated.
    It takes advantage of the fact that the number go from 1 to the length of the input array.

    It maps each number in the input array to an index. The map is defined by subtracting 1 from the actual value to be
    mapped.

    For example, input_array: [3, 2, 1, 4, 2] has indices 0, 1, 2 and 3.

    to map we do
    map = value - 1

    So we get.

    Index | Value | Map
      0   |   3   | 3 - 1 = 2
      1   |   2   | 2 - 1 = 1
      2   |   1   | 1 - 1 = 0
      3   |   4   | 4 - 1 = 3
      4   |   2   | 2 - 1 = 1

    The actual value at the index of the map does not matter, only its sign. If the value is positive, it means the
    number has not been previously seen; otherwise, when the value is negative, it means it was already seen and the
    current value is a duplicate.

    For example, continuing with the same input_array: [3, 2, 1, 4, 2]

    If we had [3, -2, 1, 4, 2] it means that the value that maps to the index 1 has already been seen.

    So if we evaluate the value at index 4, in this case input_array[4] = 2, we would check to where it maps by
    computing map = value - 1 -> map = 2 - 1 = 1. So we know that the 2 at index 4 maps to the value at index 1.
    To see if the value 2 has already seen before we check th sign of the value at index 1. In this case the value is
    negative and that indicates that the 2 at index 4 is a value that ahs already been seen.

    This is the main logic behind how this solution works.

    The algorithm iterates over the input_array, at each step it updates the sing of the index to which the current
    value maps to, to indicate the value ahs already been seen. At the same time it checks that the current value has
    not been seen. When a value that has already been seen, then it return this value as solution.

    If the for loop ends and no duplicate value is found, then -1 is returned.

    :param array: array of integers between 1 and the length of the array
    :return: value of the first duplicate element in the array, -1 if no duplicate is found
    """
    for value in array:
        abs_value = abs(value)
        if array[abs_value - 1] < 0:
            return abs_value
        array[abs_value - 1] *= -1
    return -1
