import os
import sys

import pytest

from algosds.problems.categories.dynamic_programming.levenshtein_distance import levenshtein_distance_brute_force, \
    levenshtein_distance_optimal, levenshtein_distance_original_brute_force, levenshtein_distance_original_optimal


myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

tests = [("abc", "yabd", 2),
         ("", "", 0),
         ("", "abc", 3),
         ("abc", "abc", 0),
         ("abc", "abx", 1),
         ("abc", "abcx", 1),
         ("abc", "yabcx", 2),
         ("algoexpert", "algozexpert", 1),
         ("abcdefghij", "1234567890", 10),
         ("abcdefghij", "a234567890", 9),
         ("biting", "mitten", 4),
         ("cereal", "saturday", 6),
         ("cereal", "saturdzz", 7),
         ("abbbbbbbbb", "bbbbbbbbba", 2),
         ("xabc", "abcx", 2),
         ("table", "bal", 3),
         ("gumbo", "gambol", 2),
         ]


@pytest.mark.parametrize("str1, str2, answer", tests)
def test_levenshtein_distance_brute_force(str1, str2, answer):
    assert levenshtein_distance_brute_force(str1, str2) == answer


@pytest.mark.parametrize("str1, str2, answer", tests)
def test_levenshtein_distance_optimal(str1, str2, answer):
    assert levenshtein_distance_optimal(str1, str2) == answer


@pytest.mark.parametrize("str1, str2, answer", tests)
def test_levenshtein_distance_original_brute_force(str1, str2, answer):
    assert levenshtein_distance_original_brute_force(str1, str2) == answer


@pytest.mark.parametrize("str1, str2, answer", tests)
def test_levenshtein_distance_original_optimal(str1, str2, answer):
    assert levenshtein_distance_original_optimal(str1, str2) == answer
