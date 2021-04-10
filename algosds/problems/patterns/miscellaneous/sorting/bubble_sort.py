"""
Problem:

Write a function that takes in an array of integers and returns a sorted version of that array. Use the Bubble Sort
algorithm to sort the array.

Input:
    array: [8, 5, 2, 9, 5, 6, 3]

Output:
    [2, 3, 5, 5, 6, 8, 9]
"""


# Time O(n^2), where n is the length of the array
# Space O(1)
def bubble_sort_for_loop(array):
    """ Uses two for loops

    This solution exemplifies more easily the time complexity of O(n^2) since the two for loops are clearly stated.
    The other 2 solutions use the same logic and strategy, but since the outer for loop is no explicit and a while loop
    is used instead, it is more difficult to see why it is O(n^2) time.

    For a detail explanation fo the time complexity see: https://www.youtube.com/watch?v=euPlXW7dnlI

    The outer loop traverses the array backwards and the inner loop make sure that the biggest, not yet sorted, element
    is at the index of the outer loop.

    :param array: array of integers to be sorted
    :return: array sorted in ascending order
    """
    for idx_outer in reversed(range(len(array))):
        for idx_inner in range(0, idx_outer):
            if array[idx_inner] > array[idx_inner + 1]:
                swap(idx_inner, array)

    return array


# Time O(n^2), where n is the length of the array
# Space O(1)
def bubble_sort_while(array):
    """ Uses a while loop and a for loop

    The logic for this algorithm is the exact same one as the previous one, it just uses a while loop instead of the
    outer for loop.

    :param array: array of integers to be sorted
    :return: array sorted in ascending order
    """
    performed_swaps = True

    while performed_swaps:

        performed_swaps = False

        for idx in range(1, len(array)):
            if array[idx] < array[idx - 1]:
                swap_while(idx, array)
                performed_swaps = True

    return array


def swap_while(idx, array):
    """ Helper swap function for while loop solution (solution above)

    :param idx: index of current integer from the array
    :param array: array containing the integers
    :return: array with swapped elements. The value for current index gets the value for the previous index and the
             value for the previous index gets the value for the current index
    """
    array[idx], array[idx - 1] = array[idx - 1], array[idx]


# Time O(n^2), where n is the length of the array
# Space O(1)
def bubble_sort_while_original(array):
    """ Uses a while loop and a for loop (original)

    The logic for this algorithm is the exact same one as the previous one, it just uses a while loop instead of the
    outer for loop.

    Also, this algorithm uses an additional counter variable to make it more efficient, this counter variable is similar
    ti the effect the outer for loop has in the firs solution, where it makes the inner loop go al the way up to the las
    index of the array and on every iteration go one index lower. This avoids analysing already sorted values.
    Nevertheless, the time complexity does not change.

    :param array: array of integers to be sorted
    :return: array sorted in ascending order
    """
    is_sorted = False
    counter = 0

    while not is_sorted:
        is_sorted = True

        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                swap(i, array)
                is_sorted = False

        counter += 1

    return array


def swap(idx, array):
    """ Helper swap function for for loop and while original solutions

    :param idx: index of current integer from the array
    :param array: array containing the integers
    :return: array with swapped elements. The value for current index gets the value for the previous index and the
             value for the previous index gets the value for the current index
    """
    array[idx], array[idx + 1] = array[idx + 1], array[idx]
