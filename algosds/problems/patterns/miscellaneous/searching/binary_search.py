"""
Problem:

Write a function that takes in a sorted array of integers and a target integer. The function should use the Binary
Search algorithm to determine if the target integer is contained in the array and should return its index if it is,
otherwise it should return -1.

Input:
    array: [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    target: 33

Output:
    3
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
