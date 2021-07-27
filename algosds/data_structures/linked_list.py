# @TODO Finish LinkedList implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        pass


if __name__ == "__main__":
    linked_list = LinkedList
    linked_list.append('A')
    linked_list.append('B')
