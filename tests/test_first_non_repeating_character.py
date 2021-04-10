import os
import sys

import pytest

from algosds.problems.patterns.miscellaneous.hash_table.first_non_repeating_character import \
    first_non_repeating_character_brute_force, \
    first_non_repeating_character_hashmap_original, \
    first_non_repeating_character_hashtable

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

tests = [("abcdcaf", 1),
         ("faadabcbbebdf", 6),
         ("a", 0),
         ("ab", 0),
         ("abc", 0),
         ("abac", 1),
         ("ababac", 5),
         ("ababacc", -1),
         ("lmnopqldsafmnopqsa", 7),
         ("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy", 25),
         ("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", -1),
         ("", -1),
         ("ggyllaylacrhdzedddjsc", 10),
         ("aaaaaaaaaaaaaaaaaaaabbbbbbbbbbcccccccccccdddddddddddeeeeeeeeffghgh", -1),
         ("aabbccddeeff", -1)]


@pytest.mark.parametrize("string, answer", tests)
def test_first_non_repeating_character_brute_force(string, answer):
    assert first_non_repeating_character_brute_force(string) == answer


@pytest.mark.parametrize("string, answer", tests)
def test_first_non_repeating_character_hashmap_original(string, answer):
    assert first_non_repeating_character_hashmap_original(string) == answer


@pytest.mark.parametrize("string, answer", tests)
def test_first_non_repeating_character_hashtable(string, answer):
    assert first_non_repeating_character_hashtable(string) == answer
