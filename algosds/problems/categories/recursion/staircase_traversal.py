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
    """ My suboptimal dynamic programming solution

    This solution works by creating a table of size height * max_steps. Each entry in this table corresponds to a
    sub-problem. Dynamic programming is used to solve each sub-problem incrementally until the final original
    sub-problem is solved.

    For example, when

    height = 3
    max_steps = 2

    A table of sub-problems is created initialized as follows:

       height	0	1	2	3
    max steps
        0		1	0	0	0
        1		1	0	0	0
        2		1	0	0	0

    What this table shows is the results for the sub-problems where the height = 0 and for all steps (0, 1, 2).

    For the first sub-problem (0, 0) where the height = 0  and max steps = 0 the solution is 1 because we are
    essentially asking in how many ways we can climb a staircase of height 0. The only solution is to not do anything,
    that is why 1 is the answer. The important thing to notice is how this result will not change no matter the max step
    size. For that reason, the first column of sub-problems can be initialized with 1s.

    Then, to actually solve the rest of the sub-problems, we have to iterate for each step size and for each step size
    we iterate over each height. This means we essentially solve row by row. Another important thing is that we start
    solving from ste size 1 because the row containing the sub-problems for step size 0 is already solved in the
    initialization. All sub-problems but the first one are 0 because when the step size is 0, it is impossible to climb.

    For that reason, the first sub-problem that is solved is the one found at (1, 1) where max step = 1 and height = 1.

    All sub-problems are solved using the following formula (assuming results is the results matrix):

    results[current_step][height] = for step in (current_step to 0) sum -> results[current_step][height - step] when current_step < height
                                    results[current_step - 1][height]    when step > height

    What this formula essentially means is that there are two possibilities. The first one is when the current step is
    smaller than the height of the current sub-problem. The second possibility is when the step is bigger than the
    height in the current sub-problem.

    For the second case, when the step is bigger than the current sub-problem we just take the solution for the
    sub-problem with the current height but one ste size lower results[current_step - 1][height]. This is because when
    the step size is bigger than the height, nothing new is added.

    For the first case, when the step is smaller than the current height the solution is gotten iteratively. 



    :param height: integer representing the height of the staircase
    :param max_steps: integer representing the maximum step size
    :return: integer representing the number of ways to climb the staircase
    """
    # Initialize results array
    results = initialize_results(height, max_steps)

    # Compute number of ways
    for step_idx in range(1, max_steps + 1):

        for height_idx in range(1, height + 1):
            results[step_idx][height_idx] = get_result(step_idx, height_idx, results)

    return results[-1][-1]


def initialize_results(height, max_steps):
    """ helper function to initialize results array

    :param height: integer representing the height of the staircase
    :param max_steps: integer representing the maximum step size
    :return: array of initialized results
    """
    row_init = [0 for _ in range(height + 1)]
    row_init[0] = 1
    results = []
    for step in range(max_steps + 1):
        results.append(row_init)

    return results


def get_result(step_idx, height_idx, results):
    """ Helper function, performs actual logic

    :param step_idx:
    :param height_idx:
    :param results:
    :return:
    """
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
    """ My optimal dynamic programming solution

    :param height: integer representing the height of the staircase
    :param max_steps: integer representing the maximum step size
    :return: integer representing the number of ways to climb the staircase
    """
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
    """ Helper function, performs actual logic

    :param step_idx:
    :param height_idx:
    :param results:
    :return: integer representing the number of ways to climb the staircase
    """
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
    """ Original suboptimal recursive solution

    :param height: integer representing the height of the staircase
    :param max_steps: integer representing the maximum step size
    :return: integer representing the number of ways to climb the staircase
    """
    return number_of_ways_to_top(height, max_steps)


def number_of_ways_to_top(height, max_steps):
    """ Helper function, performs actual logic

    :param height: integer representing the height of the staircase
    :param max_steps: integer representing the maximum step size
    :return: integer representing the number of ways to climb the staircase
    """
    if height <= 1:
        return 1

    number_of_ways = 0

    for step in range(1, min(max_steps, height) + 1):
        number_of_ways += number_of_ways_to_top(height - step, max_steps)

    return number_of_ways


# O(k^n) time where n is the height and k the number of allowed steps
# O(n) space
def staircase_traversal_recursive_original_optimal(height, max_steps):
    """ Original optimal recursive solution

    :param height: integer representing the height of the staircase
    :param max_steps: integer representing the maximum step size
    :return: integer representing the number of ways to climb the staircase
    """
    return number_of_ways_to_top_optimal(height, max_steps, {0: 1, 1: 1})


def number_of_ways_to_top_optimal(height, max_steps, memoize):
    """ Helper function, performs actual logic

    :param height: integer representing the height of the staircase
    :param max_steps: integer representing the maximum step size
    :param memoize:
    :return: integer representing the number of ways to climb the staircase
    """
    if height in memoize:
        return memoize[height]

    number_of_ways = 0

    for step in range(1, min(max_steps, height) + 1):
        number_of_ways += number_of_ways_to_top_optimal(height - step, max_steps, memoize)

    return number_of_ways


# O(n * k) time where n is the height and k the number of allowed steps
# O(n) space
def staircase_traversal_dynamic_programming_original_suboptimal(height, max_steps):
    """ Original suboptimal dynamic programming solution

    :param height: integer representing the height of the staircase
    :param max_steps: integer representing the maximum step size
    :return: integer representing the number of ways to climb the staircase
    """
    ways_to_top = [0 for _ in range(height + 1)]
    ways_to_top[0], ways_to_top[1] = 1, 1

    for current_height in range(2, height + 1):
        step = 1
        while step <= max_steps and step <= current_height:
            ways_to_top[current_height] = ways_to_top[current_height] + ways_to_top[current_height - step]
            step += 1

    return ways_to_top[height]


# O(n) time where n is the height and k the number of allowed steps
# O(n) space
def staircase_traversal_dynamic_programming_original_optimal(height, max_steps):
    """ Original optimal dynamic programming solution

    :param height: integer representing the height of the staircase
    :param max_steps: integer representing the maximum step size
    :return: integer representing the number of ways to climb the staircase
    """
    current_number_of_ways = 0
    ways_to_top = [1]

    for current_height in range(1, height + 1):
        start_of_window = current_height - max_steps - 1
        end_of_window = current_height - 1

        if start_of_window >= 0:
            current_number_of_ways -= ways_to_top[start_of_window]

        current_number_of_ways += ways_to_top[end_of_window]
        ways_to_top.append(current_number_of_ways)

    return ways_to_top[height]
