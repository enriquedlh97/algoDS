"""
Problem:

Given two non-empy arrays of integers, write a function that determines whether the
second array is a subsequence of the first one.

A subsequence of an array is a set of numbers that aren't necessarily adjacent in the
array but are in the same order as they appear in the array. For example, the numbers \
[1, 3, 4] form a subsequence of the array [1, 2, 3, 4], and so do the numbers [2, 4].
A single number in an array and the array itself are both valid subsequences.

There is at least one element in the array

Input:
    array: [5, 1, 22, 25, 6, -1, 8, 10]
    sequence: [1, 6, -1, 10]

Output:
    True
"""


# Time O(n)
# Space O(1)
def is_valid_subsequence_for_loop_pop(array, sequence):
    """ Validates by comparing las elements of sequence with last elements of array

        Loops over the array comparing the last elements. A sequence is validated when
        the sequence array is empty. If the for loop finishes before the sequence then it
        not a sequence.

        Checks, before everything, if the sequence is longer than the array.


        Attributes:
            array: Non-empty array with integer
            sequence: Non-empty array to bu validated as sequence
    """
    if len(sequence) > len(array):
        return False

    for num in range(0, len(array)):
        # popping takes O(1)
        if array.pop() == sequence[-1]:
            sequence.pop()
            if not sequence:
                return True

    return False


# Time O(n)
# Space O(n)
def is_valid_subsequence_hash_table(array, sequence):
    """ Validates by comparing las elements of sequence with last elements of array

        Loops over the array comparing the last elements. A sequence is validated when
        the sequence array is empty. If the for loop finishes before the sequence then it
        not a sequence.

        When an element from the array is not the same as the current element
        from the sequence, then it gets added to a hashtable. This helps when the sequence is
        not in the proper order without having to wait to loop over the whole array to find out.
        Example: Array: [(1000 elements), 8, 2] sequence: [2, 8]
        The sequence is rendered invalid after checking the second element of the array, which
        is found in the hash table.

        This solution increases the Space complexity, but it helps in the cases like above.

        Checks, before everything, if the sequence is longer than the array.

        Attributes:
            array: Non-empty array with integer
            sequence: Non-empty array to bu validated as sequence
    """
    popped_elements = {}

    if len(sequence) > len(array):
        return False

    for num in range(0, len(array)):
        if sequence[-1] in popped_elements:
            return False
        else:
            array_pop = array.pop()
            if array_pop == sequence[-1]:
                sequence.pop()
                if not sequence:
                    return True
            else:
                popped_elements[array_pop] = True

    return False


# Time O(n)
# Space O(1)
def is_valid_subsequence_while(array, sequence):
    """ Validates by iterating over array and sequence (original solution)

        Is the same as the while one.

        Attributes:
            array: Non-empty array with integer
            sequence: Non-empty array to bu validated as sequence
    """
    array_idx = 0
    sequence_idx = 0
    while array_idx < len(array) and sequence_idx < len(sequence):
        if array[array_idx] == sequence[sequence_idx]:
            sequence_idx += 1
        array_idx += 1
    return sequence_idx == len(sequence)


# Time O(n)
# Space O(1)
def is_valid_subsequence_for_loop(array, sequence):
    """ Validates by iterating over array and sequence (original solution)

        Is the same as the for loop one.

        Attributes:
            array: Non-empty array with integer
            sequence: Non-empty array to bu validated as sequence
    """
    sequence_idx = 0
    for num in array:
        if sequence_idx == len(sequence):
            break
        if sequence[sequence_idx] == num:
            sequence_idx += 1
    return sequence_idx == len(sequence)