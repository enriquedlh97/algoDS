"""
Problem:

Write a function that takes in a non-empty array of integers and returns an array of the same length, where each element
in the output array is equal to the product of every other number in the array.

In other words, the value at output[i] is equal to the product of every number in the input array other than input[i].

Division cannot be used to solve this problem.

Input:

    array: [5, 1, 4, 2]

Output:

    output_array: [8, 40, 10, 20]

    where
    8 = 1 x 4 x 2
    40 = 5 x 4 x 2
    10 = 5 x 1 x 2
    20 = 5 x 1 x 4

"""


# Time O(n^2), where n is the length of the input array
# Space O(n)
def array_of_products_original_brute_force(array):
    """ Original brute force solution

    This solution works by iterating over the input array and, for every element, another iteration over the same array
    computes the products of all numbers. This product is computed whenever the outer and inner array values are
    different.

    :param array: array of integers
    :return: array of products
    """
    products = [1 for _ in array]

    for i in range(len(array)):
        running_product = 1
        for j in range(len(array)):
            if i != j:
                running_product *= array[j]
        products[i] = running_product

    return products


# Time O(n^2), where n is the length of the input array
# Space O(n)
def array_of_products_brute_force(array):
    """ My brute force solution

    This solution works almost the same as the previous one. The implementation is just a little different

    :param array: array of integers
    :return: array of products
    """
    output_array = []

    for current in range(len(array)):
        temp = array[current]
        array[current] = 1

        product_total = 1

        for value in array:
            product_total *= value

        output_array.append(product_total)
        array[current] = temp

    return output_array


# Time O(n), where n is the length of the input array
# Space O(n)
def array_of_products_slice(array):
    """ My linear solution that uses array slicing

    This solution works by iterating once over the input array and, at each step, multiplying the current value by all
    the elements of the output array that apply.

    For example, assuming the input_array: [5, 1, 4, 2] and output array is initialized with ones as
    output_array: [1, 1, 1, 1]

    On the first iteration, indices 1 to 3 should be multiplied by 5, so that is what is done. The result of this
    iteration is as follows:

    output_array: [1, 1 x 5, 1 x 5, 1 x 5] -> [1, 5, 5, 5]

    In the next step, indices 0 and 2 to 3 should be multiplied by 1. The result is as follows:

    output_array: [1 x 1, 5, 5 x 1, 5 x 1] -> [1, 5, 5, 5]

    In the next step, indices 0, 1 and 3 are multiplied by 4 yielding the following result.

    output_array: [1 x 4, 5 x 4, 5, 5 x 4] -> [4, 20, 5, 20]

    On the final step, indices 0 to 2 are multiplied by 2.

    output_array: [4 x 2, 20 x 2, 5 x 2, 20] -> [8, 40, 10, 20]

    And that is the final result.

    :param array: array of integers
    :return: array of products
    """
    output_array = [1 for _ in array]

    for idx in range(len(array)):
        output_array[:idx] = [array[idx] * value for value in output_array[:idx]]
        output_array[idx + 1:] = [array[idx] * value for value in output_array[idx + 1:]]

    return output_array


# Time O(n), where n is the length of the input array
# Space O(n)
def array_of_products_pointers(array):
    """ My linear solution using left and right pointers

    This solution is similar to the previous one but instead of working with slices, pointers are used. Similarly, the
    corresponding product is incremental computed at each step.

    First, a left_product and right_product are initialized with a value of 1.

    Then a for loop is executed, where the current value serves as left pointer and the right pointer is computed my
    multiplying the left pointer by -1 and subtracting 1. So right = left * (-1) - 1.

    At each step, the left_product and right_product are set as values in the output array corresponding to the
    positions indicated by the left and right pointers respectively. After this, the left_product and right_product are
    updated by being multiplied by the corresponding element at the current position of the array indicated by the left
    and right pointers.

    For example, assuming the input_array: [5, 1, 4, 2] and output array is initialized with ones as
    output_array: [1, 1, 1, 1] and left_product: 1 and right_product: 1

    On the first step,
    output_array: [1 x left_product, 1, 1, 1 x right_product] -> [1, 1, 1, 1]
    Then, the left_product and right_product are updated as follows
    left_product: left_product x 5 -> 1 x 5 = 5
    right_product: right_product x 2 -> 1 x 2 = 2

    On the next step,
    output_array: [1, 1 x left_product, 1 x right_product, 1] -> [1, 5, 2, 1]
    Then, the left_product and right_product are updated as follows
    left_product: left_product x 1 -> 5 x 1 = 5
    right_product: right_product x 4 -> 2 x 4 = 8

    On the next step,
    output_array: [1, 5 x right_product, 2 x left_product, 1] -> [1, 5 x 8, 2 x 5, 1] -> [1, 40, 10, 1]
    Then, the left_product and right_product are updated as follows
    left_product: left_product x 4 -> 5 x 4 = 20
    right_product: right_product x 1 -> 8 x 1 = 8

    Finally,
    output_array: [1 x right_product, 40, 10, 1 x left_product] -> [1 x 8, 40, 10, 1 x 20] -> [8, 40, 10, 20]
    Then, the left_product and right_product are updated but the values are not used.

    The output array is returned as the solution.
    
    :param array: array of integers
    :return: array of products
    """
    output_array = [1 for _ in array]

    product_left = 1
    product_right = 1

    for idx in range(len(array)):
        output_array[idx] = output_array[idx] * product_left
        output_array[idx * (-1) - 1] = output_array[idx * (-1) - 1] * product_right
        product_left *= array[idx]
        product_right *= array[idx * (-1) - 1]

    return output_array
