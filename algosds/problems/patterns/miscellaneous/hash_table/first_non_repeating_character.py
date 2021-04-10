"""
Problem:

Write a function that takes in a string of lowercase English-alphabet letters and returns the index of the string's
first non-repeating character.

The first non-repeating character is the first character in a string that occurs only once.

If the input string does not have any non-repeating characters, the function should return -1.

Input:
    string: "abcdcaf"

Output:
    1
    where the first non-repeating character is "b" and is found at index 1
"""


def first_non_repeating_character_brute_force(string):
    """ Uses two for loops (second one is nested) to check for duplicates for each character

    :param string: string to be checked for non-repeating characters
    :return: -1 if no non-repeating character is found; otherwise, returns the index of first non-repeating character
    """
    # Iterate over each character
    for idx in range(len(string)):
        found_duplicate = False  # indicates if a duplicate has been found for the current character

        # with the current character, iterate once again over the string to look for duplicates
        for idx2 in range(len(string)):
            # check if it is duplicate, making sure they are in different indices
            if string[idx] == string[idx2] and idx != idx2:
                found_duplicate = True
                break
        if not found_duplicate:  # If no duplicate was found, the current character is the first non-repeating character
            return idx

    return -1  # In case no non-repeating character is found


def first_non_repeating_character_hashmap_original(string):
    """

    :param string: string to be checked for non-repeating characters
    :return: -1 if no non-repeating character is found; otherwise, returns the index of first non-repeating character
    """
    character_frequencies = {}  # hashmap to keep characters and their frequencies

    # loop over each character
    for character in string:
        # This adds a character to the hashmap with a value of 0 in case it does not exists and then adds 1, if it does
        # exist in the hashmap, then it just gets it and adds 1
        character_frequencies[character] = character_frequencies.get(character, 0) + 1

    # loop over string once again and search the character in the hashmap to get the first one that occurs only once
    for idx in range(len(string)):  # Uses index because we want to return it
        character = string[idx]
        if character_frequencies[character] == 1:
            return idx

    return -1  # In case no non-repeating character is found


# Time O(n + c), where n is the length of the string and c is the number of non-repeating characters,
# it could also be considered just O(n) because m is always going to be, at most, as
# large as and, so assuming they are the same size, we could just say:
# O(n + n) -> O(2n) -> O(n)
# Space O(m), where m is the number of unique characters in the string, could also be considered O(1)
# because hashtables, together, will never have more than the 26 characters of the
# english alphabet
def first_non_repeating_character_hashtable(string):
    """

    :param string: string to be checked for non-repeating characters
    :return: -1 if no non-repeating character is found; otherwise, returns the index of first non-repeating character
    """
    new_character = {}
    seen_characters = {}
    first_non_repeating_idx = len(string)

    if string:

        for idx in reversed(range(0, len(string))):
            if string[idx] not in new_character and string[idx] not in seen_characters:
                new_character[string[idx]] = idx
            elif string[idx] in new_character:
                del new_character[string[idx]]
                seen_characters[string[idx]] = True

        if new_character:
            for key in new_character:
                if new_character[key] <= first_non_repeating_idx:
                    first_non_repeating_idx = new_character[key]

            return first_non_repeating_idx
        else:
            return -1
    else:
        return -1
