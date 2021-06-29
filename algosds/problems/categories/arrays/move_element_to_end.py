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
    """ Original solution

    This solution works by initializing pointers to the beginning and end of the input array. The right pointer moves
    elements that do not correspond to the indicated value in the variable to_move. The left pointers moves elements
    that due correspond to the to_move value. Essentially, everytime both the left and right pointers find valid values
    they perform a swap.

    The execution is done until both pointers meet each other.

    :param array: Non-empty array of integers
    :param to_move: Integer corresponding to the values that have to be sent to the end of the original array
    :return: the original array with values corresponding to the to_move value sent to the back
    """
    i = 0
    j = len(array) - 1
    # This first while loop, makes sure that the right pointer is moved all the way down until a valid number is found.
    # This is done to prevent iterating over non-valid values.
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
    """ My solution, very similar to the original one

    This solution works basically the same as the previous original solution. The only exception is that there is no
    outer while loop.

    :param array: Non-empty array of integers
    :param to_move: Integer corresponding to the values that have to be sent to the end of the original array
    :return: the original array with values corresponding to the to_move value sent to the back
    """
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
# Space O(n)
def move_element_to_end_list_deque(array, to_move):
    """ My solution using deque

    This solution is very similar to the previous two solutions. The difference is that a for loop is used to iterate
    over the input array and the values that do not correspond to to_move values are popped out of the array and saved
    to a temporary one. The values that due correspond to the to_move value are popped and appended to the original
    array. At the end, the temporary array containing the non-valid values is prepended to the original array.

    This solution yields a higher space complexity, which in the worst case scenario will be O( n - 1 ) = O(n)

    :param array: Non-empty array of integers
    :param to_move: Integer corresponding to the values that have to be sent to the end of the original array
    :return: the original array with values corresponding to the to_move value sent to the back
    """
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
