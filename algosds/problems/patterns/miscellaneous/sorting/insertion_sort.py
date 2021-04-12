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
    for idx_outer in range(1, len(array)):
        for idx_inner in reversed(range(1, idx_outer + 1)):
            if array[idx_inner] < array[idx_inner - 1]:
                swap(idx_inner, array)

    return array


def swap(idx, array):
    array[idx], array[idx - 1] = array[idx - 1], array[idx]


def insertion_sort_while(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            swap_while(j, j - 1, array)
            j -= 1

    return array


def swap_while(i, j, array):
    array[i], array[j] = array[j], array[i]
