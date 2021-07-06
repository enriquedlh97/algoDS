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

    Also note that the input string is not guaranteed to always contain words.

Input:

    "string": "AlgoExpert is the best!"

Output:

    "best! the is AlgoExpert"

"""

from collections import deque


# Time: O(n) time, where w is the length of string
# Space: O(n) space
def reverse_words_in_string(string):
    """ My solution

    This solution works by looping over each character from the input string. Whenever a word is identified, then it is
    appended to the front of a deque. Whenever a single space is identified it is also immediately appended to the front
    of the deque.

    At the end the deque is turned into a list and the list is joined and turned into the reversed output string.

    :param string: input string
    :return: input string with the orders in reverse order
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
    """ Original solution, finds words, then reverses their order

    This solution works by first looping over all characters form the input string. For each characters a few checks are
    performed. To identify words, a variable called start_of_word is initialized to 0, corresponding to the first
    character in the string. As the loop executes, the idx variable keeps track of what is going to be the end of the
    word. We know we are at the end of a a word when the current idx points to a character corresponding to an empty
    space " ". Once this happens, the characters from start_of_word to the current idx (not inclusive) are appended to
    a list along with the empty space " ".

    This procedure continues until all words have been added to the words array.

    At the end this array is reversed with a custom function that then turns it into a string and returns it as output.

    :param string: input string
    :return: input string with the orders in reverse order
    """
    words = []
    start_of_word = 0

    # This operation takes O(n) time and O(n) space
    for idx in range(len(string)):
        character = string[idx]

        if character == " ":  # Checks if character at idx is a space
            words.append(string[start_of_word:idx])  # We append the word up to the current index but not including it
            start_of_word = idx  # Resets start of word
        elif string[start_of_word] == " ":  # Every time the start of word is a space we append it immediately
            words.append(" ")
            start_of_word = idx

    # This operation takes O(n) time
    # Makes sure the las word is added since it could happen that the last
    # character will not be a space " "
    words.append(string[start_of_word:])

    # This operation takes O(n) time
    reverse_list(words)

    return "".join(words)  # This operation takes O(n) time


def reverse_list(characters):
    """ Helper function for reverse_words_in_string_original, reverses array

     Works by swapping the first element with the first element and then continues inwards until the string is
     reversed.

    :param characters: string to be reversed
    :return: reversed characters string
    """
    start, end = 0, len(characters) - 1

    while start < end:
        characters[start], characters[end] = characters[end], characters[start]
        start += 1
        end -= 1


# Time: O(n) time, where w is the length of string
# Space: O(n) space
def reverse_words_in_string_original2(string):
    """ Original solution, reverses entire string, un-reverses words.

    This solution works by first reversing the entire string. So if the input string was

    "AlgoExpert is the best!"

    This puts the words in the correct output order. Once it is reverse it would look like this

    "!tseb eht si trepxEoglA"

    Then, each word is un-reversed. So we end up with the final solution

    "best! the is AlgoExpert"

    :param string: input string
    :return: input string with the orders in reverse order
    """
    characters = [char for char in string]  # Represent the string as a list to manipulate it more easily
    reverse_list_range(characters, 0, len(characters) - 1)  # Reverses list inplace

    start_of_word = 0
    while start_of_word < len(characters):
        end_of_word = start_of_word
        while end_of_word < len(characters) and characters[end_of_word] != " ":
            end_of_word += 1

        reverse_list_range(characters, start_of_word, end_of_word - 1)
        start_of_word = end_of_word + 1

    return "".join(characters)


def reverse_list_range(characters, start, end):
    """ Helper function for original solution 2, used for reversing individual words within a range of indices

    Works by swapping the first element with the first element and then continues inwards until the string is
    reversed.

    :param characters: string to be reversed
    :param start: integer indicating the start character
    :param end: integer representing the end character
    :return: original character string reversed
    """
    while start < end:
        characters[start], characters[end] = characters[end], characters[start]
        start += 1
        end -= 1
