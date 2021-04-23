"""
Problem:

You're given a Node class that has a name and an array of optional children nodes. When put together, nodes form an
acyclic tree-like structure.

Implement the depthFirstSearch method on the Node class, which takes in an empty array, traverses the tree using the
Depth-first Search approach (specifically navigating the tree from left to right), stores all of the nodes' names in
the input array, and returns it.

Input:
    graph:      A
            /   |   \
           B    C     D
         /  \        / \
        E    F      G   H
            / \      \
           I   J      K
Output:
    ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]

"""


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def add_child(self, name):
        self.children.append(Node(name))
        return self

        # Time O(v + e), where v is the number of vertices (nodes) and e is the number of edges (connecting lines)
        # Space O(v)
    def depth_first_search(self, array):
        """ This is my solution, which is the same as the original one

        The graphs used for this problem are interpreted as directed graphs.

        The time complexity is O(v + e). The O(v) part is gotten because all nodes/vertices in the graph are traversed
        once. The O(e) corresponds to the cost of the for loop, since at every node we call the depth_first_search()
        function for each of the children of the node. For instance, in the case of node C, since it has no children
        e=0.

        The space complexity is O(v) because in the worse case scenario, which is when we have a single branch, which
        for the example problem would be something like this:

        A-B-C-D-E-F-G-H-I-J-K

        So first, the depth_first_search() function is run for node A and before the function is resolved, the function
        is called for node B, and before it gets resolved for node B, the function is called for node C, and it
        continuous like this, which means that the function call for node A is not going to be resolved until the
        function call for all other nodes are resolved. or this reason, the callstack is going to be of the same size as
        nodes/vertices in the graph for the worst case.

        :param array: Contains the names of the nodes from the graph in order gotten by traversing in a depth-first
                      search manner
        :return: returns the array with all the nodes names.
        """
        array.append(self.name)

        for child in self.children:
            child.depthFirstSearch(array)

        return array
