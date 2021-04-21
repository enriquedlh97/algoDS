import os
import sys

import pytest

from algosds.problems.categories.greedy_algorithms.minimum_waiting_time import \
    minimum_waiting_time, \
    minimum_waiting_time_original

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


tests = [([3, 2, 1, 2, 6], 17),
         ([2, 1, 1, 1], 6),
         ([1, 2, 4, 5, 2, 1], 23),
         ([25, 30, 2, 1], 32),
         ([1, 1, 1, 1, 1], 10),
         ([7, 9, 2, 3], 19),
         ([4, 3, 1, 1, 3, 2, 1, 8], 45),
         ([2], 0),
         ([7], 0),
         ([8, 9], 8),
         ([1, 9], 1),
         ([5, 4, 3, 2, 1], 20),
         ([1, 2, 3, 4, 5], 20),
         ([1, 1, 1, 4, 5, 6, 8, 1, 1, 2, 1], 81),
         ([17, 4, 3], 10)]


@pytest.mark.parametrize("queries, answer", tests)
def test_minimum_waiting_time(queries, answer):
    assert minimum_waiting_time(queries) == answer


@pytest.mark.parametrize("queries, answer", tests)
def test_minimum_waiting_time_original(queries, answer):
    assert minimum_waiting_time_original(queries) == answer
