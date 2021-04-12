"""
Problem:

Write a function that takes in an array of integers and returns a sorted version of that array. Use the Insertion Sort
algorithm to sort the array.

Input:
    array: [8, 5, 2, 9, 5, 6, 3]

Output:
    [2, 3, 5, 5, 6, 8, 9]
"""


def insertion_sort_two_for_loops(array):
    """ Uses two for loops to sort

    This solution exemplifies more easily the time complexity of O(n^2) since the two for loops are clearly stated.
    The other 2 solutions use the same logic and strategy, but since the outer for loop is not explicit and a while loop
    is used instead, it is more difficult to see why it is O(n^2) time.

    For a detail explanation fo the time complexity see: https://www.youtube.com/watch?v=ufIET8dMnus
    For a visual comparison between bubble sort and insertion sort see: https://www.youtube.com/watch?v=TZRWRjq2CAg

    The outer loop traverses the array and the inner loop make sure that each new element, no yet sorted, selected by
    the outer loop is inserted in the appropriate location in the sorted array (the sorted array is always in the left).

    :param array: array of integers to be sorted
    :return: array sorted in ascending order
    """
    for idx_outer in range(1, len(array)):
        for idx_inner in reversed(range(1, idx_outer + 1)):
            if array[idx_inner] < array[idx_inner - 1]:
                swap(idx_inner, array)

    return array


def swap(idx, array):
    """ Helper function for two for loops solution

    :param idx: index of current integer from the array
    :param array: array containing the integers
    :return: array with swapped elements. The value for current index gets the value for the previous index and the
             value for the previous index gets the value for the current index
    """
    array[idx], array[idx - 1] = array[idx - 1], array[idx]


def insertion_sort_while(array):
    """ Uses outer for loop and inner while loop to sort (original)

    The logic for this algorithm is the exact same one as the previous one, it just uses a while loop instead of the
    inner for loop.

    :param array: array of integers to be sorted
    :return: array sorted in ascending order
    """
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            swap_while(j, j - 1, array)
            j -= 1

    return array


def swap_while(i, j, array):
    """ Helper function for while solution (original)

    :param i: index of current element selected to be swapped
    :param j: index of previous element (relative to element of index i) in the array that is going to be swapped
    :param array: array containing the integers
    :return: array with swapped elements. The value for current index gets the value for the previous index and the
             value for the previous index gets the value for the current index
    """
    array[i], array[j] = array[j], array[i]
