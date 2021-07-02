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
    """ My solution using hash table

    :param words: Input array of strings containing potential anagrams
    :return: List of anagram groups in no particular order
    """
    strings_dict = {}

    for string in words:
        sorted_string = "".join(sorted(string))

        if sorted_string in strings_dict:
            strings_dict[sorted_string].append(string)
        else:
            strings_dict[sorted_string] = [string]

    return [anagram_group for anagram_group in strings_dict.values()]


# Time: O(w*n*lg(n) + n*w*lg(w))
# Space: O(w*n)
def group_anagrams_original_brute_force(words):
    """ Original brute force solution

    Because of how this solution is structures, it has to first handle for the case when the input array of words is
    empty.

    This solution works by first arranging in alphabetical order the letters in each word from the input array of words.
    This is done immediately after the array of words is received. It corresponds to the first step.

    To do this, the algorithm iterates over each of the words. Then sorts the letters of each word in alphabetical order
    and appends the sorted word into a new array containing the sorted words. This operation takes O(w) time to loop
    over each word (w is the number of words in the input array) and n*lg(n) time for sorting the letters of each word
    (where n is the length of the longest word). So, the whole operation takes O(w * n * lg(n)) time. Additionally,
    since a new array of sorted words of length w (where w is the number of words in the input array) the operation
    takes O(w) space.

    This operation has the following effect. Assuming an input array

    words: ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]

    The resulting sorted array would be as follows:

    sorted_array: ["oy", "act", "flop", "act", "foo", "act", "oy", "flop"]

    Notice how the order of the words is the same, the only thing that changes is the order in the letters for each
    word.

    The next is to create an array of indices and sort it according to how the previous array of sorted words would be
    if sorted.

    So, the sorted array with its corresponding indices would be as follows.

    sorted_array: ["oy", "act", "flop", "act", "foo", "act", "oy", "flop"]
         indices    0      1       2      3     4       5      6     7

    Now, if the sorted_array was sorted, that is, setting the order of the words within the array in alphabetical order,
    the resulting array, along with the correspond indices would look as follows.

    sorted_array: ["act", "act", "act", "flop", "flop", "foo", "oy", "oy"]
         indices    0      1       2      3     4       5      6     7

    Nevertheless, we do not want to actually sort the sorted_array, that is why the array of indices is created.

    ::param words: Input array of strings containing potential anagrams
    :return: List of anagram groups in no particular order
    """
    if len(words) == 0:
        return []

    # This step loops over each word from the input array of words, sorts the letter alphabetically for each word and
    # then appends each sorted word to a new array of sorted words. Here, sorted(w) returns an array with the letters of
    # the word sorted in alphabetical order.  For example, sorted('hola') -> ['a', 'h', 'l', 'o']. For this reason, and
    # to get back a string, the "".join() method is used to concatenate the characters into a string. So, in this case
    # "".join(sorted('hola')) -> 'ahlo'.
    # This operation takes O(w * n * lg(n)) time and O(w) space
    sorted_words = ["".join(sorted(w)) for w in words]
    # This creates an array of size w (where w is the number of words in the input array) with vales from 0 to w - 1
    indices = [i for i in range(len(words))]
    # This operation sorts the elements in the indices array, corresponding to the positions of the words in the
    # sorted_array, in the same order that they would be in if the actual words that they represent were sorted in
    # alphabetical order.
    # The operation takes O(w * lg(w))
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
    """ Original solution using hash table

    :param words: Input array of strings containing potential anagrams
    :return: List of anagram groups in no particular order
    """
    anagrams = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]

    return list(anagrams.values())
