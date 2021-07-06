"""
Problem:

    Write a function that takes in a string of words separated by one or more whitespaces and returns a string that has
    these words in reverse order. For example, given the string "tim is great" , your function should return
    "great is tim".

    For this problem, a word can contain special characters, punctuation, and numbers. The words in the string will be
    separated by one or more whitespaces, and the reversed string must contain the same whitespaces as the original
    string. For example, given the string "whitespaces    4" you would be expected to return "4    whitespaces".

    Note that you're not allowed to to use any built-in split or reverse methods/functions. However, you are allowed to
    use a built-in join method/function.

    Also note that the input string is not guaranteed to alwasy contian words.

Input:

    "string": "AlgoExpert is the best!"

Output:

    "best! the is AlgoExpert"

"""

from collections import deque


# Time: O(n) time, where w is the length of string
# Space: O(n) space
def reverse_words_in_string(string):
    """

    :param string:
    :return:
    """
    output = deque()
    current_word = ""

    for idx in range(0, len(string)):
        if string[idx] == " ":
            output.appendleft(current_word)
            current_word = ""
            output.appendleft(string[idx])
        else:
            current_word = "".join([current_word, string[idx]])

            if idx == len(string) - 1:
                output.appendleft(current_word)

    return "".join(output)


# Time: O(n) time, where w is the length of string
# Space: O(n) space
def reverse_words_in_string_original(string):
    """

    :param string:
    :return:
    """
    words = []
    start_of_word = 0

    for idx in range(len(string)):
        character = string[idx]

        if character == " ":
            words.append(string[start_of_word:idx])
            start_of_word = idx
        elif string[start_of_word] == " ":
            words.append(" ")
            start_of_word = idx

    words.append(string[start_of_word:])

    reverse_list(words)

    return "".join(words)


def reverse_list(characters):
    """

    :param characters:
    :return:
    """
    start, end = 0, len(characters) - 1

    while start < end:
        characters[start], characters[end] = characters[end], characters[start]
        start += 1
        end -= 1


# Time: O(n) time, where w is the length of string
# Space: O(n) space
def reverse_words_in_string_original2(string):
    """

    :param string:
    :return:
    """
    characters = [char for char in string]
    reverse_list_range(characters, 0, len(characters) - 1)

    start_of_word = 0
    while start_of_word < len(characters):
        end_of_word = start_of_word
        while end_of_word < len(characters) and characters[end_of_word] != " ":
            end_of_word += 1

        reverse_list_range(characters, start_of_word, end_of_word - 1)
        start_of_word = end_of_word + 1

    return "".join(characters)


def reverse_list_range(characters, start, end):
    """

    :param characters:
    :param start:
    :param end:
    :return:
    """
    while start < end:
        characters[start], characters[end] = characters[end], characters[start]
        start += 1
        end -= 1
