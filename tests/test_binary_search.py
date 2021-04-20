import os
import sys

import pytest

from algosds.problems.categories.searching.binary_search import \
    binary_search_while, \
    binary_search_recursive, \
    binary_search_recursive_original, \
    binary_search_while_original

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

tests = [([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33, 3),
         ([1, 5, 23, 111], 111, 3),
         ([1, 5, 23, 111], 5, 1),
         ([1, 5, 23, 111], 35, -1),
         ([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 0, 0),
         ([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 1, 1),
         ([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 21, 2),
         ([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 45, 4),
         ([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 61, 6),
         ([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 71, 7),
         ([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 72, 8),
         ([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 73, 9),
         ([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 70, -1),
         ([0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355], 355, 10),
         ([0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355], 354, -1),
         ([1, 5, 23, 111], 120, -1),
         ([5, 23, 111], 3, -1)]


@pytest.mark.parametrize("array, target, answer", tests)
def test_binary_search_while(array, target, answer):
    assert binary_search_while(array, target) == answer


@pytest.mark.parametrize("array, target, answer", tests)
def test_binary_search_recursive(array, target, answer):
    assert binary_search_recursive(array, target) == answer


@pytest.mark.parametrize("array, target, answer", tests)
def test_binary_search_recursive_original(array, target, answer):
    assert binary_search_recursive_original(array, target) == answer


@pytest.mark.parametrize("array, target, answer", tests)
def test_binary_search_while_original(array, target, answer):
    assert binary_search_while_original(array, target) == answer
