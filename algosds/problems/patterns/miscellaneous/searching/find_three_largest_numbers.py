"""
Problem:

Write a function that takes in an array of at least three integers and, without sorting the input array, returns a
sorted array of the three largest integers in the input array.

The function should return duplicate integers if necessary; for example, it should return [10, 10, 12] for an input
array of [10, 5, 9, 10, 12].

Input:
    array: [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]

Output:
    [18, 141, 541]
"""

from collections import deque


# Time O(n)
# Space O(1)
def find_three_largest_numbers_deque_swap(array):
    """ Uses Deque as data structure and swaps to update array with 3 largest elements

    This solution uses a while loop to populate the integer array of the largest 3 elements. It executes as long as it
    is not full.

    Then, a for loop is used to traverse the input array once. For each value traversed by the for loop, the index of
    the largest value is selected. After the for loop traverses the inout array, it adds the current largest element of
    the array to the deque by prepending it. Then, the element is swapped with the last element of the input array and
    then, the last element is popped. This reduces the size of the array.

    After this, the deque has the largest element of the input array, the input array has one less element (the largest)
    and the process starts again. The reduced input array is searched once again to find the current largest value.
    Since, the absolute largest value has already been popped from the input array, the new largest value is actually
    the second largest value. Once this value is gotten, it is prepended to the deque, swapped with the las element of
    the input array and then popped out.

    This means that the input array is going to be traversed k times, where k is the number of k largest elements. This
    yields a time complexity of O(kn) but since k is a constant value, in this case k=3, the time complexity ends up
    being O(n). The space complexity is O(1).

    Swapping the largest element on each run with the last element of the array allows to pop the last element of the
    array to reduce the input array. This is important because swain (which involves getting and setting operations),
    as well as popping the last element, are all constant time operations, ie O(1). If instead, the largest element was
    popped in place, ie pop(idx_largest_element) that would be an operation of O(n) time, yielding an algorithm of
    O(n^2) time complexity.

    :param array: array of size >= 3 to be searched for the largest 3 integers
    :return: array with the largest 3 elements sorted in ascending order
    """
    largest_integers = deque()

    while len(largest_integers) != 3:  # Essentially is like a for loop that runs 3 times (3 loops)

        current_largest_idx = 0  # Initializes largest element to first element of the array

        for idx in range(len(array)):  # Loops over the input array
            if array[idx] >= array[current_largest_idx]:
                current_largest_idx = idx  # Keeps track of the largest element of the array

        largest_integers.appendleft(array[current_largest_idx])  # Prepends the largest element to array of 3 elements
        # Swaps current largest value to last value of array. Essentially puts current largest value at the end of the
        # array.
        swap(current_largest_idx, array)
        # Pops the largest value out of the array, reducing the size of the array by one element.
        array.pop()

    return list(largest_integers)  # Casting list() is O(n) time operation, so does not affect over all time complexity


def swap(current_largest_idx, array):
    """ Helper function for deque swap solution, helps to swap largest element with last element of the array

    :param current_largest_idx: Index of the current largest value in the array
    :param array: input array that is being searched for the largest 3 integers
    :return: input array with the current largest value as the last element of the array.
    """
    array[-1], array[current_largest_idx] = array[current_largest_idx], array[-1]


# Time O(n)
# Space O(1)
def find_three_largest_numbers_elif(array):
    """ Only traverses the input array once, actively updates output array elements.

    This solution only traverses the input array once. On each iteration, the output array with the largest 3 elements
    is populated by checking if the current element should be the first, second or third element of the output array, or
    if it should not go in the output array.

    Popping operations are used to update the values, all popping operations used in this solutions are O(1) time since
    they only pop last and initial elements.

    :param array: array of size >= 3 to be searched for the largest 3 integers
    :return: array with the largest 3 elements sorted in ascending order
    """
    # largest_integers = deque([float('-inf'), float('-inf'), float('-inf')])
    largest_integers = deque([float('-inf') for _ in "123"])

    for idx in range(len(array)):

        if array[idx] >= largest_integers[2]:  # Checks if it is bigger than current largest element

            # If it is, it then pops out the third/smallest largest element and appends the new largest element.
            # It is like shifting the array by one element to the left
            largest_integers.append(array[idx])
            largest_integers.popleft()

        # Checks if it is bigger than current second largest element (middle element in the output array)
        elif largest_integers[1] <= array[idx] <= largest_integers[2]:

            # If it is, it pops the first element twice, which is like taking out the third/smallest largest element and
            # the second largest element. Since the second largest element should now be the third/smallest largest
            # element, this value is saved. Then the new current second largest element is prepended. After that the
            # saved element (previously second largest element and now third/smallest largest element) is prepended to
            # the array.

            largest_integers.popleft()  # third/smallest largest element is popped out
            shifted_value = largest_integers.popleft()  # second largest element is popped out and saved
            largest_integers.appendleft(array[idx])  # new second largest element is prepended
            largest_integers.appendleft(shifted_value)  # saved previously second largest element is prepended

        # Checks if it is bigger than current third/smallest largest element
        elif largest_integers[0] <= array[idx] <= largest_integers[1]:

            # If it is , then the the current third/smallest largest element is popped out and the new third/smallest
            # largest is prepended
            largest_integers.popleft()
            largest_integers.appendleft(array[idx])

    return list(largest_integers)


# Time O(n)
# Space O(1)
def find_three_largest_numbers_original(array):
    """ Traverses the array once, actively updates output array elements. Uses for loop to shift output array elements

    This solution loops once over the input array. For each element it checks if it the current element should take the
    the place of the current largest, second largest or third largest element in the output array or if it should not
    take any place in the output array. Depending on which place it takes, the current elements of the the output array
    are shifted using a for loop.

    :param array: array of size >= 3 to be searched for the largest 3 integers
    :return: array with the largest 3 elements sorted in ascending order
    """
    three_largest = [None, None, None]
    for num in array:
        update_largest(three_largest, num) # For each element the output array is updated if necessary
    return three_largest


def update_largest(three_largest, num):
    """ Helper function to check if a value should be int he current largest elements array and in which position

    Checks if the current element should be the first, second or third element of the output array, or
    if it should not go in the output array.

    Depending on the previous check, the array if shifted if necessary.

    :param three_largest: array containing the current three largest elements
    :param num: Integer representing the element to be checked if it should be in the array of current largest elements
    :return: None
    """
    if three_largest[2] is None or num > three_largest[2]:
        shift_and_update(three_largest, num, 2)
    elif three_largest[1] is None or num > three_largest[1]:
        shift_and_update(three_largest, num, 1)
    elif three_largest[0] is None or num > three_largest[0]:
        shift_and_update(three_largest, num, 0)


def shift_and_update(array, num, idx):
    """

    :param array: Array of current largest elements, it is to be updated
    :param num: New value that should be in array. Should be in index specified in idx
    :param idx: Integer representing the index that the num value should take in the array. It is also the index from
                which the shifting should start
    :return: None
    """
    for i in range(idx + 1):  # Adds one to the range because the range is non-inclusive.
        if i == idx:
            # If the current index form the for loop iteration is the same as the new index specified as parameter that
            # indicates the position that the new value "num" should take in the array, then the value is set to num.
            array[i] = num
        else:
            # Otherwise, the current index takes the value of the element at the next index, this is basically a shift
            # to the left
            array[i] = array[i + 1]
