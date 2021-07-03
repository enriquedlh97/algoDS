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


# Time: O(w*n*lg(n)) time, where w is the number of words and n the length of the longest word
# Space: O(w*n) space
def group_anagrams_hash_table(words):
    """ My solution using hash table

    This solutions works by iteration over all words in the input array and, for each of them, sorting the letters
    (generating an anagram), and check if it already exists in a hash table. If it does nto exists, then we added with
    the anagram as key and the actual string as value. If is is already in the hash table we then just appended it.

    The reason for the O(w*n*lg(n)) time is the same one explained in the solution below.

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


# Time: O(w*n*lg(n) + n*w*lg(w)) time, where w is the number of words and n the length of the longest word
# Space: O(w*n) space
def group_anagrams_original_brute_force(words):
    """ Original brute force solution

    Because of how this solution is structured, it has to first handle for the case when the input array of words is
    empty.

    Then, this solution works by first arranging in alphabetical order the letters in each word from the input array of
    words. This is done immediately after the array of words is received.

    To do this, the algorithm iterates over each of the words. Then, it sorts the letters of each word in alphabetical
    order and appends the sorted word into a new array containing the sorted words. This operation takes O(w) time to
    loop over each word (w is the number of words in the input array) and O(n*lg(n)) time for sorting the letters of
    each word (where n is the length of the longest word). So, the whole operation takes O(w * n * lg(n)) time.
    Additionally, since a new array of sorted words of length w (where w is the number of words in the input array) is
    created, the operation takes O(w * n) space. The n is because it corresponds to the length of the longest word.

    This operation has the following effect. Assuming an input array

    words: ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]

    The resulting sorted array would be as follows:

    sorted_array: ["oy", "act", "flop", "act", "foo", "act", "oy", "flop"]

    Notice how the order of the words is the same, the only thing that changes is the order of the letters for each
    word.

    The next step is to create an array of indices and sort it according to how the previous array of sorted words would
    be if sorted with respect to the words.

    So, the sorted array with its corresponding indices would be as follows.

    sorted_array: ["oy", "act", "flop", "act", "act", "oy", "flop"]
         indices    0      1       2      3     4       5      6

    Now, if the sorted_array was sorted, that is, setting the order of the words within the array in alphabetical order,
    the resulting array, along with the correspond indices would look as follows.

    sorted_array: ["act", "act", "act", "flop", "flop", "oy", "oy"]
         indices    1      3       4      2       6      0      5

    Nevertheless, we do not want to actually sort the sorted_array, that is why the array of indices is created.

    This operation of sorting the array of indices according to how the sorted_Array would end up if sorted takes
    O( n * w * lg(w) ) time. Sorting the array of indices takes O( w * lg(w) ) time because there are w indices in the
    array. The n in O( n * w * lg(w) ) comes from the fact that we are dealing with strings. So, the operation is
    essentially sorting an array of strings and not an array of integers. If the operation was to sort an array of
    integers it would take only O( w * lg(w) ), because for w indices we perform at most w comparisons. Nevertheless, in
    the case of strings, in order to compare two strings, in the worst case, all of the characters of the strings have
    to be compared, and this would yield an O(n) time operation, where n is the length of the longest word.

    Essentially, this operation of comparing two strings is equivalent to comparing two arrays.

    In summary, the operation involves sorting the w elements, which takes O(w * lg(w)) time and for each element, for
    each of the O( w * lg(w) ) comparisons, we have to compare each character of the string, this comparison takes O(n)
    time. This means that the whole operation takes O( n * w * lg(w) ) time.

    To read more on sorting strings, string comparisons and the reason for the time complexity in this operation see the
    following links:

    https://stackoverflow.com/a/57062358/15542477
    https://stackoverflow.com/questions/34318489/is-it-true-that-sorting-strings-is-on2logn/34318565
    https://cs.stackexchange.com/questions/127899/what-is-the-expected-time-complexity-of-checking-equality-of-two-arbitrary-strin

    As a whole, the algorithm ends up taking O(w*n*lg(n) + n*w*lg(w)) time, where w is the number of words and n the
    length of the longest word

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
    # This operation takes O(w * n * lg(n)) time and O(w * n) space
    sorted_words = ["".join(sorted(w)) for w in words]
    # This creates an array of size w (where w is the number of words in the input array) with vales from 0 to w - 1
    indices = [i for i in range(len(words))]
    # This operation sorts the elements in the indices array, corresponding to the positions of the words in the
    # sorted_array, in the same order that they would be in if the actual words that they represent were sorted in
    # alphabetical order.
    # The operation takes O(n * w * lg(w))
    # The key value is to sort the elements according to the string that the index represents in the sorted array.
    #
    # The value of the key parameter should be a function (or other callable) that takes a single argument and returns a
    # key to use for sorting purposes. This technique is fast because the key function is called exactly once for each
    # input record.
    # A common pattern is to sort complex objects using some of the object’s indices as keys. For example:
    # For example,
    # >>> student_tuples = [
    # ...    ('john', 'A', 15),
    # ...    ('jane', 'B', 12),
    # ...    ('dave', 'B', 10),
    # ...]
    # >>> sorted(student_tuples, key=lambda student: student[2])   # sort by age
    # [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
    # For more details ont his, see https://docs.python.org/3/howto/sorting.html#key-functions
    indices.sort(key=lambda x: sorted_words[x])
    # For details on lambda use see https://www.w3schools.com/python/python_lambda.asp
    # lambda x: sorted_words[x] is equivalent to writing
    # x = lambda x: sorted_words[x] and the x function is called as x(0) which is equivalent to sorted_words[0]

    result = []
    current_anagram_group = []
    current_anagram = sorted_words[indices[0]]

    for index in indices:
        word = words[index]
        sorted_word = sorted_words[index]

        # This operation of comparing two strings takes O(n) time.
        if sorted_word == current_anagram:
            current_anagram_group.append(word)
            continue

        result.append(current_anagram_group)
        current_anagram_group = [word]
        current_anagram = sorted_word

    result.append(current_anagram_group)

    return result


# Time: O(w*n*lg(n)) time, where w is the number of words and n the length of the longest word.
# Space: O(w*n) space
def group_anagrams_original_hash_table(words):
    """ Original solution using hash table

    This solution works exactly the same as my hash table solution. The implementation is just a little different.

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
