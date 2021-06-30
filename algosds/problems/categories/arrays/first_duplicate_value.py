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

    :param array: array of integers between 1 and the length of the array
    :return: value of the first duplicate element in the array, -1 if no duplicate is found
    """
    for value in array:
        abs_value = abs(value)
        if array[abs_value - 1] < 0:
            return abs_value
        array[abs_value - 1] *= -1
    return -1
