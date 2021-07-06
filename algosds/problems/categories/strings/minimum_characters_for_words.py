"""
Problem:

    Write a function that takes in an array of words and returns the smallest array of characters needed to form all of
    the words. The characters don’t need to be in any particular order.

    For example, the characters [“y", "r", "o", "u"] are needed to form the words ["your", "you", "or", "yo"]

    Note: the input words won't contain any spaces; however, they might contain punctuation and/or special characters.

Input:

    "words": ["this", "that", "did", "deed", "them!", "a"]

Output:

    ["!", "a", "d", "d", "e", "e", "h", "i", "m", "s", "t", "t"]

"""


# Time: O(w*n*lg(n)) time, where w is the number of words and n the length of the longest word
# Space: O(w*n) space
def minimum_characters_for_words(words):
    """

    :param words:
    :return:
    """
    output_array = []
    unique_chars = {}

    for word in words:

        word_frequencies = {}

        for char in word:
            if char in word_frequencies:
                word_frequencies[char].append(char)
            else:
                word_frequencies[char] = [char]

        for key, values in word_frequencies.items():
            if key in unique_chars:
                if len(word_frequencies[key]) > len(unique_chars[key]):
                    unique_chars[key] = word_frequencies[key]
            else:
                unique_chars[key] = word_frequencies[key]

    for key, values in unique_chars.items():
        for char in values:
            output_array.append(char)

    return output_array


# Time: O(n * l) time, where n is the number of words and l the length of the longest word
# Space: O(c) space, where c is the number of unique characters across all words
def minimum_characters_for_words_original(words):
    """

    :param words:
    :return:
    """
    maximum_character_frequencies = {}

    for word in words:
        character_frequencies = count_character_frequencies(word)
        update_maximum_frequencies(character_frequencies, maximum_character_frequencies)

    return make_array_from_character_frequencies(maximum_character_frequencies)


def count_character_frequencies(string):
    """

    :param string:
    :return:
    """
    character_frequencies = {}

    for character in string:
        if character not in character_frequencies:
            character_frequencies[character] = 0

        character_frequencies[character] += 1

    return character_frequencies


def update_maximum_frequencies(frequencies, maximum_frequencies):
    """

    :param frequencies:
    :param maximum_frequencies:
    :return:
    """
    for character in frequencies:
        frequency = frequencies[character]

        if character in maximum_frequencies:
            maximum_frequencies[character] = max(frequency, maximum_frequencies[character])
        else:
            maximum_frequencies[character] = frequency


def make_array_from_character_frequencies(character_frequencies):
    """

    :param character_frequencies:
    :return:
    """
    characters = []

    for character in character_frequencies:
        frequency = character_frequencies[character]

        for _ in range(frequency):
            characters.append(character)

    return  characters
