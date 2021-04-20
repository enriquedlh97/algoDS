import os
import sys

import pytest

from algosds.problems.categories.strings.generate_document import \
    generate_document_multiple_counts, \
    generate_document_single_counts, \
    generate_document_sorting, \
    generate_document_hashtable, \
    generate_document_hashtable_original

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


tests = [("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!", True),
         ("A", "a", False),
         ("a", "a", True),
         ("a hsgalhsa sanbjksbdkjba kjx", "", True),
         (" ", "hello", False),
         ("     ", "     ", True),
         ("aheaollabbhb", "hello", True),
         ("aheaolabbhb", "hello", False),
         ("estssa", "testing", False),
         ("Bste!hetsi ogEAxpert", "AlgoExpert is the Best!", False),
         ("helloworld ", "hello wOrld", False),
         ("helloworldO", "hello wOrld", False),
         ("helloworldO ", "hello wOrld", True),
         ("&*&you^a%^&8766 _=-09     docanCMakemthisdocument", "Can you make this document &", True),
         ("abcabcabcacbcdaabc", "bacaccadac", True)]


@pytest.mark.parametrize("characters, document, answer", tests)
def test_generate_document_multiple_counts(characters, document, answer):
    assert generate_document_multiple_counts(characters, document) == answer


@pytest.mark.parametrize("characters, document, answer", tests)
def test_generate_document_single_counts(characters, document, answer):
    assert generate_document_single_counts(characters, document) == answer


@pytest.mark.parametrize("characters, document, answer", tests)
def test_generate_document_sorting(characters, document, answer):
    assert generate_document_sorting(characters, document) == answer


@pytest.mark.parametrize("characters, document, answer", tests)
def test_generate_document_hashtable(characters, document, answer):
    assert generate_document_hashtable(characters, document) == answer


@pytest.mark.parametrize("characters, document, answer", tests)
def test_generate_document_hashtable_original(characters, document, answer):
    assert generate_document_hashtable_original(characters, document) == answer
