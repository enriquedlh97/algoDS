import os
import sys

import pytest

from algosds.problems.categories.recursion.staircase_traversal import \
    staircase_traversal_dynamic_programming_suboptimal, staircase_traversal_dynamic_programming_optimal, \
    staircase_traversal_recursive_original, staircase_traversal_recursive_original_optimal, \
    staircase_traversal_dynamic_programming_original_suboptimal, \
    staircase_traversal_dynamic_programming_original_optimal


myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

tests = [(4, 2, 5),
         (10, 1, 1),
         (10, 2, 89),
         (4, 3, 7),
         (1, 1, 1),
         (5, 2, 8),
         (4, 4, 8),
         (6, 2, 13),
         (100, 1, 1),
         (15, 5, 13624),
         (7, 2, 21),
         (6, 3, 24),
         (3, 2, 3),
         ]


@pytest.mark.parametrize("height, max_steps, answer", tests)
def test_staircase_traversal_dynamic_programming_suboptimal(height, max_steps, answer):
    assert staircase_traversal_dynamic_programming_suboptimal(height, max_steps) == answer


@pytest.mark.parametrize("height, max_steps, answer", tests)
def test_staircase_traversal_dynamic_programming_optimal(height, max_steps, answer):
    assert staircase_traversal_dynamic_programming_optimal(height, max_steps) == answer


@pytest.mark.parametrize("height, max_steps, answer", tests)
def test_staircase_traversal_recursive_original(height, max_steps, answer):
    assert staircase_traversal_recursive_original(height, max_steps) == answer


@pytest.mark.parametrize("height, max_steps, answer", tests)
def test_staircase_traversal_recursive_original_optimal(height, max_steps, answer):
    assert staircase_traversal_recursive_original_optimal(height, max_steps) == answer


@pytest.mark.parametrize("height, max_steps, answer", tests)
def test_staircase_traversal_dynamic_programming_original_suboptimal(height, max_steps, answer):
    assert staircase_traversal_dynamic_programming_original_suboptimal(height, max_steps) == answer


@pytest.mark.parametrize("height, max_steps, answer", tests)
def test_staircase_traversal_dynamic_programming_original_optimal(height, max_steps, answer):
    assert staircase_traversal_dynamic_programming_original_optimal(height, max_steps) == answer
