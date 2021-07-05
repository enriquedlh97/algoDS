

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

    def get_stack(self):
        return self.items


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
            return self.items.pop()
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


class Deque:
    """

    """

    def __init__(self):
        """

        """
        self.items = []

    def append_left(self, item):
        """

        :param item:
        :return:
        """
        self.items.insert(0, item)

    def append_right(self, item):
        """

        :param item:
        :return:
        """
        self.items.append(item)

    def pop_left(self):
        """

        :return:
        """
        return self.items.pop(0)

    def pop_right(self):
        """

        :return:
        """
        return self.items.pop()

    def size(self):
        """

        :return:
        """
        return len(self.items)

    def is_empty(self):
        """

        :return:
        """
        if self.items:
            return False
        else:
            return True

    def peek_front(self):
        """

        :return:
        """
        return self.items[0]

    def peek_back(self):
        """

        :return:
        """
        return self.items[-1]
