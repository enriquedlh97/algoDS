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


def merge_contact_lists(contacts):
    """ Merges list of objects of type ContactList into a single list

    Returns:

    """
    return list(set(contacts))

