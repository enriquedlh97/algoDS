"""
Problem:

Write a function that takes in an array of integers and returns a sorted version of that array. Use the Bubble Sort
algorithm to sort the array.

Input:
    array: [8, 5, 2, 9, 5, 6, 3]

Output:
    [2, 3, 5, 5, 6, 8, 9]
"""


def bubble_sort_for_loop(array):
    for idx_outer in reversed(range(len(array))):
        for idx_inner in range(0, idx_outer):
            if array[idx_inner] > array[idx_inner + 1]:
                swap_for_loop(idx_inner, array)

    return array


def bubble_sort_while(array):
    performed_swaps = True

    while performed_swaps:

        performed_swaps = False

        for idx in range(1, len(array)):
            if array[idx] < array[idx - 1]:
                swap_while(idx, array)
                performed_swaps = True

    return array


def swap_while(idx, array):
    array[idx], array[idx - 1] = array[idx - 1], array[idx]


def bubble_sort_while_original(array):
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
    array[idx], array[idx + 1] = array[idx + 1], array[idx]

