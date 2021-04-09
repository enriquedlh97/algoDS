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
def generate_document_sorting(characters, document):
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
def generate_document_multiple_counts(characters, document):
    for character in document:

        document_frequency = count_character_frequency(character, document)
        characters_frequency = count_character_frequency(character, characters)

        if document_frequency > characters_frequency:
            return False

    return True


# Time O( c * (n +m) ), where n is the length of available characters string and m the length of document and c the
#                       number of unique characters in the characters string
# Space O(c), where c is the number of unique characters in the characters string
def generate_document_single_counts(characters, document):
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


def count_character_frequency(character, target):
    """ Helper function for multiple counts and single counts

    :param character:
    :param target:
    :return:
    """
    frequency = 0
    for char in target:
        if char == character:
            frequency += 1

    return frequency


# Time O(n +m), where n is the length of available characters string and m the length of document
# Space O(c), where c is the number of unique characters in the characters string
def generate_document_hashtable_original(characters, document):
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
def generate_document_hashtable(characters, document):
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
