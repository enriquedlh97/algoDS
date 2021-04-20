import os
import sys

import pytest

from algosds.problems.categories.strings.palindrome_check import \
    is_palindrome_reversed_string_for_loop, \
    is_palindrome_reversed_string_join, \
    is_palindrome_recursion, \
    is_palindrome_tail_recursion, \
    is_palindrome_two_pointers_explicit, \
    is_palindrome_two_pointers_implicit, \
    is_palindrome_two_pointers_implicit_pythonic

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


tests = [("abcdcba", True),
         ("a", True),
         ("ab", False),
         ("aba", True),
         ("abb", False),
         ("abba", True),
         ("abcdefghhgfedcba", True),
         ("abcdefghihgfedcba", True),
         ("abcdefghihgfeddcba", False)]


@pytest.mark.parametrize("string, answer", tests)
def test_is_palindrome_reversed_string_for_loop(string, answer):
    assert is_palindrome_reversed_string_for_loop(string) == answer


@pytest.mark.parametrize("string, answer", tests)
def test_is_palindrome_reversed_string_join(string, answer):
    assert is_palindrome_reversed_string_join(string) == answer


@pytest.mark.parametrize("string, answer", tests)
def test_is_palindrome_recursion(string, answer):
    assert is_palindrome_recursion(string) == answer


@pytest.mark.parametrize("string, answer", tests)
def test_is_palindrome_tail_recursion(string, answer):
    assert is_palindrome_tail_recursion(string) == answer


@pytest.mark.parametrize("string, answer", tests)
def test_is_palindrome_two_pointers_explicit(string, answer):
    assert is_palindrome_two_pointers_explicit(string) == answer


@pytest.mark.parametrize("string, answer", tests)
def test_is_palindrome_two_pointers_implicit(string, answer):
    assert is_palindrome_two_pointers_implicit(string) == answer


@pytest.mark.parametrize("string, answer", tests)
def test_is_palindrome_two_pointers_implicit_pythonic(string, answer):
    assert is_palindrome_two_pointers_implicit_pythonic(string) == answer
