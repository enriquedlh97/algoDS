import os
import sys

import pytest

from algosds.problems.categories.searching.find_three_largest_numbers import \
    find_three_largest_numbers_deque_swap, \
    find_three_largest_numbers_elif, \
    find_three_largest_numbers_original

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


tests = [([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7], [18, 141, 541]),
         ([55, 7, 8], [7, 8, 55]),
         ([55, 43, 11, 3, -3, 10], [11, 43, 55]),
         ([7, 8, 3, 11, 43, 55], [11, 43, 55]),
         ([55, 7, 8, 3, 43, 11], [11, 43, 55]),
         ([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7], [7, 7, 7]),
         ([7, 7, 7, 7, 7, 7, 8, 7, 7, 7, 7], [7, 7, 8]),
         ([-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7], [-2, -1, 7])]


#  @pytest.mark.skip()
@pytest.mark.parametrize("array, answer", tests)
def test_find_three_largest_numbers_elif(array, answer):
    assert find_three_largest_numbers_elif(array) == answer


#  @pytest.mark.skip()
@pytest.mark.parametrize("array, answer", tests)
def test_find_three_largest_numbers_original(array, answer):
    assert find_three_largest_numbers_original(array) == answer


#  @pytest.mark.skip()
@pytest.mark.parametrize("array, answer", tests)
def test_find_three_largest_numbers_deque_swap(array, answer):
    assert find_three_largest_numbers_deque_swap(array) == answer
