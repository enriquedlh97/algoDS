"""
Problem:

You are given the head of a Singly Linked List whose nodes are in sorted ascending order with respect to their values.
Write a function that returns a modified version of the Linked List that does not contain any nodes with duplicate
values. The Linked List should be modified in place (ie do nto create a brand new list), and the modified Linked List
should still have its nodes sorted in ascending order with respect to their values.

Each Linked List node has an integer value as well as a next node pointing to the next node in the list or to None if it
 is the tail of the list.

Input:
    Linked List: 1 -> 1 -> 3 -> 4 -> 4 -> 4 -> 5 -> 6 -> 6

Output:
    Linked List: 1 -> 3 -> 4 -> 5 -> 6
"""


# This is an input class.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Time O(n)
# Space O(1)
def remove_duplicates_from_linked_list_single_while(linked_list):
    current_node = linked_list

    while current_node.next is not None:

        if current_node.value == current_node.next.value:
            current_node.next = current_node.next.next
        else:
            current_node = current_node.next

    return linked_list


def remove_duplicates_from_linked_list_two_whiles(linked_list):
    current_node = linked_list

    while current_node is not None:
        next_distinct_node = current_node.next

        while next_distinct_node is not None and next_distinct_node.value == current_node.value:
            next_distinct_node = next_distinct_node.next

        current_node.next = next_distinct_node
        current_node = next_distinct_node

    return linked_list
