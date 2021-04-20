"""
Problem:

Write a function that takes in an array of integers and returns a sorted version of that array. Use the Selection Sort
algorithm to sort the array.

Input:
    array: [8, 5, 2, 9, 5, 6, 3]

Output:
    [2, 3, 5, 5, 6, 8, 9]
"""


# Time O(n^2), where n is the length of the array
# Space O(1)
def selection_sort_two_for_loops(array):
    """ Uses two for loops to sort

    This solution exemplifies more easily the time complexity of O(n^2) since the two for loops are clearly stated.
    The other 2 solutions use the same logic and strategy, but since the outer for loop is not explicit and a while loop
    is used instead, it is more difficult to see why it is O(n^2) time.

    For a detail explanation of the time complexity see: https://www.youtube.com/watch?v=Lrd1QaKyok4
    For a visual comparison between bubble sort, insertion sort and selection sort see:
    https://www.youtube.com/watch?v=peLS-S23TvE

    The outer loop traverses the array and the inner loop make sure that the smallest element in the unsorted apart of
    the array (right side) is selected, then after inner loop is done, th current element of the outer loop is swapped
    with the current smallest element selected in the inner loop. This happens only if the smallest selected element
    from the inner loop is smaller than the current element from the outer loop.

    :param array: array of integers to be sorted
    :return: array sorted in ascending order
    """
    for outer_idx in range(len(array)):

        smallest_value_idx = outer_idx

        for inner_idx in range(outer_idx, len(array)):
            if array[inner_idx] < array[smallest_value_idx]:
                smallest_value_idx = inner_idx

        swap(outer_idx, smallest_value_idx, array)

    return array


# Time O(n^2), where n is the length of the array
# Space O(1)
def selection_sort_while(array):
    """ Uses outer for loop and inner while loop to sort (original)

    The logic for this algorithm is the exact same one as the previous one, it just uses a while loop instead of the
    inner for loop.

    :param array: array of integers to be sorted
    :return: array sorted in ascending order
    """
    current_idx = 0
    while current_idx < len(array) - 1:
        smallest_idx = current_idx
        for i in range(current_idx + 1, len(array)):
            if array[smallest_idx] > array[i]:
                smallest_idx = i
        swap(current_idx, smallest_idx, array)
        current_idx += 1
    return array


def swap(old_idx, new_idx, array):
    """ Helper function for swapping

    :param old_idx: index of current selected element from the outer loop to be replaced by new smallest element
    :param new_idx: index of new smallest element selected in inner for loop
    :param array: array containing the integers
    :return: array with swapped elements. The value for old_index gets replaced by the value for the new_index and the
             value for the new_index gets the value for the old_index
    """
    array[old_idx], array[new_idx] = array[new_idx], array[old_idx]
