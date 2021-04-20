import os
import sys

import pytest

from algosds.problems.categories.recursion import product_sum

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


tests = [([5, 2, [7, -1], 3, [6, [-13, 8], 4]], 12),
         ([1, 2, 3, 4, 5], 15),
         ([1, 2, [3], 4, 5], 18),
         ([[1, 2], 3, [4, 5]], 27),
         ([[[[[5]]]]], 600),
         ([9,
           [2, -3, 4],
           1,
           [1, 1, [1, 1, 1]],
           [[[[3, 4, 1]]], 8],
           [1, 2, 3, 4, 5, [6, 7], -7],
           [1, [2, 3, [4, 5]],
            [6, 0, [7, 0, -8]], -7],
           [1, -3, 2, [1, -3, 2, [1, -3, 2], [1, -3, 2, [1, -3, 2]], [1, -3, 2]]],
           -3], 1351)]


@pytest.mark.parametrize("array, answer", tests)
def test_product_sum(array, answer):
    assert product_sum(array) == answer
