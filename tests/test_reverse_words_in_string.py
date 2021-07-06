import os
import sys

import pytest

from algosds.problems.categories.strings.reverse_words_in_string import reverse_words_in_string_original, \
    reverse_words_in_string_original2, reverse_words_in_string


myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

tests = [("AlgoExpert is the best!", "best! the is AlgoExpert"),
         ("Reverse These Words", "Words These Reverse"),
         ("..H,, hello 678", "678 hello ..H,,"),
         ("this this words this this this words this", "this words this this this words this this"),
         ("1 12 23 34 56", "56 34 23 12 1"),
         ("APPLE PEAR PLUM ORANGE", "ORANGE PLUM PEAR APPLE"),
         ("this-is-one-word", "this-is-one-word"),
         ("a", "a"),
         ("ab", "ab"),
         ("", ""),
         ("algoexpert is the best platform to use to prepare for coding interviews!",
          "interviews! coding for prepare to use to platform best the is algoexpert"),
         ("words, separated, by, commas", "commas by, separated, words,"),
         ("this      string     has a     lot of   whitespace", "whitespace   of lot     a has     string      this"),
         ("a ab a", "a ab a"),
         ("test        ", "        test"),
         (" ", " ")
         ]


@pytest.mark.parametrize("string, answer", tests)
def test_reverse_words_in_string_original(string, answer):
    assert reverse_words_in_string_original(string) == answer


@pytest.mark.parametrize("string, answer", tests)
def test_reverse_words_in_string_original2(string, answer):
    assert reverse_words_in_string_original2(string) == answer


@pytest.mark.parametrize("string, answer", tests)
def test_reverse_words_in_string(string, answer):
    assert reverse_words_in_string(string) == answer
