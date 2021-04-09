"""
Problem:

Write a function that takes in a non-empty string and returns its run-length encoding.

A run-length encoding is a form of lossless data compression in which runs of data are stored as a single data value and
count, rather than as the original run. In this problem, a run of data is any sequence of CONSECUTIVE, identical
characters. So the run "AAA" would be run-length-encoded as "3A". Notice how "AAABBAA" contains 3 different runs which
would be encoded as 3A2B3A. The idea is to be able to get the original sequence from the encoding.

To make things more complicated, however, the input string can contain all sorts of special characters, including
numbers. And since encoded data must be decodable, this means that we cannot naively run-length-encode long runs. For
example, the run "AAAAAAAAAAAA" (12 As), cannot be naively encoded as 12A, since this string can be decoded as either
"AAAAAAAAAAAA" or "1AA". Thus, long runs (runs of 10 or more characters) should be encoded in a split fashion; the
aforementioned run should be encoded as 9A3A.

Input:
    string: "AAAAAAAAAAAAABBCCCCDD"

Output:
    "9A4A2B4C2D"
"""

import math


# Time O(n), where n is the length of the string
# Space O(n),
def run_length_encoding_double_for_loop(string):
    """ Counts the elements of a run and waits until the run is over to add them to the encoded string

    This solution traverses a single run until it is over, that means until it finds a different character or it reaches
    the end of the string. After it gets the number of elements in the run it proceeds to add them to the encoded string
    and dealing with runs greater than 9 elements. It does this by dividing the total run number by 9, which gives the
    times that blocks of 9 complete elements are found int he run. The remainder, always less than 9, is computed by
    subtracting the multiples of 9 from the total run amount, this gives always a number less than 9. Each 9 block is
    appended to the encoded string in a for loop.

    At first, by seeing 2 for loops one may think this solution runs in O(n^2) but in reality the second for loop runs
    the same number of times as the other to linear solutions. The difference is that the other solutions append the
    current amount of the run once it reaches 9, and then resets the counter. In this case, we wait until the end of the
    run to append the values at the end of the run, not every time it reaches 9 elements. This means that the operations
    done are the same, and instead of doing them everytime the count hits 9, it waits until the run is over and performs
    all the operations at once.

    To handle for the last character, when the input string is received, an additional character is added to the end of
    the string which is different than the current last character.

    :param string: non-empty string to be encoded
    :return: run-length-encoded input string
    """
    string = "".join([string, chr(ord(string[-1]) + 1)])
    encoded_run = []
    run_count = 1
    for idx in range(1, len(string)):
        if string[idx] == string[idx - 1]:
            run_count += 1
        if string[idx] != string[idx - 1] or idx == len(string):
            loops = math.floor(run_count / 9)
            remainder = run_count - 9 * loops
            for loop in range(loops):
                encoded_run.append("9")
                encoded_run.append(string[idx - 1])
            if remainder > 0:
                encoded_run.append(str(remainder))
                encoded_run.append(string[idx - 1])

            run_count = 1

    return "".join(encoded_run)


def run_length_encoding_single_for_loop(string):
    """ Counts the elements of a run and adds the encoded values to the string, if count hits 9 it adds incrementally

    This is the same as the previous solution, the difference is that instead of waiting at the end of every run, the
    run count is added to the encoded string everytime the count hits 9 elements. Then the count is restarted.

    To handle for the last character, when the input string is received, an additional character is added to the end of
    the string which is different than the current last character.

    :param string: non-empty string to be encoded
    :return: run-length-encoded input string
    """
    string = "".join([string, chr(ord(string[-1]) + 1)])
    encoded_run = []
    run_count = 1
    for idx in range(1, len(string)):
        if string[idx] == string[idx - 1]:
            if run_count < 9:
                run_count += 1
            else:
                encoded_run.append("9")
                encoded_run.append(string[idx - 1])
                run_count = 1
        if string[idx] != string[idx - 1] or idx == len(string):
            encoded_run.append(str(run_count))
            encoded_run.append(string[idx - 1])

            run_count = 1

    return "".join(encoded_run)


def run_length_encoding_original(string):
    """ Original solution, counts element sin run and adds them incrementally to finals tring.

    This is the same as the previous solution. The elements in runs are counted and if the count reaches 9, the element
    is added to the output encoded string, the count is reset and it continuous if necessary. The difference is that for
    dealing with the last element of the string, the previous solution adds a different character at the end of the
    input string. Instead, this solution just adds whatever the count for the last element is.

    :param string: non-empty string to be encoded
    :return: run-length-encoded input string
    """
    encoded_characters = []
    current_run_length = 1

    for i in range(1, len(string)):
        current_character = string[i]
        previous_character = string[i - 1]

        if current_character != previous_character or current_run_length == 9:
            encoded_characters.append(str(current_run_length))
            encoded_characters.append(previous_character)
            current_run_length = 0

        current_run_length += 1

    encoded_characters.append(str(current_run_length))
    encoded_characters.append(string[-1])

    return "".join(encoded_characters)
