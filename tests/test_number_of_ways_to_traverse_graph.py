import os
import sys

import pytest

from algosds.problems.categories.dynamic_programming.number_of_ways_to_traverse_graph import \
    number_of_ways_to_traverse_graph_recursive, number_of_ways_to_traverse_graph_dynamic_programming, \
    number_of_ways_to_traverse_graph_constant_space


myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

tests = [(4, 3, 10),
         (3, 2, 3),
         (2, 3, 3),
         (5, 5, 70),
         (5, 6, 126),
         (7, 5, 210),
         (10, 2, 10),
         (11, 2, 11),
         (5, 9, 495),
         (6, 7, 462),
         (8, 5, 330),
         (2, 2, 2),
         (2, 1, 1),
         (1, 2, 1),
         (3, 3, 6),
         ]


@pytest.mark.parametrize("width, height, answer", tests)
def test_number_of_ways_to_traverse_graph_recursive(width, height, answer):
    assert number_of_ways_to_traverse_graph_recursive(width, height) == answer


@pytest.mark.parametrize("width, height, answer", tests)
def test_number_of_ways_to_traverse_graph_recursive_dynamic_programming(width, height, answer):
    assert number_of_ways_to_traverse_graph_dynamic_programming(width, height) == answer


@pytest.mark.parametrize("width, height, answer", tests)
def test_number_of_ways_to_traverse_graph_constant_space(width, height, answer):
    assert number_of_ways_to_traverse_graph_constant_space(width, height) == answer
