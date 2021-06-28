import os
import sys

import pytest

from algosds.problems.categories.arrays.smallest_difference import smallest_difference, smallest_difference_original


myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

tests = [([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17], [28, 26]),
         ([-1, 5, 10, 20, 3], [26, 134, 135, 15, 17], [20, 17]),
         ([10, 0, 20, 25], [1005, 1006, 1014, 1032, 1031], [25, 1005]),
         ([10, 0, 20, 25, 2200], [1005, 1006, 1014, 1032, 1031], [25, 1005]),
         ([10, 0, 20, 25, 2000], [1005, 1006, 1014, 1032, 1031], [2000, 1032]),
         ([240, 124, 86, 111, 2, 84, 954, 27, 89], [1, 3, 954, 19, 8], [954, 954]),
         ([0, 20], [21, -2], [20, 21]),
         ([10, 1000], [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530], [1000, 1014]),
         ([10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123], [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530],
          [-123, -124]),
         ([10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123, 530], [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530],
          [530, 530])
         ]


@pytest.mark.parametrize("array_one, array_two, answer", tests)
def test_smallest_difference(array_one, array_two, answer):
    assert smallest_difference(array_one, array_two) == answer


@pytest.mark.parametrize("array_one, array_two, answer", tests)
def test_smallest_difference_original(array_one, array_two, answer):
    assert smallest_difference_original(array_one, array_two) == answer
