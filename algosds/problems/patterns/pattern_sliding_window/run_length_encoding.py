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
