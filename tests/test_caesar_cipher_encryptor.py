import os
import sys

import pytest

from algosds.problems.categories.strings.caesar_cipher_encryptor import \
    caesar_cipher_encryptor_hash, \
    caesar_cipher_encryptor_hash_original, \
    caesar_cipher_encryptor_alphabet_original

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


tests = [("xyz", 2, "zab"),
         ("abc", 0, "abc"),
         ("abc", 3, "def"),
         ("xyz", 5, "cde"),
         ("abc", 26, "abc"),
         ("abc", 52, "abc"),
         ("abc", 57, "fgh"),
         ("xyz", 25, "wxy"),
         ("iwufqnkqkqoolxzzlzihqfm", 25, "hvtepmjpjpnnkwyykyhgpel"),
         ("ovmqkwtujqmfkao", 52, "ovmqkwtujqmfkao"),
         ("mvklahvjcnbwqvtutmfafkwiuagjkzmzwgf", 7, "tcrshocqjuidxcabatmhmrdpbhnqrgtgdnm"),
         ("kjwmntauvjjnmsagwgawkagfuaugjhawgnawgjhawjgawbfawghesh", 15,
          "zylbcipjkyycbhpvlvplzpvujpjvywplvcplvywplyvplquplvwthw")]


@pytest.mark.parametrize("string, key, answer", tests)
def test_caesar_cipher_encryptor_hash(string, key, answer):
    assert caesar_cipher_encryptor_hash(string, key) == answer


@pytest.mark.parametrize("string, key, answer", tests)
def test_caesar_cipher_encryptor_hash_original(string, key, answer):
    assert caesar_cipher_encryptor_hash_original(string, key) == answer


@pytest.mark.parametrize("string, key, answer", tests)
def test_caesar_cipher_encryptor_alphabet_original(string, key, answer):
    assert caesar_cipher_encryptor_alphabet_original(string, key) == answer
