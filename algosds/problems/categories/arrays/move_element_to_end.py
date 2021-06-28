"""
Problem:

You're given an array of integers and an integer. Write a function that moves all instances of that integer in the array
to the end of the array and returns the array.

The function should perform this in place (i.e„ it should mutate the input array) and doesnt need to maintain the order
of the other integers.

Input:

    array: [2, 1, 2, 2, 2, 3, 4, 2]
    to_move: 2

Output:

    [4, 1, 3, 2, 2, 2, 2, 2]

"""
from collections import deque


# Time O(n), where n is the length of the input array
# Space O(1)
def move_element_to_end_original(array, to_move):
    i = 0
    j = len(array) - 1
    while i < j:
        while i < j and array[j] == to_move:
            j -= 1
        if array[i] == to_move:
            array[i], array[j] = array[j], array[i]
        i += 1
    return array


# Time O(n), where n is the length of the input array
# Space O(1)
def move_element_to_end_list(array, to_move):
    # Initialize pointers
    left = 0
    right = len(array) - 1

    # Loop over array
    while left < right:
        if array[right] != to_move:
            if array[left] == to_move:
                array[left] = array[right]
                array[right] = to_move
                right -= 1
                left += 1
            else:
                left += 1
        else:
            right -= 1

    return array


# Time O(n), where n is the length of the input array
# Space O(1)
def move_element_to_end_list_deque(array, to_move):
    # Initialize temporary array for saving non-key elements
    temporary_array = []

    # Initialize array as deque
    new_array = deque(array)

    for _ in range(len(new_array)):
        value = new_array.popleft()
        if value == to_move:
            new_array.append(value)
        else:
            temporary_array.append(value)

    for x in temporary_array:
        new_array.appendleft(x)

    return list(new_array)

