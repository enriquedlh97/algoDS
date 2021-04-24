"""
Problem:

Write a function that takes in a Binary Tree and returns a list of its branch sums ordered from leftmost branch sum to
rightmost branch sum.

A branch sum is the sum of all values in a Binary Tree branch. A Binary Tree branch is a path of nodes in a tree that
starts at the root node and ends at any leaf node.

Each Binary Tree node has an integer value, a left child node and a right child node. Children nodes can either be
Binary Tree nodes themselves or None / null .

Input:
    graph:      1
             /    \
            2      3
          /  \    /  \
         4    5  6    7
       /  \  /
      8   9 10
Output:
    [15, 16, 18, 10, 11]

    gotten as
    15 = 1 + 2 + 4 + 8
    16 = 1 + 2 + 4 + 9
    18 = 1 + 2 + 5 + 10
    10 = 1 + 3 + 6
    11 = 1 + 3 + 7

"""


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# My solution
# Time O(v), where v is the number of vertices (nodes) in the tree
# Space O(v)
def branch_sums(root):
    """ My solution, recursive

    :param root: object of type BinaryTree representing the root node of the binary tree
    :return: array containing the sums of each branch in the binary tree
    """
    branch_sum_array = []

    compute_branch_sums(root, 0, branch_sum_array)

    return branch_sum_array


def compute_branch_sums(root, branch_sum, branch_sum_array):
    """
    
    :param root:
    :param branch_sum:
    :param branch_sum_array:
    :return:
    """
    branch_sum += root.value

    if root.left:
        compute_branch_sums(root.left, branch_sum, branch_sum_array)

    if root.right:
        compute_branch_sums(root.right, branch_sum, branch_sum_array)

    if not root.left and not root.right:
        branch_sum_array.append(branch_sum)

    return branch_sum_array


# Original solution
# Time O(v), where v is the number of vertices (nodes) in the tree
# Space O(v)
def branch_sums_original(root):
    """ Original solution, recursive

    :param root: object of type BinaryTree representing the root node of the binary tree
    :return: array containing the sums of each branch in the binary tree
    """
    sums = []
    calculate_branch_sums(root, 0, sums)
    return sums


def calculate_branch_sums(node, running_sum, sums):
    """

    :param node:
    :param running_sum:
    :param sums:
    :return:
    """
    if node is None:
        return

    new_running_sum = running_sum + node.value

    if node.left is None and node.right is None:
        sums.append(new_running_sum)
        return

    calculate_branch_sums(node.left, new_running_sum, sums)
    calculate_branch_sums(node.left, new_running_sum, sums)
