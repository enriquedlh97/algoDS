import os
import sys

import pytest

from algosds.problems.patterns.pattern_sliding_window.run_length_encoding import \
    run_length_encoding_single_for_loop, \
    run_length_encoding_double_for_loop, \
    run_length_encoding_original

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


tests = [("AAAAAAAAAAAAABBCCCCDD", "9A4A2B4C2D"),
         ("aA", "1a1A"),
         ("122333", "112233"),
         ("************^^^^^^^$$$$$$%%%%%%%!!!!!!AAAAAAAAAAAAAAAAAAAA", "9*3*7^6$7%6!9A9A2A"),
         ("aAaAaaaaaAaaaAAAABbbbBBBB", "1a1A1a1A5a1A3a4A1B3b4B"),
         ("                          ", "9 9 8 "),
         ("1  222 333    444  555", "112 321 334 342 35"),
         ("1A2BB3CCC4DDDD", "111A122B133C144D"),
         ("........______=========AAAA   AAABBBB   BBB", "8.6_9=4A3 3A4B3 3B"),
         ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
          "9a9a9a9a9a9a9a9a9a9a9a9a9a9a9a9a9a9a9a9a9a9a9a1a"),
         ("        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "8 9a9a9a9a9a4a"),
         (" ", "1 "),
         ("[(aaaaaaa,bbbbbbb,ccccc,dddddd)]", "1[1(7a1,7b1,5c1,6d1)1]"),
         (";;;;;;;;;;;;''''''''''''''''''''1233333332222211112222111s", "9;3;9'9'2'111273524142311s"),
         ("AAAAAAAAAAAAABBCCCCDDDDDDDDDDD", "9A4A2B4C9D2D")]


@pytest.mark.parametrize("string, answer", tests)
def test_run_length_encoding_single_for_loop(string, answer):
    assert run_length_encoding_single_for_loop(string) == answer


@pytest.mark.parametrize("string, answer", tests)
def test_run_length_encoding_double_for_loop(string, answer):
    assert run_length_encoding_double_for_loop(string) == answer


@pytest.mark.parametrize("string, answer", tests)
def test_run_length_encoding_original(string, answer):
    assert run_length_encoding_original(string) == answer
