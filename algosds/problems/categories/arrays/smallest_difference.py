"""
Problem:

Write a function that takes in two non-empty arrays of integers, finds the pair of numbers (one from each array) whose
absolute difference is closest to zero, and returns an array containing these two numbers, with the number from the
first array in the first position.

Note that the absolute difference of two integers is the distance between them on the real number line. For example,
the absolute difference of -5 and 5 is 10, and the absolute difference of -5 and -4 is 1.

You can assume that there will only be one pair of numbers with the smallest difference.

Input:

array_one = [-1, 5, 10, 20, 28, 3]
array_two = [26, 134, 135, 15, 17]

Output:

 [28, 26]

"""


# Time O( Alg(A) + Blg(B) ), where A and B are the lengths of the first and second input arrays respectively
# Space O(1)
def smallest_difference_original(array_one, array_two):
    """ Original solution

    This solution works by first sorting both input arrays and initializing pointers to the first element of each
    array. Then the variable smallest and current are initialize to infinity. The smallest represents the smallest
    difference being ket track of and current represents the current difference of the integers to which the pointers
    point to.

    A while loop is started where it is executed as long as the pointers hold values less than the actual length of the
    input arrays. Whenever a pointer reaches the end of an input array, regardless of where the other pointer points at,
    the while loop is stopped. This is because one the end of an array us reached, there is no point in searching bigger
    numbers from the other array since only bigger differences are going to be generated.

    When the first number (array_one[idx_one]) is smaller than the second number (array_two[idx_two), then to make the
    difference between these two numbers the first pointer is incremented by one.

    Otherwise, when the second number is smaller than the first number, the second pointer is incremented by one. This
    has the same effect as before reducing the difference between these two numbers.

    Each time the current variable is updated with the current difference and compared with the smallest to see if the
    smallest pair and smallest difference has to be updated.

    Whenever the current variable is zero, the while loop is stopped and the current pair is returned as the solution.

    When the while loop ends, the last smallest pair is returned as the solution.

    The full time complexity would be O( Alg(A) + Blg(B) + A + B ) but the last two terms are dropped.

    :param array_one: non-empty array of integers
    :param array_two: non-empty array of integers
    :return: array containing two integers (the first one from the input array one and the second one from the input
        array two) representing the two integers that have the smallest absolute difference.
    """
    array_one.sort()
    array_two.sort()
    idx_one = 0
    idx_two = 0
    smallest = float("inf")
    current = float("inf")
    smallest_pair = []
    while idx_two < len(array_one) and idx_two < len(array_two):
        first_num = array_one[idx_one]
        second_num = array_two[idx_two]
        if first_num < second_num:
            current = second_num - first_num
            idx_one += 1
        elif second_num < first_num:
            current = first_num - second_num
            idx_two += 1
        else:
            return [first_num, second_num]
        if smallest > current:
            smallest = current
            smallest_pair = [first_num, second_num]

    return smallest_pair


# Time O( Alg(A) + Blg(B) ), where A and B are the lengths of the first and second input arrays respectively
# Space O(1)
def smallest_difference(array_one, array_two):
    """ My solution

    This solution follows the same logic as the original solution, it is just implemented a little different.

    The current_pair variable is immediately initialized with first values of each input array. Moreover, the variables
    current_difference and smallest difference are initialized with the actual current difference of the current pair.

    In this case, for incrementing the values of each pointer the current_difference variable is used.

    The main idea is the following one (A corresponds to input array one and B to input array two).

    1) if A - B is +, then increment pointer two (pointer for array B)
    2) if A - B is -, then increment pointer one (pointer for array A)

    Both conditions are meant to generate a smaller difference between the two numbers and are equivalent to the
    conditions from the previous solution.

    :param array_one: non-empty array of integers
    :param array_two: non-empty array of integers
    :return: array containing two integers (the first one from the input array one and the second one from the input
        array two) representing the two integers that have the smallest absolute difference.
    """
    # Sort both arrays
    array_one.sort()
    array_two.sort()

    # Initialize a pointer for each array
    pointer_one = 0
    pointer_two = 0

    # Initialize solution array
    current_pair = [array_one[pointer_one], array_two[pointer_two]]

    # Initialize difference of current selected pair
    current_difference = array_one[pointer_one] - array_two[pointer_two]

    # Initialize smallest difference
    smallest_difference = array_one[pointer_one] - array_two[pointer_two]

    while pointer_one < len(array_one) and pointer_two < len(array_two):

        # Check if smallest possible difference is found
        if current_difference == 0:
            break

        elif current_difference > 0:
            # Increment array two if possible
            if pointer_two < len(array_two) - 1:
                pointer_two += 1
            else:
                break

        elif current_difference < 0:
            # Increment array one if possible
            if pointer_one < len(array_one) - 1:
                pointer_one += 1
            else:
                break

        # Update values
        current_difference, smallest_difference, current_pair = update_diff(current_difference, smallest_difference,
                                                                            current_pair, array_one[pointer_one],
                                                                            array_two[pointer_two])

    return current_pair


def update_diff(current_difference, smallest_difference, current_pair, value_one, value_two):
    """ Helper function for my solution

    :param current_difference: the difference between the current value one and two.
    :param smallest_difference: the over all smallest difference up to this point
    :param current_pair: the pair that generates the smallest_difference
    :param value_one: value to which the first pointer points to
    :param value_two: value to which the second pointer points to
    :return: updated values for current_difference, smallest_difference and current_pair
    """
    current_difference = value_one - value_two

    if abs(current_difference) < abs(smallest_difference):
        smallest_difference = current_difference
        current_pair = [value_one, value_two]

    return current_difference, smallest_difference, current_pair
