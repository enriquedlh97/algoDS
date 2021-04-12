"""
Problem:

Write a function that takes in an array of integers and returns a sorted version of that array. Use the Selection Sort
algorithm to sort the array.

Input:
    array: [8, 5, 2, 9, 5, 6, 3]

Output:
    [2, 3, 5, 5, 6, 8, 9]
"""


def selection_sort_two_for_loops(array):
    for outer_idx in range(len(array)):

        smallest_value_idx = outer_idx

        for inner_idx in range(outer_idx, len(array)):
            if array[inner_idx] < array[smallest_value_idx]:
                smallest_value_idx = inner_idx

        swap(outer_idx, smallest_value_idx, array)

    return array


def selection_sort_while(array):
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
    array[old_idx], array[new_idx] = array[new_idx], array[old_idx]
