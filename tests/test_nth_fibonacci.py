import os
import sys

import pytest

from algosds.problems.patterns.miscellaneous.dynamic_programming_and_recursion.nth_fibonacci import \
    get_nth_fib_recursive, \
    get_nth_fib_tail_recursive, \
    get_nth_fib_memoization, \
    get_nth_fib_iterative_for_loop, \
    get_nth_fib_iterative_while

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

tests = [(6, 5),
         (1, 0),
         (2, 1),
         (3, 1),
         (4, 2),
         (5, 3),
         (7, 8),
         (8, 13),
         (9, 21),
         (10, 34),
         (11, 55),
         (12, 89),
         (13, 144),
         (14, 233),
         (15, 377),
         (16, 610),
         (17, 987),
         (18, 1597)]


@pytest.mark.parametrize("n, answer", tests)
def test_get_nth_fib_recursive(n, answer):
    assert get_nth_fib_recursive(n) == answer


@pytest.mark.parametrize("n, answer", tests)
def test_get_nth_fib_tail_recursive(n, answer):
    assert get_nth_fib_tail_recursive(n) == answer


@pytest.mark.parametrize("n, answer", tests)
def test_get_nth_fib_memoization(n, answer):
    assert get_nth_fib_memoization(n) == answer


@pytest.mark.parametrize("n, answer", tests)
def test_get_nth_fib_iterative_for_loop(n, answer):
    assert get_nth_fib_iterative_for_loop(n) == answer


@pytest.mark.parametrize("n, answer", tests)
def test_get_nth_fib_iterative_while(n, answer):
    assert get_nth_fib_iterative_while(n) == answer