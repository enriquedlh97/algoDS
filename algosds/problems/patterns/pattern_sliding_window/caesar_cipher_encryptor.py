"""
Problem:

Given a non-empty string of lowercase letters and a non-negative integer representing a key, write a function that
returns a new string obtained by shifting every letter in the input string by k positions in the alphabet, where k is
the key.

Letters should "wrap" around the alphabet. For example, letter z shifted by one unit returns letter a.

Input:
    string: "xyz"
    key: 2

Output:
    "zab"
"""


# Time O(n), where n is the size of the string
# Space O(n),
def caesar_cipher_encryptor_hash(string, key):
    """ Gets UNICODE, adds shift and hashes (using modulo) to get new position

    This function iterates over each letter of the input string. For each letter, it gets the UNICODE value using the
    built-in ord() function. Then, 97 is subtracted from the gotten UNICODE value for the current letter. This is
    because the english lowercase alphabet in UNICODE goes from 97 (a) all the way up to 122 (z). So the value of 97 is
    subtracted to map the letters to a range going from 0 to 26, ie the number of letters in the english alphabet.
    This is useful because later the value of 26 is used to compute the modulo and "hash" the new letter to its
    corresponding index in the 0 to 26 map. If 97 was not subtracted, the modulo operator would not work for mapping the
    value of the letter to the 0 to 26 range.

    Mapping to this 0 to 26 range is useful because it indicates the value of the new letter. At the end, all that is
    needed is to shift back the 0-26 range into the 97-122 range, this is done simply by adding once again the 97 value.

    After the UNICODE of the current letter is gotten and it is mapped to the 0 to 26 range (by subtracting 97), then
    the key (shift) is added to get the new value of the shifted letter. With this value the remainder is computed using
    the modulo operator with the length of the alphabet, in this case 26. This modulo operation and the fact that
    the UNICODE letter were mapped to the 0-25 range means that we can effectively "wrap" around the alphabet.

    :param string: non-empty string containing the input letters
    :param key: non-negative integer indicating the number of units the letters should be shifted
    :return: string containing the shifted letters
    """
    shifted_letters = []
    for letter in string:
        shifted_letters.append(chr((ord(letter) - 97 + key) % 26 + 97))
    return "".join(shifted_letters)


# Time O(n), where n is the size of the string
# Space O(n),
def caesar_cipher_encryptor_hash_original(string, key):
    """ Gets UNICODE, adds adjusted shift and hashes (using modulo) to get new position

    Similar to the previous one, but it does not map the string to a new range, instead it adjusts the key by using the
    modulo operator with 26. To wrap around the alphabet it checks if the shifted letter code is grater than 122 ('z'),
    if it is, then it uses the modulo operator to map ot to the range 97 - 122, if it is not, then it just returns the
    character corresponding to the code.

    :param string: non-empty string containing the input letters
    :param key: non-negative integer indicating the number of units the letters should be shifted
    :return: string containing the shifted letters
    """
    shifted_letters = []
    adjusted_key = key % 26
    for letter in string:
        shifted_letters.append(get_new_letter_hash_helper(letter, adjusted_key))
    return "".join(shifted_letters)


def get_new_letter_hash_helper(letter, key):
    """ Gets the new shifted letter

    :param letter: non-empty character containing a particular letter
    :param key: non-negative integer indicating the number of units the letters should be shifted
    :return: character representing the new shifted letter
    """
    new_letter = ord(letter) + key
    return chr(new_letter) if new_letter <= 122 else chr(96 + new_letter % 122)


# Time O(n), where n is the size of the string
# Space O(n),
def caesar_cipher_encryptor_alphabet_original(string, key):
    """ Creates a list with the alphabet, computes as previous functions.

    It works the same as the hash original function, the only difference is that is manually creates a list containing
    the alphabet.
    
    :param string: non-empty string containing the input letters
    :param key: non-negative integer indicating the number of units the letters should be shifted
    :return: string containing the shifted letters
    """
    shifted_letters = []
    adjusted_key = key % 26
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for letter in string:
        shifted_letters.append(get_new_letter_alphabet_helper(letter, adjusted_key, alphabet))
    return "".join(shifted_letters)


def get_new_letter_alphabet_helper(letter, key, alphabet):
    """ Gets the new shifted letter

    Finds the current letter in the alphabet array, adds the key and finds the new shifted letter by hashing the new
    value with modulo to get the new position wrapped around the length of the alphabet.

    :param letter: non-empty character containing a particular letter
    :param key: non-negative integer indicating the number of units the letters should be shifted
    :param alphabet:
    :return: character representing the new shifted letter
    """
    new_letter = alphabet.index(letter) + key
    return alphabet[new_letter % 26]
