import os
import sys

import pytest

from algosds.problems.categories.dynamic_programming.number_of_ways_to_make_change import \
    number_of_ways_to_make_change_matrix, number_of_ways_to_make_change_linear_space, \
    number_of_ways_to_make_change_original


myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

tests = [(6, [1, 5], 2),
         (0, [2, 3, 4, 7], 1),
         (9, [5], 0),
         (7, [2, 4], 0),
         (4, [1, 5, 10, 25], 1),
         (5, [1, 5, 10, 25], 2),
         (10, [1, 5, 10, 25], 4),
         (25, [1, 5, 10, 25], 13),
         (12, [2, 3, 7], 4),
         (7, [2, 3, 4, 7], 3),
         ]


@pytest.mark.parametrize("n, denoms, answer", tests)
def test_number_of_ways_to_make_change_matrix(n, denoms, answer):
    assert number_of_ways_to_make_change_matrix(n, denoms) == answer


@pytest.mark.parametrize("n, denoms, answer", tests)
def test_number_of_ways_to_make_change_linear_space(n, denoms, answer):
    assert number_of_ways_to_make_change_linear_space(n, denoms) == answer


@pytest.mark.parametrize("n, denoms, answer", tests)
def test_number_of_ways_to_make_change_original(n, denoms, answer):
    assert number_of_ways_to_make_change_original(n, denoms) == answer
