"""
Problem:

Given an non-empty array of different integers and a target sum integer,
find any pair that sums up to the target and return them.

When there is no pair summing up to the target return an empty array.

Single integers cannot be summed to themselves. The pair must be comprised
of different integers from the array.

There is a maximum of one pair of numbers summing up to the target sum

Input:
    array: [3, 5, -4, 8, 11, 1, -1, 6]
    target sum: 10

Output:
    [-1,11]
"""


# Time O(n^2)
# Space O(1)
def two_number_sum_for_loop(array, target_sum):
    """  Searches pair sum with for loop

        Attributes:
            array: Non-empty array with possible integers
            target_sum: Target sum of any two number pair from array
    """
    for index, n_1 in enumerate(array):
        for n_2 in array[index + 1:]:
            if n_1 + n_2 == target_sum:
                return [n_1, n_2]

    return []


# Time O(n)
# Space O(n)
def two_number_sum_hash_table(array, target_sum):
    """  Searches pair sum with hash table

    Stores all number in hashtable allowing to access them in O(1),
    then checks if the complement of num to sum 10 is in the table.

    It traverses the array and searches for its complement to sum up to
    10 in the hash table. If it is not there, then adds the current int
    to the hash table for it to be checked ass complement of another int.

    complement = target sum - current int

    complement has to be in the hash table.

    Attributes:
        array: Non-empty array with possible integers
        target_sum: Target sum of any two number pair from array
    """
    sum_complement = {}
    for num in array:
        value_complement = target_sum - num
        if value_complement in sum_complement:  # checks if the complement is already in the table
            return [value_complement, num]
        else:
            # adds current num to table, which could be the complement to sum 10 of another int from the array
            sum_complement[num] = True

    return []


# Time O(nlg(n))
# Space O(1)
def two_number_sum_pointers(array, target_sum):
    """  Searches pair sum by sorting array

    The array is first sorted and then this sorted characteristic is used to search in O(n)

    Uses two pointers. One is initialized at the beginning of the array and the second one at the and.
    Then, the sum of both pointers is computed. If the sum is greater than the target sum,
    then the end pointer is lowered to the previous value. If it is too small, then the
    start pointer is switched to the next value.

    This is repeated until the sum is optimal. Works because the array is sorted.

    Note: Assumes that the ".sort()" function runs in O(nlg(n))
          With the sorted array, the answer is found in O(n)

    Attributes:
        array: Non-empty array with possible integers
        target_sum: Target sum of any two number pair from array
    """
    array.sort()
    right_pointer = len(array) - 1
    left_pointer = 0

    for _ in array:
        pointer_sum = array[left_pointer] + array[right_pointer]
        if pointer_sum == target_sum:
            return [array[left_pointer], array[right_pointer]]
        else:
            if pointer_sum < target_sum:
                left_pointer += 1
            else:
                right_pointer -= 1

    return []
