import os
import sys

import pytest

from algosds.problems.categories.dynamic_programming.max_subset_sum_no_adjacent import \
    max_subset_sum_no_adjacent_brute_force, max_subset_sum_no_adjacent_optimal, \
    max_subset_sum_no_adjacent_brute_force_original, max_subset_sum_no_adjacent_optimal_original


myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


tests = [([75, 105, 120, 75, 90, 135], 330),
         ([], 0),
         ([1], 1),
         ([1, 2], 2),
         ([1, 2, 3], 4),
         ([1, 15, 3], 15),
         ([7, 10, 12, 7, 9, 14], 33),
         ([4, 3, 5, 200, 5, 3], 207),
         ([10, 5, 20, 25, 15, 5, 5, 15], 60),
         ([10, 5, 20, 25, 15, 5, 5, 15, 3, 15, 5, 5, 15], 90),
         ([125, 210, 250, 120, 150, 300], 675),
         ([30, 25, 50, 55, 100], 180),
         ([30, 25, 50, 55, 100, 120], 205),
         ([7, 10, 12, 7, 9, 14, 15, 16, 25, 20, 4], 72),
         ]


@pytest.mark.parametrize("array, answer", tests)
def test_max_subset_sum_no_adjacent_brute_force(array, answer):
    assert max_subset_sum_no_adjacent_brute_force(array) == answer


@pytest.mark.parametrize("array, answer", tests)
def test_max_subset_sum_no_adjacent_optimal(array, answer):
    assert max_subset_sum_no_adjacent_optimal(array) == answer


@pytest.mark.parametrize("array, answer", tests)
def test_max_subset_sum_no_adjacent_brute_force_original(array, answer):
    assert max_subset_sum_no_adjacent_brute_force_original(array) == answer


@pytest.mark.parametrize("array, answer", tests)
def test_max_subset_sum_no_adjacent_optimal_original(array, answer):
    assert max_subset_sum_no_adjacent_optimal_original(array) == answer
