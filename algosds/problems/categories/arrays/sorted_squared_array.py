"""
Problem:

Write a function that takes a non-empty array of integers that are sorted in ascending
order and returns a new array of the same length with the squares of the original
integers also sorted in ascending order.

Input:
    array: [1, 2, 3, 5, 6, 8, 9]

Output:
    [1, 4, 9, 25, 36, 64, 81]
"""
from collections import deque


# Time O(nlg(n))
# Space O(1)
def sorted_squared_array_sort1(array):
    """ Computes square inplace and sorts

        Loops over the array computing the square values inplace to save memory.
        Sorts the array before returning.

        Attributes:
            array: Non-empty array
    """
    for idx in range(0, len(array)):
        array[idx] = array[idx] ** 2
    return sorted(array)


# Time O(nlg(n))
# Space O(n)
def sorted_squared_array_sort_lambda(array):
    """ Computes square inplace and sorts. Uses lambda and map for this

        Loops over the array computing the square and saving it to a new list.
        Sorts the array before returning.

        Attributes:
            array: Non-empty array
    """
    return sorted(list(map(lambda num: num ** 2, array)))


# Time O(n)
# Space O(n)
def sorted_squared_array_pointers_pop(array):
    """ Computes square and places it in proper index using pointer technique and deque

        Uses the pointer technique of starting one pointer at the end and the other one
        at the beginning of the array. Starts traversing with both towards the center.
        While traversing, computes squares and compares them, prepending the lowes value first
        and then comparing the left value with the next value from the opposite pointer.

        Instead of specifically using pointers, it uses pop() to get first and last values
        iteratively.


        Attributes:
            array: Non-empty array
    """
    if len(array) == 1:
        return [array[0] ** 2]

    # Use Double Ended Queue which is a generalized queue
    # that can get/insert first or last elements
    array_squared = deque()

    for _ in range(0, len(array)):

        if array[0] ** 2 > array[-1] ** 2:
            array_squared.appendleft(array.pop(0) ** 2)
        else:
            array_squared.appendleft(array.pop() ** 2)

    return list(array_squared)


# Time O(nlg(n))
# Space O(n)
def sorted_squared_array_sort2(array):
    """ Computes square inplace and sorts. (original)

        Loops over the array computing the square and saving it to a new array.
        Sorts the array before returning.

        Attributes:
            array: Non-empty array
    """
    array_squared = [0]*len(array)  # initializes array to preallocate memory

    for idx in range(0, len(array)):
        array_squared[idx] = array[idx]**2

    return sorted(array_squared)


# Time O(n)
# Space O(n)
def sorted_squared_array_pointers(array):
    """ Computes square and places it in proper index using pointer technique and deque (original)

            Uses the pointer technique of starting one pointer at the end and the other one
            at the beginning of the array. Starts traversing with both towards the center.
            While traversing, computes squares and compares them, prepending the lowes value first
            and then comparing the left value with the next value from the opposite pointer.

            Attributes:
                array: Non-empty array
        """
    array_squared = [0]*len(array)  # initializes array to preallocate memory
    start = 0
    end = len(array) - 1

    for idx in reversed(range(len(array))):
        start_value = array[start]
        end_value = array[end]

        if abs(start_value) > abs(end_value):
            array_squared[idx] = start_value**2
            start += 1
        else:
            array_squared[idx] = end_value**2
            end -= 1

    return array_squared
