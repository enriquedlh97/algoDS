"""
Problem:

Given an non-empty array of different integers and a target sum integer,
find any pair that sums up to the target and return them.

When there is no pair summing up to the target return an empty array.

Single integers cannot be summed to themselves. The pair must be comprised
of different integers from the array.

There is at most one pair summing up to the target.

Input:
    array: [3, 5, -4, 8, 11, 1, -1, 6]
    target sum: 10

Output:
    [-1,11]
"""


# Time O(n^2)
# Space O(1)
def two_number_sum_for_loop(array, target_sum):
    for index, n_1 in enumerate(array):
        for n_2 in array[index + 1:]:
            if n_1 + n_2 == target_sum:
                return [n_1, n_2]

    return []


# Time O(n)
# Space O(n)
def two_number_sum_hash_table(array, target_sum):
    """
    Stores all number in hashtable allowing to access them in O(1),
    then checks if the complement of num to sum 10 is in the table.

    The complement is going to be another integer from the array.
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
