import functools


class HashTable(object):
    """Summary of class here.

    Longer class information....
    Longer class information....

    Attributes:
        MULT: Base value for updating current additive hash code in the
              string_hash() method. Helps provide large range of values.
    """

    def __init__(self):
        self.MULT = 997
        pass

    def string_hash(self, s, modulus):
        """Hashes string

        This hash function is an incremental one. This means that the hash code
        is an additive function of each individual character. Hence, the following
        characteristics:

        1. Examines all characters
        2. Provides large range of values (this avoids collisions)
        3. No one character dominates

        Note:
            1. "ord()" returns integer representing the Unicode character (inverse of "chr()").
            2. "reduce" is equivalent to reduce(function, iterable, initializer=None). Here
                initializer=0

        Args:
            s: String value to be hashed
            modulus: Int value that represents the size og the hash table

            Returns:
                The index of the Hash Table in which the string s should be placed
        """

        return functools.reduce(lambda v, c: (v * self.MULT + ord(c)) % modulus, s, 0)
