"""
Problem:

Write a function that takes in a "special" array and returns its product sum.

A "special" array is a non-empty array that contains either integers or other "special" arrays. The product sum of a
"special" array is the sum of its elements, where "special" array inside it are summed themselves and then multiplied by
their level of depth.

The depth of a "special" array is how far nested it is. For instance, the depth of [] is 1; the depth of the inner array
in [[]] is 2; the depth of the innermost array in [[[]]] is 3.

Therefore, the product sum of [x, y] is x + y; the product sum of [x, [y, z]] is x + 2 * (y + z); the product sum of
[x, [y, [z]]] is x + 2 * (y + 3z).

Input:
    array: [5, 2, [7, -1], 3, [6, [-13, 8], 4]]

Output:
    12 calculated as: 5 + 2 + 2 * (7 - 1) + 3 + 2 * (6 + 3 * (-13 + 8) + 4)
"""


# Time O(n), where n is the total number of elements in the array, including sub-elements
# Space O(d), where d is the greatest depth of "special" arrays in the array
def product_sum(array, multiplier=1):
    """ Recursive solution (same as original, hence not included)

    Runs in O(n) time because each element is visited only once, hence it is like iterating over each
    element once.

    The space complexity is O(d) because, for instance, in [5, 2, [7, -1], 3, [6, [-13, 8], 4]] the maximum depth is d=3
    where the original array is level 1, then the array [6, [-13, 8], 4] is level 2, and finally array [-13, 8] is level
    3. This means that there are going to be at most 3 function calls in the call stack at a given time.

    :param array: non-empty "special" array
    :param multiplier: integer indicating the depth level of the current array
    :return: the product sum of the input "special array"
    """
    total = 0

    for element in array:
        if type(element) == int:
            total += element
        else:
            total += product_sum(element, multiplier + 1)

    return multiplier * total
