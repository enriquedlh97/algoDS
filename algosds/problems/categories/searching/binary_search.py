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


# Time O( lg(n) )
# Space O(1)
def binary_search_while(array, target):
    """ Uses while to test stop condition.

    This solution executes as long as the left pointer is not greater than the right pointer.
    On each iteration, all it does is check if the target element is the same as the middle element, if it is the  it
    returns the index of the middle element. Otherwise it checks if the right pointer and left pointer are pointing to
    the same value, and if they are it checks if the current value is the same at the the element being pointed to.

    If these conditions are not passed, then it  checks if the target element is bigger or lower than the middle
    pointer. Either case, the corresponding pointer is adjusted.

    If the target is less than middle element, then the right pointer is set to point to the element before the middle
    pointer. If the target element is bigger than the middle pointer, then the left pointer is set to point to the
    element next to the middle pointer.

    :param array: array to be searched containing elements sorted in ascending order.
    :param target: integer element that is being search in the input array element
    :return: integer representing the index of target element in the input array. If it is not found then -1 is returned
    """
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


# Time O( lg(n) )
# Space O( lg(n) ) because of the call stack
def binary_search_recursive(array, target, left_pointer=0, right_pointer=None):
    """ Recursive binary search algorithm

    This solutions checks if the target element is the same as the middle element, if it is then it returns the index of
    the middle element. Otherwise it checks if the right pointer and left pointer are pointing to
    the same value, and if they are it checks if the current value is the same ats the the element being pointed to. If
    they are the same, the index of the element is returned, if they are not the same that means the target is not in
    the array and -1 is returned.

    If none of this conditions are passed, then either the right or left pointer are updated, depending ont e one that
    should be updated and finally the function calls it self again (recursive operation) with the updated right and left
    pointers as parameters.

    :param array: array to be searched containing elements sorted in ascending order.
    :param target: integer element that is being search in the input array element
    :param left_pointer: integer representing the index to which left pointer points
    :param right_pointer: integer representing the index to which left pointer points
    :return:
    """
    if right_pointer is None:
        right_pointer = len(array) - 1

    middle_pointer = get_middle(left_pointer, right_pointer)

    # Checks base case right_pointer == left_pointer
    if target == array[middle_pointer]:
        return middle_pointer
    elif left_pointer == right_pointer and array[right_pointer] == target:
        return right_pointer
    elif left_pointer == right_pointer and array[right_pointer] != target:
        return -1
    # Adjust right and left pointer
    elif target < array[middle_pointer]:
        right_pointer = middle_pointer - 1
    elif target > array[middle_pointer]:
        left_pointer = middle_pointer + 1

    return binary_search_recursive(array, target, left_pointer, right_pointer)


def get_middle(left_pointer, right_pointer):
    """ Helper function for recursive and while algorithm to compute the middle

    :param left_pointer: integer representing the index to which left pointer points
    :param right_pointer: integer representing the index to which left pointer points
    :return: index to which the middle pointer should point
    """
    return (left_pointer + right_pointer) // 2


# Time O( lg(n) )
# Space O( lg(n) ) because of the call stack
def binary_search_recursive_original(array, target):
    """ Recursive binary search algorithm (original)

    :param array: array to be searched containing elements sorted in ascending order.
    :param target: integer element that is being search in the input array element
    :return: The value returned by the helper recursive function. This function returns the index of the target if found
             or -1 if not found.
    """
    return binary_search_recursive_helper(array, target, 0, len(array) - 1)


def binary_search_recursive_helper(array, target, left, right):
    """ Helper function for original recursive that performs the logic of searching for the target recursively

    :param array: array to be searched containing elements sorted in ascending order.
    :param target: integer element that is being search in the input array element
    :param left: integer representing the index to which left pointer points
    :param right: integer representing the index to which left pointer points
    :return: Returns the middle pointer when it is the same as the target value, otherwise it calls itself again until
             the target element is found or, if it is not found, return -1. When left is bigger than right
    """
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


# Time O( lg(n) )
# Space O(1)
def binary_search_while_original(array, target):
    """ Binary search algorithm with while to check for base case

    This is the same as the first while binary search algorithm. the only difference is that the stop criteria is either
    when the target element is found (meaning the middle pointer points to it) or when the left pointer is bigger than
    the left pointer

    :param array: array to be searched containing elements sorted in ascending order.
    :param target: integer element that is being search in the input array element
    :return: integer representing the index of target element in the input array. If it is not found then -1 is returned
    """
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
