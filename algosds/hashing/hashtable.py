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
