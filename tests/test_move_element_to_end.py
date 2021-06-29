import os
import sys

import pytest

from algosds.problems.categories.arrays.move_element_to_end import move_element_to_end_list, \
    move_element_to_end_list_deque, move_element_to_end_original


myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

tests = [([2, 1, 2, 2, 2, 3, 4, 2], 2, [4, 1, 3, 2, 2, 2, 2, 2]),
         ([], 3, []),
         ([1, 2, 4, 5, 6], 3, [1, 2, 4, 5, 6]),
         ([3, 3, 3, 3, 3], 3, [3, 3, 3, 3, 3]),
         ([3, 1, 2, 4, 5], 3, [5, 1, 2, 4, 3]),
         ([1, 2, 4, 5, 3], 3, [1, 2, 4, 5, 3]),
         ([1, 2, 3, 4, 5], 3, [1, 2, 5, 4, 3]),
         ([2, 4, 2, 5, 6, 2, 2], 2, [6, 4, 5, 2, 2, 2, 2]),
         ([5, 5, 5, 5, 5, 5, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12], 5,
          [12, 11, 10, 9, 8, 7, 1, 2, 3, 4, 6, 5, 5, 5, 5, 5, 5]),
         ([1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 5, 5, 5, 5, 5, 5], 5,
          [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 5, 5, 5, 5, 5, 5]),
         ([5, 1, 2, 5, 5, 3, 4, 6, 7, 5, 8, 9, 10, 11, 5, 5, 12], 5,
          [12, 1, 2, 11, 10, 3, 4, 6, 7, 9, 8, 5, 5, 5, 5, 5, 5]),
         ]


@pytest.mark.parametrize("array, to_move, answer", tests)
def test_move_element_to_end_list(array, to_move, answer):
    assert move_element_to_end_list(array, to_move) == answer


# @pytest.mark.parametrize("array, to_move, answer", tests)
# def test_move_element_to_end_list_deque(array, to_move, answer):
#     assert move_element_to_end_list_deque(array, to_move) == answer


@pytest.mark.parametrize("array, to_move, answer", tests)
def test_move_element_to_end_original(array, to_move, answer):
    assert move_element_to_end_original(array, to_move) == answer
