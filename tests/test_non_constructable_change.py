import os
import sys

import pytest

from algosds.problems.patterns.pattern_top_k_elements.non_constructable_change import \
    non_constructable_change_optimal, \
    non_constructable_change

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


tests = [([5, 7, 1, 1, 2, 3, 22], 20),
         ([1, 1, 1, 1, 1], 6),
         ([1, 5, 1, 1, 1, 10, 15, 20, 100], 55),
         ([6, 4, 5, 1, 1, 8, 9], 3),
         ([], 1),
         ([87], 1),
         ([5, 6, 1, 1, 2, 3, 4, 9], 32),
         ([5, 6, 1, 1, 2, 3, 43], 19),
         ([1, 1], 3),
         ([2], 1),
         ([1], 2),
         ([109, 2000, 8765, 19, 18, 17, 16, 8, 1, 1, 2, 4], 87),
         ([1, 2, 3, 4, 5, 6, 7], 29)]


@pytest.mark.parametrize("coins, answer", tests)
def test_non_constructable_change_optimal(coins, answer):
    assert non_constructable_change_optimal(coins) == answer


@pytest.mark.parametrize("coins, answer", tests)
def test_non_constructable_change(coins, answer):
    assert non_constructable_change(coins) == answer