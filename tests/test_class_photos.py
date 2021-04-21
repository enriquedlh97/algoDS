import os
import sys

import pytest

from algosds.problems.categories.greedy_algorithms.class_photos import \
    class_photos_single_check, \
    class_photos_simultaneous_check

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


tests = [([6, 9, 2, 4, 5], [5, 8, 1, 3, 4], True),
         ([5, 8, 1, 3, 4], [6, 9, 2, 4, 5], True),
         ([5, 8, 1, 3, 4, 9], [6, 9, 2, 4, 5, 1], False),
         ([6], [6], False),
         ([125], [126], True),
         ([2, 3, 4, 5, 6], [1, 2, 3, 4, 5], True),
         ([5, 6, 7, 2, 3, 1, 2, 3], [1, 1, 1, 1, 1, 1, 1, 1], False),
         ([2, 2, 2, 2, 2, 2, 2, 2], [1, 1, 1, 1, 1, 1, 1, 1], True),
         ([126], [125], True),
         ([21, 5, 4, 4, 4, 4, 4, 4, 4], [19, 2, 4, 6, 2, 3, 1, 1, 4], False),
         ([20, 5, 4, 4, 4, 4, 4, 4], [19, 19, 21, 1, 1, 1, 1, 1], False),
         ([2, 4, 7, 5, 1], [3, 5, 6, 8, 2], True),
         ([2, 4, 7, 5, 1, 6], [3, 5, 6, 8, 2, 1], False),
         ([5, 4], [4, 5], False),
         ([5, 4], [5, 6], True)]


@pytest.mark.parametrize("blue_shirt_heights, red_shirt_heights, answer", tests)
def test_class_photos_single_check(blue_shirt_heights, red_shirt_heights, answer):
    assert class_photos_single_check(red_shirt_heights, blue_shirt_heights) == answer
