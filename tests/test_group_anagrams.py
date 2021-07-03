import os
import sys

import pytest

from algosds.problems.categories.strings.group_anagrams import group_anagrams_original_brute_force, \
    group_anagrams_original_hash_table, group_anagrams_hash_table


myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

# tests = [(["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"], ),
#          (, ),
#          (,),
#          (,),
#          (,),
#          (,),
#          (,),
#          (,),
#          (,),
#          (,),
#          (,),
#          (,),
#          (,),
#          (,)
#          ]
#
#
# @pytest.mark.parametrize("array, answer", tests)
# def test_group_anagrams_original_brute_force(array, answer):
#     assert group_anagrams_original_brute_force(array) == answer
#
#
# @pytest.mark.parametrize("array, answer", tests)
# def test_group_anagrams_original_hash_table(array, answer):
#     assert group_anagrams_original_hash_table(array) == answer
#
#
# @pytest.mark.parametrize("array, answer", tests)
# def test_group_anagrams_hash_table(array, answer):
#     assert group_anagrams_hash_table(array) == answer
