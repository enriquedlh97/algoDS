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


# Time: O(w*n*lg(n))
# Space: O(w*n)
def group_anagrams_hash_table(words):
    strings_dict = {}

    for string in words:
        sorted_string = "".join(sorted(string))

        if sorted_string in strings_dict:
            strings_dict[sorted_string].append(string)
        else:
            strings_dict[sorted_string] = [string]

    return [anagram_group for anagram_group in strings_dict.values()]


# Time: O(w*n*lg(n))
# Space: O(w*n)
def group_anagrams_original_brute_force(words):
    if len(words) == 0:
        return []

    sorted_words = ["".join(sorted(w)) for w in words]
    indices = [i for i in range(len(words))]
    indices.sort(key=lambda x: sorted_words[x])

    result = []
    current_anagram_group = []
    current_anagram = sorted_words[indices[0]]

    for index in indices:
        word = words[index]
        sorted_word = sorted_words[index]

        if sorted_word == current_anagram:
            current_anagram_group.append(word)
            continue

        result.append(current_anagram_group)
        current_anagram_group = [word]
        current_anagram = sorted_word

    result.append(current_anagram_group)

    return result


# Time: O(w*n*lg(n))
# Space: O(w*n)
def group_anagrams_original_hash_table(words):
    anagrams = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]

    return list(anagrams.values())
