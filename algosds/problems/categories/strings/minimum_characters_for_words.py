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


# Time: O(n * l) time, where n is the number of words and l the length of the longest word
# Space: O(n * l) space as upper bound or O(c) space as lower bound where c is the number of unique characters across
#                 all words
def minimum_characters_for_words(words):
    """

    :param words: array of strings
    :return: array of characters containing the smallest array of characters needed to form all of the words
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
# Space: O(n * l) space as upper bound or O(c) space as lower bound where c is the number of unique characters across
#                 all words
def minimum_characters_for_words_original(words):
    """ Original solution

    This solution has two main steps. before these two steps are executed,  an initial dictionary is initialized with
    the name of maximum_character_frequencies. This dictionary is going to contain the output characters, that is, the
    smallest number of characters to form all words.

    Next, the solution iterates over every word from the input array. For each of these words, two steps are executed.
    First, the frequencies of the characters of the the word are determined and saved in a dictionary. Then, using this
    dictionary of character frequencies form the current word, the maximum_character_frequencies dictionary is updated.
    Whenever a character from the characters in the current word is not yet in the maximum_character_frequencies, then
    it is added. When it already is in it, then the value for the frequencies is set as the value with the higher
    frequencies. For example, of the character 'a' was already in the maximum_character_frequencies with a frequency of
    1 and the same character is found in the current word with a frequency of 2, then maximum_character_frequencies is
    updated and set to have a frequency of 2.

    This process is then repeated for all words, everytime updating the maximum_character_frequencies dictionary. At the
    end, the maximum_character_frequencies dictionary contains the smallest number of characters needed to from all
    words.

    This maximum_character_frequencies dictionary is then turned into an array where each character is contained as many
    times as the value for its frequency indicates it in the maximum_character_frequencies array. This output array is
    then returned as the final solution.

    This solution has a lower bound space complexity of O(c), this is because c is the maximum number of unique
    characters across all words. It is a lower bound because the maximum_character_frequencies dictionary will contain
    this many keys. Nevertheless, it could take more space if some characters appear more than once. For example, if the
    maximum_character_frequencies dictionary contains {"a": 3}, then the output array will contain ["a", "a", "a"].

    An upper bound for the space complexity is O(n * l) where n is the length of the array of words and l is the longest
    word where every single character in each word is unique across all words and the output array therefore contains
    n * l characters.

    The time complexity is O(n * l) because we first loop over all the n words and then, for each word, we loop over
    their characters, so l represents the word with the most characters.

    :param words: array of strings
    :return: array of characters containing the smallest array of characters needed to form all of the words
    """
    maximum_character_frequencies = {}

    # Loops over all n words
    for word in words:
        # Takes O(l) time to count frequencies of current word. l is the length of the word with the most characters
        character_frequencies = count_character_frequencies(word)
        # Updates maximum_character_frequencies in place
        update_maximum_frequencies(character_frequencies, maximum_character_frequencies)

    # Transforming the dictionary into array takes O(c) time, since there are at most c keys corresponding to the unique
    # characters
    return make_array_from_character_frequencies(maximum_character_frequencies)


# Time: O(l) time, where l is the length of the string
# Space: O(c) space where c is the number of unique characters in the string
def count_character_frequencies(string):
    """ Helper function for original solution to count the frequencies of characters in a string

    This helper function works by looping over all characters from the input string. Then, for each character, a check
    is performed to see if the character is already in the dictionary of character frequencies. If it is already in it,
    then, the frequency is updated. If it is not, then it is added with frequency of one.

    At then end, the dictionary is returned.

    :param string: string
    :return: dictionary with the unique characters of the string as keys and their frequencies as values
    """
    character_frequencies = {}

    for character in string:
        if character not in character_frequencies:
            character_frequencies[character] = 0

        character_frequencies[character] += 1

    return character_frequencies


# Time: O(c) space, where c is the number of unique characters in the string
# Space: O(c) space, where c is the number of unique characters in the string
def update_maximum_frequencies(frequencies, maximum_frequencies):
    """ Helper function for original solution to update the frequency of characters in the main dictionary

    This helper function works by looping over each key of the frequencies dictionary. For each key, if it is not yet in
    the maximum_frequencies it is added; otherwise, when the character is already in there, then if the current
    frequency of the character is bigger than the frequency in the maximum_frequencies dictionary, then it is updated.

    :param frequencies: dictionary containing the unique characters and their frequencies from the current word
    :param maximum_frequencies: main dictionary of the final maximum frequencies for each of the unique characters
           across all words
    :return: None (the maximum_frequencies dictionary is updated in place)
    """
    for character in frequencies:
        frequency = frequencies[character]

        if character in maximum_frequencies:
            maximum_frequencies[character] = max(frequency, maximum_frequencies[character])
        else:
            maximum_frequencies[character] = frequency


def make_array_from_character_frequencies(character_frequencies):
    """ Helper function for original solution to transform the main dictionary into the output array format

    :param character_frequencies: main dictionary of the final maximum frequencies for each of the unique characters
           across all words
    :return: array of characters in the corresponding frequency indicated in the character_frequencies dictionary
    """
    characters = []

    for character in character_frequencies:
        frequency = character_frequencies[character]

        for _ in range(frequency):
            characters.append(character)

    return characters
