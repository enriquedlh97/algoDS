import os
import sys

import pytest

from algosds.problems.categories.arrays.monotonic_array import is_monotonic, is_monotonic_original


myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

tests = [([-1, -5, -10, -1100, -1100, -1101, -1102, -9001], True),
         ([], True),
         ([1], True),
         ([1, 2], True),
         ([2, 1], True),
         ([1, 5, 10, 1100, 1101, 1102, 9001], True),
         ([-1, -5, -10, -1100, -1101, -1102, -9001], True),
         ([-1, -5, -10, -1100, -900, -1101, -1102, -9001], False),
         ([1, 2, 0], False),
         ([1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 7, 9, 10, 11], False),
         ([1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 11], True),
         ([-1, -1, -2, -3, -4, -5, -5, -5, -6, -7, -8, -7, -9, -10, -11], False),
         ([-1, -1, -2, -3, -4, -5, -5, -5, -6, -7, -8, -8, -9, -10, -11], True),
         ([-1, -1, -1, -1, -1, -1, -1, -1], True),
         ([1, 2, -1, -2, -5], False),
         ([-1, -5, 10], False),
         ([2, 2, 2, 1, 4, 5], False),
         ([1, 1, 1, 2, 3, 4, 1], False),
         ([1, 2, 3, 3, 2, 1], False),
         ]


@pytest.mark.parametrize("array, answer", tests)
def test_is_monotonic(array, answer):
    assert is_monotonic(array) == answer


@pytest.mark.parametrize("array, answer", tests)
def test_is_monotonic_original(array, answer):
    assert is_monotonic_original(array) == answer
