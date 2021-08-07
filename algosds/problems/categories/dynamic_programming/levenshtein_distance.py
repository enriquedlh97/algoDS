"""
Problem:

    Write a function that takes in two strings and returns the minimum number of edit operations that need to be
    performed on the first string to obtain the second string.

    There are three edit operations: insertion of a character, deletion of a character, and substitution of a character
    for another.

Input:

    str1: "abc"
    str2: "yabd"

Output:

    2 computed as insert "y" and substitute "c" for "d"

"""


# My first solution

# Time: O(n * d) time, where and m are the lengths of the first and second strings.
# Space: O(n * d) space
def levenshtein_distance_brute_force(str1, str2):
    """ My brute force solution

    :param str1: string
    :param str2: string
    :return: integer representing the smallest number of edits to turn str1 into str2
    """
    # We want str1 -> str2

    # Initialize results matrix
    results = initialize_results_brute_force(str1, str2)

    # Get min number of edits (Levenshtein distance)
    answer = get_min_edits_brute_force(str1, str2, results)

    return answer


def get_min_edits_brute_force(str1, str2, results):
    """ Helper function for my brute force solution, handles actual logic of computing min number of edits

    :param str1: string
    :param str2: string
    :param results:
    :return: integer representing the smallest number of edits to turn str1 into str2
    """
    for row_idx in range(len(str2)):
        for col_idx in range(len(str1)):
            if str1[col_idx] == str2[row_idx]:
                results[row_idx + 1][col_idx + 1] = results[row_idx][col_idx]
            else:
                results[row_idx + 1][col_idx + 1] = 1 + min(results[row_idx][col_idx],
                                                            results[row_idx][col_idx + 1],
                                                            results[row_idx + 1][col_idx])

    return results[-1][-1]


def initialize_results_brute_force(str1, str2):
    """ Helper function for my brute force solution, initializes results matrix

    :param str1: string
    :param str2: string
    :return:
    """
    # We want str1 -> str2
    results = []

    for row in range(len(str2) + 1):
        row_init = [row]
        for col in range(len(str1)):
            row_init.append(col + 1 if row == 0 else 0)

        results.append(row_init)

    return results


# My second solution
def levenshtein_distance_optimal(str1, str2):
    """ My optimal solution, linear space

    :param str1: string
    :param str2: string
    :return: integer representing the smallest number of edits to turn str1 into str2
    """
    # We want str1 -> str2

    # Handle base case with two empty strings
    if len(str1) == len(str2) == 0:
        return 0

    # Initialize results matrix
    results, small, big = initialize_results(str1, str2)

    # Get min number of edits (Levenshtein distance)
    answer = get_min_edits(small, big, results)

    return answer


def get_min_edits(small, big, results):
    """ Helper function for my optimal solution, computes actual min number of edits

    :param small:
    :param big:
    :param results:
    :return:
    """
    for row_idx in range(len(big)):

        for col_idx in range(len(small)):

            if small[col_idx] == big[row_idx]:

                results[1][col_idx + 1] = results[0][col_idx]

            else:
                results[1][col_idx + 1] = 1 + min(results[0][col_idx],
                                                  results[1][col_idx],
                                                  results[0][col_idx + 1])

        if row_idx != len(big) - 1:
            results[0], results[1] = results[1], [None for _ in range(len(small) + 1)]
            results[1][0] = row_idx + 2

    return results[-1][-1]


def initialize_results(str1, str2):
    """ Helper function for my optimal solution, initializes results array

    :param str1: string
    :param str2: string
    :return:
    """
    # Identifies smaller string
    small = str1 if len(str1) < len(str2) else str2
    big = str2 if len(str2) > len(str1) else str1

    results = [[x for x in range(len(small) + 1)]]

    second_row = [0 for _ in range(len(small) + 1)]
    # Change first value of second row to 1 edit
    second_row[0] = 1

    # Append second row to results array
    results.append(second_row)

    return results, small, big


# Original brute force solution
def levenshtein_distance_original_brute_force(str1, str2):
    """ Original brute force solution

    :param str1: string
    :param str2: string
    :return: integer representing the smallest number of edits to turn str1 into str2
    """
    edits = [[x for x in range(len(str1) + 1)] for _ in range(len(str2) + 1)]

    for i in range(1, len(str2) + 1):
        edits[i][0] = edits[i - 1][0] + 1

    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                edits[i][j] = edits[i - 1][j - 1]
            else:
                edits[i][j] = 1 + min(edits[i - 1][j - 1], edits[i - 1][j], edits[i][j - 1])

    return edits[-1][-1]


# Original optimal solution
def levenshtein_distance_original_optimal(str1, str2):
    """ Original optimal solution, linear space

    :param str1: string
    :param str2: string
    :return: integer representing the smallest number of edits to turn str1 into str2
    """
    small = str1 if len(str1) < len(str2) else str2
    big = str1 if len(str1) >= len(str2) else str2
    even_edits = [x for x in range(len(small) + 1)]
    odd_edits = [None for _ in range(len(small) + 1)]
    for i in range(1, len(big) + 1):
        if i % 2 == 1:
            current_edits = odd_edits
            previous_edits = even_edits
        else:
            current_edits = even_edits
            previous_edits = odd_edits
        current_edits[0] = i
        for j in range(1, len(small) + 1):
            if big[i - 1] == small[j - 1]:
                current_edits[j] = previous_edits[j - 1]
            else:
                current_edits[j] = 1 + min(previous_edits[j - 1], previous_edits[j], current_edits[j - 1])
    return even_edits[-1] if len(big) % 2 == 0 else odd_edits[-1]
