"""
Problem:

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The
function should find all triplets in the array that sum up to the target sum and return a two-dimensional array of all
these triplets. The numbers in each triplet should be ordered in ascending order, and the triplets themselves should be
ordered in ascending order with respect to the numbers they hold.

If no three numbers sum up to the target sum, the function should return an empty array.

Input:

    array: [12, 3, 1, 2, -6, 5, -8, 6]
    target_sum = 0

Output:
    [[-8, 2, 6], [-8, 3, 5], -6, 1, 5]

"""


def three_number_sum(array, target_sum):
    """ Loops over array with one pointer and uses two more to complete the triplet

    This function uses three pointers, the first one loops over the array from the index 0 to the index len(array) - 2,
    the two other pointers correspond to the right and left pointers. The left pointer is always initialized right after
    the first pointer. The right pointer is always initialized at the last element of the array. So if the first pointer
    is a index 0, the left will be at index 1 and the right pointer at index len(array) - 1.

    As the first pointer loops over the array, the right and left pointers are moved to get a triplet that sums up to
    the target sum. If the current sum of the three pointers is less than the target sum, the left pointer is moved one
    step to the right. Otherwise, when the current sum is more than the target sum, the right pointer is moved one step.
    to the left.

    When a triplet is found that sums up to the target sum, both the left and right pointers are moved one step to the
    right and one the left respectively.

    When the left and right pointer are at index i and i+1, then after checking the triplet sum, the first pinter is
    moved up one step to the right, and the left and right pointers are reinitialized ti the corresponding initial
    positions.

    :param array: Non-empty array of distinct integers.
    :param target_sum: Integer value representing the target sum.
    :return: Two-dimensional array containing all triplets that sum up to the target sum. If no valid triplet is found,
        return an empty array.
    """
    # Initialize final triplets array
    triplets = []

    # Sort array
    array.sort()

    # Loop over array
    for idx in range(0, len(array) - 2):
        left = idx + 1
        right = len(array) - 1

        while left < right:
            current_sum = array[idx] + array[left] + array[right]

            if current_sum > target_sum:
                right -= 1
            elif current_sum < target_sum:
                left += 1
            else:
                triplets.append([array[idx], array[left], array[right]])
                left += 1
                right -= 1

    return triplets

