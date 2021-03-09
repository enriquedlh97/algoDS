import functools


class HashTable(object):
    """Summary of class here.

    Longer class information....
    Longer class information....

    Attributes:
        MULT: Base value for updating current additive hash code in the
              string_hash() method. Helps provide large range of values.
              Important to try to choose prime numbers that are not close
              to powers of 2. "See string_hash" documentation for links to
              explanations of this.
    """

    def __init__(self):
        self.MULT = 997

    def string_hash(self, s, modulus):
        """Hashes string using polynomial rolling hash function.

        This hash function is an incremental one. This means that the hash code
        is an additive function of each individual character. Hence, the following
        characteristics:

        Time complexity: O(n) where n is the size of the string
        Space complexity: O(1)

        1. Examines all characters
        2. Provides large range of values (this avoids collisions)
        3. No one character dominates

        Explanation of this function: https://iq.opengenus.org/string-hashing/#:~:text=One%20of%20the%20most%20common,O(1)%20time%20complexity.

        Note:
            1. "ord()" returns integer representing the Unicode character (inverse of "chr()").
            2. "reduce" is equivalent to reduce(function, iterable, initializer=None). Here
                initializer=0

        Why choose prime numbers that are not close to powers of 2 for the size of the
        hash table when using division method for hashing:
            - https://cs.stackexchange.com/questions/19020/why-should-one-not-use-a-2p-size-hash-table-when-using-the-division-method-as-a/19021#19021
            - https://stackoverflow.com/questions/5929878/why-is-the-size-127-prime-better-than-128-for-a-hash-table
            - https://cs.stackexchange.com/questions/86237/hash-size-are-prime-numbers-near-powers-of-two-a-poor-choice-for-the-modulus/86345#86345
            - https://cs.stackexchange.com/questions/19020/why-should-one-not-use-a-2p-size-hash-table-when-using-the-division-method-as-a#:~:text=An%20uniform%20hash%20function%20is,and%20many%20collisions%20will%20ensue.

        Args:
            s: String value to be hashed
            modulus: Int value that represents the size og the hash table

            Returns:
                The index of the Hash Table in which the string s should be placed
        """

        return functools.reduce(lambda v, c: (v * self.MULT + ord(c)) % modulus, s, 0)


class ContactList:
    """ Class to represent contacts

    Taken from "Elements of programming interviews in python" page 161.
    This class represents contacts where each contact is a string.
    Characteristics:
    1. Individual contacts are stored in a list.
    2. There could be duplicate contacts.
    3. Two contacts are equal if they contain the same set of strings
        regardless of ordering of the string in an underlying list.
    4. Multiple repetitions of the same contact is the same as a single
        instance of the contact.

    Equality: Defined by forming sets from the lists and comparing them
        (needed to store contacts in hash table).
        This means the following:
        - Hash function depends on the strings present but not their ordering.
        - Hash function considers only one copy if their are duplicates.

    Note: The implemented hash function and equals method are very inefficient.
         In practice, it would be advisable to cache the underlying set and the
         hash code, remembering to void these values on updates.

    Attributes:
        names: list containing the set of names

    """

    def __init__(self, names):
        """

        Args:
             names: list of strings
        """
        self.names = names

    def __hash__(self):
        """ Hashes set of names

        hash(): Returns the hash value of object if it has one.
            https://www.programiz.com/python-programming/methods/built-in/hash
        frozenset(): returns immutable frozenset object initialized with elements from
            the given iterable.
            https://www.programiz.com/python-programming/methods/built-in/frozenset

        Args:

        Returns:

        """
        # frozenset() is required since set type is mutable and we require
        # an immutable key value to be able to hash
        return hash(frozenset(self.names))

    def __eq__(self, other):
        """

        Args:
            other:

        Returns:

        """
        return set(self.names) == set(other.names)

    def merge_contact_lists(self):
        pass
