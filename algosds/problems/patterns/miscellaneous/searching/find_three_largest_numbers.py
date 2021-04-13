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
    largest_integers = deque()

    while len(largest_integers) != 3:

        current_largest_idx = 0

        for idx in range(len(array)):
            if array[idx] >= array[current_largest_idx]:
                current_largest_idx = idx

        largest_integers.appendleft(array[current_largest_idx])
        swap(current_largest_idx, array)
        array.pop()

    return list(largest_integers)


def swap(current_largest_idx, array):
    array[-1], array[current_largest_idx] = array[current_largest_idx], array[-1]


# Time O(n)
# Space O(1)
def find_three_largest_numbers_elif(array):
    # largest_integers = deque([float('-inf'), float('-inf'), float('-inf')])
    largest_integers = deque([float('-inf') for _ in "123"])

    for idx in range(len(array)):

        if array[idx] >= largest_integers[2]:

            largest_integers.append(array[idx])
            largest_integers.popleft()

        elif largest_integers[1] <= array[idx] <= largest_integers[2]:

            largest_integers.popleft()
            shifted_value = largest_integers.popleft()
            largest_integers.appendleft(array[idx])
            largest_integers.appendleft(shifted_value)

        elif largest_integers[0] <= array[idx] <= largest_integers[1]:

            largest_integers[0] = array[idx]
            largest_integers.popleft()
            largest_integers.appendleft(array[idx])

    return list(largest_integers)


# Time O(n)
# Space O(1)
def find_three_largest_numbers_original(array):
    three_largest = [None, None, None]
    for num in array:
        update_largest(three_largest, num)
    return three_largest


def update_largest(three_largest, num):
    if three_largest[2] is None or num > three_largest[2]:
        shift_and_update(three_largest, num, 2)
    elif three_largest[1] is None or num > three_largest[1]:
        shift_and_update(three_largest, num, 1)
    elif three_largest[0] is None or num > three_largest[0]:
        shift_and_update(three_largest, num, 0)


def shift_and_update(array, num, idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i + 1]
