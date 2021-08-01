import os
import sys

import pytest

from algosds.problems.categories.dynamic_programming.min_number_of_coins_for_change import \
    min_number_of_coins_for_change, min_number_of_coins_for_change_linear_space, min_number_of_coins_for_change_original


myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

tests = [(7, [1, 5, 10], 3),
         (7, [1, 10, 5], 3),
         (7, [10, 1, 5], 3),
         (0, [1, 2, 3], 0),
         (3, [2, 1], 2),
         (4, [1, 5, 10], 4),
         (10, [1, 5, 10], 1),
         (11, [1, 5, 10], 2),
         (24, [1, 5, 10], 6),
         (25, [1, 5, 10], 3),
         (7, [2, 4], -1),
         (7, [3, 7], 1),
         (9, [3, 5], 3),
         (9, [3, 4, 5], 2),
         (135, [39, 45, 130, 40, 4, 1], 3),
         (135, [39, 45, 130, 40, 4, 1, 60, 75], 2),
         (10, [1, 3, 4], 3),
         ]


@pytest.mark.parametrize("n, denoms, answer", tests)
def test_min_number_of_coins_for_change(n, denoms, answer):
    assert min_number_of_coins_for_change(n, denoms) == answer


@pytest.mark.parametrize("n, denoms, answer", tests)
def test_min_number_of_coins_for_change_linear_space(n, denoms, answer):
    assert min_number_of_coins_for_change_linear_space(n, denoms) == answer


@pytest.mark.parametrize("n, denoms, answer", tests)
def test_min_number_of_coins_for_change_original(n, denoms, answer):
    assert min_number_of_coins_for_change_original(n, denoms) == answer
