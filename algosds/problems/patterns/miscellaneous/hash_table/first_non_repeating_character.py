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


# Time O(n^2), where n is the length of the string
# Space O(1)
def first_non_repeating_character_brute_force(string):
    """ Uses two for loops (second one is nested) to check for duplicates for each character

    This solution loops over each character of the string and then, for each character, loops once again over the string
    and looks for a duplicate character (which has to be in a different index than the current character). If no
    duplicate is found, then it returns the current index, otherwise it continues with the next characters. If no
    non-repeating character is found, then it returns -1.

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


# Time O(n), where n is the length of the string
# Space O(1), constant because it has at most the number of letter in the english-alphabet (26)
def first_non_repeating_character_hashmap_original(string):
    """ Keeps track of character occurrences in hashtable

    This solution dos not have nested loops. Instead, in the first loop[, it creates a hashmap of all the characters in
    the string and the count of their occurrences. Then it loops once again over each character of the string and looks
    it up in the hash table, if it finds that the character has a count of 1, then it return its index, otherwise it
    continues traversing the string. If no character with 1 occurrence is found, then it returns -1.

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
    """ Keeps track of index and non-repeating characters with hashmaps

    This solution is similar to the previous one in that it uses hashmaps.

    First, there is check to verify that the string is not empty. If the string is empty, then -1 is returned; otherwise
    the string is checked for non-repeating characters.

    Then, there are 2 hashmaps, one is used for keeping track of new characters that have only been seen once in the
    string (potential non-repeating characters) and the second one is used to keep track of characters that have been
    seen more than once.

    The algorithm iterates over each character of the string. It checks if the current character is not in the
    new_character hashtable and the seen_characters, if it is in none of these hashtable, then it is added to the
    new_character hashtable along with its index.

    Whenever a character is found that is already in the new_character hashtable, it is deleted and added to the
    seen_characters hashtable. The result of this is that at the end, the new character hashtable has only the
    characters that are non-repeating along with their indices.

    To get the first non-repeating character we just iterate over the new_character hashtable and keep the character
    with the lowest index, then we just return that index.

    The complexity of this solution is the same as the previous one, both are optimal. Nevertheless, this solution si a
    little more efficient because it iterates once over the string and once over the non-repeating characters. So, for
    example, if the string is of length 50 and the number of non-repeating characters is 4 (assuming all 4 non-reaping
    characters are the las 4 elements of the string), this algorithm would do 50 + 4 = 54 operations and the previous
    algorithm would do 50 + 47 = 97 operations. Still the time complexity in O-notation is the same O(n).

    :param string: string to be checked for non-repeating characters
    :return: -1 if no non-repeating character is found; otherwise, returns the index of first non-repeating character
    """
    new_character = {}  # Holds potential non-repeating characters and their indices
    seen_characters = {}  # Holds characters seen more than once
    first_non_repeating_idx = len(string)  # Holds index of first non-repeating character

    if string:

        for idx in reversed(range(0, len(string))):
            # If the character is not yet in the new_character hashtable and the seen_characters hashtable it has only
            # been seen once, hence it is a potential non-repeating character
            if string[idx] not in new_character and string[idx] not in seen_characters:
                new_character[string[idx]] = idx
            # if it is already in the new_character hashtable then it has been seen already and it ahs to be removed
            elif string[idx] in new_character:
                del new_character[string[idx]]
                seen_characters[string[idx]] = True

        if new_character:  # Checks if it is not empty, indicating that there are non-repeating characters
            for key in new_character:
                # Compares the indices of all non-repeating characters and keeps the lowest one
                if new_character[key] <= first_non_repeating_idx:
                    first_non_repeating_idx = new_character[key]

            return first_non_repeating_idx
        else:
            return -1
    else:
        return -1
