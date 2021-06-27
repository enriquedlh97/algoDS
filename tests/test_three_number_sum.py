import os
import sys

import pytest

from algosds.problems.categories.arrays.three_number_sum import three_number_sum


myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


tests = [([12, 3, 1, 2, -6, 5, -8, 6], 0, [
                                              [-8, 2, 6],
                                              [-8, 3, 5],
                                              [-6, 1, 5]
                                            ]),
         ([1, 2, 3], 6, [[1, 2, 3]]),
         ([1, 2, 3], 7, []),
         ([8, 10, -2, 49, 14], 57, [[-2, 10, 49]]),
         ([12, 3, 1, 2, -6, 5, 0, -8, -1], 0, [
                                                  [-8, 3, 5],
                                                  [-6, 1, 5],
                                                  [-1, 0, 1]
                                                ]),
         ([12, 3, 1, 2, -6, 5, 0, -8, -1, 6], 0, [
                                                      [-8, 2, 6],
                                                      [-8, 3, 5],
                                                      [-6, 0, 6],
                                                      [-6, 1, 5],
                                                      [-1, 0, 1]
                                                    ]),
         ([12, 3, 1, 2, -6, 5, 0, -8, -1, 6, -5], 0, [
                                                          [-8, 2, 6],
                                                          [-8, 3, 5],
                                                          [-6, 0, 6],
                                                          [-6, 1, 5],
                                                          [-5, -1, 6],
                                                          [-5, 0, 5],
                                                          [-5, 2, 3],
                                                          [-1, 0, 1]
                                                        ]),
         ([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 18, [
                                                  [1, 2, 15],
                                                  [1, 8, 9],
                                                  [2, 7, 9],
                                                  [3, 6, 9],
                                                  [3, 7, 8],
                                                  [4, 5, 9],
                                                  [4, 6, 8],
                                                  [5, 6, 7]
                                                ]),
         ([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 32, [[8, 9, 15]]),
         ([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 33, []),
         ([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 5, [])
         ]


@pytest.mark.parametrize("array, target_sum, answer", tests)
def test_three_number_sum(array, target_sum, answer):
    assert three_number_sum(array, target_sum) == answer
