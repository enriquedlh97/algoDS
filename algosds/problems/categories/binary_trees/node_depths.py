"""
Problem:

The distance between a node in a Binary Tree and the tree's root is called the node's depth.

Write a function that takes in a Binary Tree and returns the sum of its node's depths.

Each BinaryTree node has an integer value, a left child node, anda right child node. Children nodes can either be
BinaryTree nodes themselves or None / null.

Input:
    graph:      1
             /    \
            2      3
          /  \    /  \
         4    5  6    7
       /  \
      8   9
Output:
    16

    gotten as

    Depth of node with value 2 is 1.
    Depth of node with value 3 is 1.
    Depth of node with value 4 is 2.
    Depth of node with value 5 is 2.
    Etc...
    Summing all of these depths yields 16

"""


#  This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# ****** My solution ******
# Time O(n), where n is the number of vertices (nodes) in the tree
# Space O(h),where h is the height of the tree
def node_depths_recursive(root):
    """

    :param root:
    :return:
    """
    depth_sums = 0
    depth_sums = sum_node_depths(root, depth_sums, 0)
    return depth_sums


def sum_node_depths(node, current_sum, level):
    """

    :param node:
    :param current_sum:
    :param level:
    :return:
    """
    if node is None:
        return current_sum

    current_sum += level
    current_sum = sum_node_depths(node.left, current_sum, level + 1)
    current_sum = sum_node_depths(node.right, current_sum, level + 1)

    return current_sum


# ****** End of my solution ******


# Time O(n), where n is the number of vertices (nodes) in the tree
# Space O(h),where h is the height of the tree
def node_depths_recursive_original(root, depth=0):
    """

    :param root:
    :param depth:
    :return:
    """
    if root is None:
        return 0

    return depth + node_depths_recursive_original(root.left, depth + 1) + \
           node_depths_recursive_original(root.right, depth + 1)


# Time O(n), where n is the number of vertices (nodes) in the tree
# Space O(h),where h is the height of the tree
def node_depths_while(root):
    """
    
    :param root:
    :return:
    """
    sum_of_depths = 0
    stack = [{"node": root, "depth": 0}]

    while len(stack) > 0:
        node_info = stack.pop()
        node, depth = node_info["node"], node_info["depth"]

        if node is None:
            continue

        sum_of_depths += depth
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})

    return sum_of_depths
