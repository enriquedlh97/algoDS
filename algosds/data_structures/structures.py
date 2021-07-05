

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


class Queue:
    """

    """

    def __init__(self):
        """

        """
        self.items = []

    def enqueue(self, item):
        """

        :param item:
        :return:
        """
        self.items.insert(0, item)

    def dequeue(self):
        """

        :return:
        """
        if self.items:
            self.items.pop()
        else:
            return None

    def peek(self):
        """

        :return:
        """
        if self.items:
            return self.items[-1]

    def is_empty(self):
        """
        
        :return:
        """
        if self.items:
            return False
        else:
            return True

    def size(self):
        """

        :return:
        """
        return len(self.items)

