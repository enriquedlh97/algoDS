

class Stack:
    """

    """

    def __init__(self):
        """
        
        """
        self.items = []

    def push(self, item):
        """

        :param item:
        :return:
        """
        self.items.append(item)

    def pop(self):
        """

        :return:
        """
        self.items.pop()

    def peek(self):
        """

        :return:
        """
        if self.items:
            return self.items[-1]
        else:
            return None

    def size(self):
        """

        :return:
        """
        if self.items:
            return len(self.items)
        else:
            return None

    def is_empty(self):
        """

        :return:
        """
        if self.items:
            return False
        else:
            return True
