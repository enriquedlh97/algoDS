import collections


class Anagram(object):
    """

    """

    def __init__(self, strings=None, anagram_groups=None):
        """

        Args:
        """
        self.strings = strings
        self.anagram_groups = anagram_groups

    def find_anagrams(self, see=True):
        """ Finds groups of anagrams in a set of words using python sorted() and defaultdict(list)

        Using collections.defaultdict(), as opposed to normal dict, it does not raise KeyError,
        instead, it provides a default value for a key that doe snot exists.
        https://www.geeksforgeeks.org/defaultdict-in-python/

        Using list as default_factory in defaultdict() creates a defaultdict with values
        that are a list. This is useful for grouping the strings that are anagrams.
        """
        # Creates a defaultdict with values a list
        self.anagram_groups = collections.defaultdict(list)

        for string in self.strings:
            # sorted(string) returns the sorted string
            # "".join(sorted(string)) adds the sorted string as key
            # Then, the original string is appended as a value
            self.anagram_groups["".join(sorted(string))].append(string)

        # Remove groups of less than 2 strings
        # When implementing as stand-alone function this process should be
        # omitted to improve time complexity and just keep second commented-out return
        for group in self.anagram_groups.copy():
            if len(self.anagram_groups[group]) == 1:
                del self.anagram_groups[group]

        if see:
            return [group for group in self.anagram_groups.values()]
            # return [group for group in self.anagram_groups.values() if len(group) > 1]

    def find_anagrams_csort(self, ):
        """ Finds groups of anagrams in a set of words using custom sort and defaultdict(list)

        """
        pass

    def find_anagrams_chashtable(self, ):
        """ Finds groups of anagrams in a set of words using sorted and custom hashtable
        """
        pass

    def find_anagrams_csort_chashtable(self, ):
        """ Finds groups of anagrams in a set of words using custom sort and custom hashtable

        """
        pass
