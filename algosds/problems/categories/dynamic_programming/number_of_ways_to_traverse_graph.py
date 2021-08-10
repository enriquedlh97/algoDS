"""
Problem:

    You are given two positive integers representing the width and height of a grid-shaped, rectangular graph.

    Write a function that returns the number of ways to reach the bottom right corner of the graph when starting at the
    top left corner. Each move you take must either go down or right. In other words, you can never move up or left in
    the graph.

    For example, given the graph illustrated below, width=2 and height=3, there are three ways to reach the bottom right
    corner when starting at the top left corner:

     ____
    |_|_|
    |_|_|
    |_|_|

    1. Down, Down, Right
    2. Right, Down, Down
    3. Down, Right, Down

    Note you may assume that width * height >= 2. In other words, the graph will never be a 1x1 grid.

Input:

    width: 4
    height: 3

Output:

    output: 10

"""


# Time: O(n * m) time, where n and m are the lengths of the first and second strings.
# Space: O(n * m) space
def number_of_ways_to_traverse_graph_recursive(width, height):
    """ My recursive solution

    :param width: Integer representing the height of the grid
    :param height: Integer representing the width of the grid
    :return: Integer representing the number of ways to traverse the graph from top left corner to bottom right corner
    """
    if width == 1 or height == 1:
        return 1
    else:
        return number_of_ways_to_traverse_graph_recursive(width - 1, height) + \
               number_of_ways_to_traverse_graph_recursive(width, height - 1)


# Time: O(n * m) time, where n and m are the lengths of the first and second strings.
# Space: O(n * m) space
def number_of_ways_to_traverse_graph_recursive_dynamic_programming(width, height):
    """ My solution using dynamic programming

    :param width: Integer representing the height of the grid
    :param height: Integer representing the width of the grid
    :return: Integer representing the number of ways to traverse the graph from top left corner to bottom right corner
    """
    # Build matrix and fill it with solutions
    results = []

    for col in range(width):
        column = []
        for row in range(height):
            if row == 0 or col == 0:
                column.append(1)
            else:
                column.append(results[col - 1][row] + column[-1])

        results.append(column)

    return results[-1][-1]
