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
    shifted_letters = []
    for letter in string:
        shifted_letters.append(chr((ord(letter) - 97 + key) % 26 + 97))
    return "".join(shifted_letters)


# Time O(n), where n is the size of the string
# Space O(n),
def caesar_cipher_encryptor_hash_original(string, key):
    shifted_letters = []
    adjusted_key = key % 26
    for letter in string:
        shifted_letters.append(get_new_letter(letter, adjusted_key))
    return "".join(shifted_letters)


def get_new_letter_hash_helper(letter, key):
    new_letter = ord(letter) + key
    return chr(new_letter) if new_letter <= 122 else chr(96 + new_letter % 122)


def caesar_cipher_encryptor_alphabet_original(string, key):
    shifted_letters = []
    adjusted_key = key % 26
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for letter in string:
        shifted_letters.append(get_new_letter_alphabet_helper(letter, adjusted_key, alphabet))
    return "".join(shifted_letters)


def get_new_letter_alphabet_helper(letter, key, alphabet):
    new_letter = alphabet.index(letter) + key
    return alphabet[new_letter % 26]
