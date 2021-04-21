import os
import sys

import pytest

from algosds.problems.categories.greedy_algorithms.tandem_bicycle import \
    tandem_bicycle, \
    tandem_bicycle_original

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


tests = [([3, 6, 7, 2, 1], [5, 5, 3, 9, 2], True, 32),
         ([3, 6, 7, 2, 1], [5, 5, 3, 9, 2], False, 25),
         ([3, 3, 4, 6, 1, 2], [1, 2, 1, 9, 12, 3], False, 30),
         ([3, 3, 4, 6, 1, 2], [1, 2, 1, 9, 12, 3], True, 37),
         ([3, 3, 4, 6, 1, 2, 5, 6, 34, 256, 123, 32], [1, 2, 1, 9, 12, 3, 1, 54, 21, 231, 32, 1], True, 816),
         ([3, 3, 4, 6, 1, 2, 5, 6, 34, 256, 123, 32], [1, 2, 1, 9, 12, 3, 1, 54, 21, 231, 32, 1], False, 484),
         ([5], [1], True, 5),
         ([5], [1], False, 5),
         ([1, 1, 1, 1], [1, 1, 1, 1], True, 4),
         ([1, 1, 1, 1], [1, 1, 1, 1], False, 4),
         ([1, 1, 1, 1, 3, 3, 3, 3, 5, 7], [1, 1, 1, 1, 2, 2, 2, 2, 9, 11], True, 48),
         ([1, 1, 1, 1, 3, 3, 3, 3, 5, 7], [1, 1, 1, 1, 2, 2, 2, 2, 9, 11], False, 36),
         ([3, 4, 4, 1, 1, 8, 9], [9, 8, 2, 2, 3, 5, 6], True, 49),
         ([3, 4, 4, 1, 1, 8, 9], [9, 8, 2, 2, 3, 5, 6], False, 35),
         ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], False, 15),
         ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], True, 21),
         ([], [], True, 0)]


@pytest.mark.parametrize("blue_shirt_speeds, red_shirt_speeds, fastest, answer", tests)
def test_tandem_bicycle(blue_shirt_speeds, red_shirt_speeds, fastest, answer):
    assert tandem_bicycle(red_shirt_speeds, blue_shirt_speeds, fastest) == answer
