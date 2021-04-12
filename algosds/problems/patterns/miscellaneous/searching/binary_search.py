"""
Problem:

Write a function that takes in an array of integers and returns a sorted version of that array. Use the Selection Sort
algorithm to sort the array.

Input:
    array: [8, 5, 2, 9, 5, 6, 3]

Output:
    [2, 3, 5, 5, 6, 8, 9]
"""


def binary_search_while(array, target):
    left_pointer = 0
    right_pointer = len(array) - 1

    while left_pointer <= right_pointer:

        middle_pointer = get_middle(left_pointer, right_pointer)

        if target == array[middle_pointer]:
            return middle_pointer
        elif right_pointer == left_pointer and array[right_pointer] == target:
            return right_pointer
        elif target < array[middle_pointer]:
            right_pointer = middle_pointer - 1
        elif target > array[middle_pointer]:
            left_pointer = middle_pointer + 1

    return - 1


def binary_search_recursive(array, target, left_pointer=0, right_pointer=None):
    if right_pointer is None:
        right_pointer = len(array) - 1

    middle_pointer = get_middle(left_pointer, right_pointer)

    if target == array[middle_pointer]:
        return middle_pointer
    elif left_pointer == right_pointer and array[right_pointer] == target:
        return right_pointer
    elif left_pointer == right_pointer and array[right_pointer] != target:
        return -1
    elif target < array[middle_pointer]:
        right_pointer = middle_pointer - 1
    elif target > array[middle_pointer]:
        left_pointer = middle_pointer + 1

    return binary_search_recursive(array, target, left_pointer, right_pointer)


def get_middle(left_pointer, right_pointer):
    return (left_pointer + right_pointer) // 2


def binary_search_recursive_original(array, target):
    return binary_search_recursive_helper(array, target, 0, len(array) - 1)


def binary_search_recursive_helper(array, target, left, right):
    if left > right:
        return - 1
    middle = (left + right) // 2
    potential_match = array[middle]
    if target == potential_match:
        return middle
    elif target < potential_match:
        return binary_search_recursive_helper(array, target, left, middle - 1)
    else:
        return binary_search_recursive_helper(array, target, middle + 1, right)


def binary_search_while_original(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        potential_match = array[middle]
        if target == potential_match:
            return middle
        elif target < potential_match:
            right = middle - 1
        else:
            left = middle + 1

    return -1
