import os
import sys

import pytest

from algosds.problems.patterns.pattern_two_pointers.two_number_sum import \
    two_number_sum_for_loop, \
    two_number_sum_hash_table, \
    two_number_sum_pointers

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

tests = [([3, 5, -4, 8, 11, 1, -1, 6], 10, [-1, 11]),
         ([4, 6], 10, [4, 6]),
         ([4, 6, 1], 5, [4, 1]),
         ([4, 6, 1, -3], 3, [6, -3]),
         ([1, 2, 3, 4, 5, 6, 7, 8, 9], 17, [8, 9]),
         ([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 18, [3, 15]),
         ([-7, -5, -3, -1, 0, 1, 3, 5, 7], -5, [-5, 0]),
         ([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 163, [210, -47]),
         ([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 164, []),
         ([3, 5, -4, 8, 11, 1, -1, 6], 15, []),
         ([14], 15, []),
         ([15], 15, [])]


@pytest.mark.parametrize("array, target_sum, result", tests)
def test_two_number_sum_for_loop(array, target_sum, result):
    assert sorted(two_number_sum_for_loop(array, target_sum)) == sorted(result)


@pytest.mark.parametrize("array, target_sum, result", tests)
def test_two_number_sum_hash_table(array, target_sum, result):
    assert sorted(two_number_sum_hash_table(array, target_sum)) == sorted(result)


@pytest.mark.parametrize("array, target_sum, result", tests)
def test_two_number_sum_pointers(array, target_sum, result):
    assert sorted(two_number_sum_pointers(array, target_sum)) == sorted(result)
