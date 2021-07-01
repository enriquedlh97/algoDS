"""
Problem:

Write a function that takes in an array of strings and groups anagrams together.

Anagrams are strings made up of exactly the same letters, where order doesn't matter. For example, "cinema"
and "iceman" are anagrams; similarly, "foo" and "ofo" are anagrams.

Your function should return a list of anagram groups in no particular order.

Input:

    array: ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]

Output:

    [
      ["yo", "oy"],
      ["act", "tac", "cat"],
      ["flop", "olfp"],
      ["foo"]
    ]

"""


# Time O(n^2), where n is the length of the input array
# Space O(1)