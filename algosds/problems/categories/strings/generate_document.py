"""
Problem:

Your are given a string of available characters and a string representing a document that you need to generate. Write a
function that determines if you can generate the document using the available characters. If you can generate the
document the function should return True; otherwise, it should return False.

You are only able to generate the document if the frequency of unique characters in the characters string is greater
than or equal than to the frequency of unique characters in the document string. For example, if you are given
characters = "abcabc" and document = "aabbccc" you cannot generate the document because you are missing once c.

The document that you need to create may contain any characters, including special characters, capital letters, numbers
and spaces.

You can always generate the empty string "".

Input:
    characters: "aheaollabbhb"
    document: "hello"

Output:
    True
"""


# Time O( nlg(n) + mlg(m) ), where n is the length of available characters string and m the length of document
# Space O(n + m), where n is the length of available characters string and m the length of document
def generate_document_sorting(characters, document) -> bool:
    """ Sorts both input strings and checks if a character is not available

    This solution first sorts both the characters and document string. This take O(nlg(n)) and O(mlg(m)) respectively,
    assuming the characters string is of length n, and the document string is of length m.

    Then, it iterates over each character of the sorted document string. Everytime the first character from the sorted
    document string is the same as the first character from the the sorted characters string, both of these characters
    are popped ".pop(0)". If these characters are different, then only the character from the sorted characters string
    is popped. This procedure continues until either the document string or the characters string are empty. When the
    document string is empty, that indicates that the document can, in deed, be generated. If the characters string is
    empty and the document string is not yet empty, then that is an indication that the document cannot be generated.

    An extra check is added at the beginning returning False whenever the characters string has a smaller length than
    the document string.

    :param characters: string containing the available characters
    :param document: string containing the target that is to be checked if it can be generated
    :return: Returns True if the document string can be generated from the characters string; return False otherwise
    """
    if len(document) <= len(characters):
        characters_sorted = sorted(characters)
        document_sorted = sorted(document)

        character_available = True

        while character_available and len(document_sorted) != 0:

            if document_sorted[0] == characters_sorted[0]:
                characters_sorted.pop(0)
                document_sorted.pop(0)
            else:
                characters_sorted.pop(0)

            if len(characters_sorted) == 0 and len(document_sorted) > 0:
                return False

        return True

    else:
        return False


# Time O( m * (n +m) ), where n is the length of available characters string and m the length of document
# Space O(1)
def generate_document_multiple_counts(characters, document) -> bool:
    """ Checks if enough characters are available by counting the number of occurrences multiple (unnecessary) times

    This solution iterates over each character in the document string. For each character, it then counts the number fo
    occurrences of this character in both the document and characters string. This is very inefficient because if there
    are multiple repeated characters, it will count the occurrence of these characters multiple times instead of
    storing the count in some way.

    For example, if document = "aaaa" it will count the number of a's 4 times, since it will get the total for every
    character in the document, ie 4.

    This solution returns False whenever it finds that there are not enough characters to cover the ones indicated in
    document.

    :param characters: string containing the available characters
    :param document: string containing the target that is to be checked if it can be generated
    :return: Returns True if the document string can be generated from the characters string; return False otherwise
    """
    for character in document:

        document_frequency = count_character_frequency(character, document)
        characters_frequency = count_character_frequency(character, characters)

        if document_frequency > characters_frequency:
            return False

    return True


# Time O( c * (n +m) ), where n is the length of available characters string and m the length of document and c the
#                       number of unique characters in the characters string
# Space O(c), where c is the number of unique characters in the characters string
def generate_document_single_counts(characters, document) -> bool:
    """ Checks if enough characters are available by only counting the occurrence of each unique character once

    This solution is almost the same as the previous one. The only difference is that the count for each unique
    character is only done once, and the result is saved in a set.

    The conditions used are the same.

    :param characters: string containing the available characters
    :param document: string containing the target that is to be checked if it can be generated
    :return: Returns True if the document string can be generated from the characters string; return False otherwise
    """
    already_counted = set()

    for character in document:
        if character in already_counted:
            continue

        document_frequency = count_character_frequency(character, document)
        characters_frequency = count_character_frequency(character, characters)

        if document_frequency > characters_frequency:
            return False

        already_counted.add(character)

    return True


def count_character_frequency(character, target) -> int:
    """ Helper function for multiple counts and single counts solutions

    This function is used by the two previous solutions (multiple counts and single counts) to get the frequency of a
    given character in the target string.

    :param character: string containing the character for which its frequency is to be determined.
    :param target: string to be checked for the frequency of the character.
    :return: int representing the frequency that the character appears in the target string.
    """
    frequency = 0
    for char in target:
        if char == character:
            frequency += 1

    return frequency


# Time O(n +m), where n is the length of available characters string and m the length of document
# Space O(c), where c is the number of unique characters in the characters string
def generate_document_hashtable_original(characters, document) -> bool:
    """ Saves characters occurrences in hashtable, then compares with document string (original)

    This solution iterates over the characters string and saves the unique characters in a hash table along with their
    occurrences.

    Them, it iterates over each character of the document string and subtracts 1 from the corresponding character in the
    hash table.

    Whenever a character from the document string is not found in the hashtable, or whenever the count in the hashtable
    goes bellow 0 if one more unit is subtracted, then it returns False; otherwise returns True.

    :param characters: string containing the available characters
    :param document: string containing the target that is to be checked if it can be generated
    :return: Returns True if the document string can be generated from the characters string; return False otherwise
    """
    character_counts = {}

    for character in characters:
        if character not in character_counts:
            character_counts[character] = 0

        character_counts[character] += 1

    for character in document:
        if character not in character_counts or character_counts[character] == 0:
            return False

        character_counts[character] -= 1

    return True


# Time O(n +m), where n is the length of available characters string and m the length of document
# Space O(c), where c is the number of unique characters in the characters string
def generate_document_hashtable(characters, document) -> bool:
    """ Saves characters occurrences in hashtable, then compares with document string

    This solution is the exact same as the previous one, with minor differences in the implementation in the form of an
    extra check is added at the beginning returning False whenever the characters string has a smaller length
    than the document string. The code is structured a little different, but the logic is the exact same.

    :param characters: string containing the available characters
    :param document: string containing the target that is to be checked if it can be generated
    :return: Returns True if the document string can be generated from the characters string; return False otherwise
    """
    if len(document) <= len(characters):

        available_characters = {}

        for character in characters:

            if character not in available_characters:
                available_characters[character] = 0

            available_characters[character] += 1

        for character in document:

            if character not in available_characters:
                return False
            else:
                if available_characters[character] - 1 < 0:
                    return False
                else:
                    available_characters[character] -= 1

        return True

    else:
        return False
