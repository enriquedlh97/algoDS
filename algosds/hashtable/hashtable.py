import functools


class HashTable(object):
    """

    """

    def __init__(self):
        self.MULT = 997
        pass

    def string_hash(self, s, modulus):
        return functools.reduce(lambda v, c: (v * self.MULT + ord(c)) % modulus, s, 0)
