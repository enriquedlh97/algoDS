"""
Problem:

    You are given two positive integers representing the height of a staircase and the maximum number of steps that you
    can advance up the staircase at a time. Write a function that returns the number of ways in which you can climb the
    staircase.

    For example, if you were given a staircase of height=3 and maxSteps=2 you could climb the staircase in 3 ways. You
    could take 1 step, 1 step, then 1 step, you could also take 1 step, then 2 steps, and you could take 2 steps, then 1
    step.

    Note that maxSteps <= height will always be true.

Input:

    height = 4
    maxSteps = 2

Output:

    5

    Computed as

    1) 1, 1, 1, 1
    2) 1, 1, 2
    3) 1, 2, 1
    4) 2, 1, 1
    5) 2, 2

"""


# O(n * m) time where n is the height and m the mx step size
# O(n * m) space
def staircase_traversal_dynamic_programming_suboptimal(height, max_steps):
    # Initialize results array
    results = initialize_results(height, max_steps)

    # Compute number of ways
    for step_idx in range(1, max_steps + 1):

        for height_idx in range(1, height + 1):
            results[step_idx][height_idx] = get_result(step_idx, height_idx, results)

    return results[-1][-1]


def initialize_results(height, max_steps):
    row_init = [0 for _ in range(height + 1)]
    row_init[0] = 1
    results = []
    for step in range(max_steps + 1):
        results.append(row_init)

    return results


def get_result(step_idx, height_idx, results):
    if step_idx > height_idx:
        return results[step_idx - 1][height_idx]

    else:
        result_value = 0

        for step_size in reversed(range(1, step_idx + 1)):
            result_value += results[step_idx][height_idx - step_size]

    return result_value


# O(n * m) time where n is the height and m the mx step size
# O(n) space
def staircase_traversal_dynamic_programming_optimal(height, max_steps):
    # Initialize results array
    results = [[0 for _ in range(height + 1)], [0 for _ in range(height + 1)]]
    results[0][0], results[1][0] = 1, 1

    # Compute number of ways
    for step_idx in range(1, max_steps + 1):

        for height_idx in range(1, height + 1):
            results[1][height_idx] = get_result_dp(step_idx, height_idx, results)

        if step_idx < max_steps:
            results[0], results[1] = results[1], [0 for _ in range(height + 1)]
            results[1][0] = 1

    return results[-1][-1]


def get_result_dp(step_idx, height_idx, results):
    if step_idx > height_idx:
        return results[0][height_idx]

    else:
        result_value = 0

        for step_size in reversed(range(1, step_idx + 1)):
            result_value += results[1][height_idx - step_size]

    return result_value


# O(k^n) time where n is the height and k the number of allowed steps
# O(n) space
def staircase_traversal_recursive_original(height, max_steps):
    return number_of_ways_to_top(height, max_steps)


def number_of_ways_to_top(height, max_steps):
    if height <= 1:
        return 1

    number_of_ways = 0

    for step in range(1, min(max_steps, height) + 1):
        number_of_ways += number_of_ways_to_top(height - step, max_steps)

    return number_of_ways


# O(k^n) time where n is the height and k the number of allowed steps
# O(n) space
def staircase_traversal_recursive_original_optimal(height, max_steps):
    return number_of_ways_to_top(height, max_steps, {0: 1, 1: 1})


def number_of_ways_to_top_optimal(height, max_steps, memoize):
    if height in memoize:
        return memoize[height]

    number_of_ways = 0

    for step in range(1, min(max_steps, height) + 1):
        number_of_ways += number_of_ways_to_top(height - step, max_steps, memoize)

    return number_of_ways


# O(n * k) time where n is the height and k the number of allowed steps
# O(n) space
def staircase_traversal_dynamic_programming_original_suboptimal(height, max_steps):
    ways_to_top = [0 for _ in range(height + 1)]
    ways_to_top[0], ways_to_top[1] = 1, 1

    for current_height in range(2, height + 1):
        step = 1
        while step <= max_steps and step <= current_height:
            ways_to_top[current_height] = ways_to_top[current_height] + ways_to_top[current_height - 1]
            step += 1

    return  ways_to_top[height]


# O(n) time where n is the height and k the number of allowed steps
# O(n) space
def staircase_traversal_dynamic_programming_original_optimal(height, max_steps):
    current_number_of_ways = 0
    ways_to_top = [1]

    for current_height in range(1, height + 1):
        start_of_window = current_height - max_steps - 1
        end_of_window = current_height - 1

        if start_of_window >=0:
            current_number_of_ways -= ways_to_top[start_of_window]

        current_number_of_ways += ways_to_top[end_of_window]
        ways_to_top.append(current_number_of_ways)

    return  ways_to_top[height]
