"""
Problem:

    Write a function that takes in a Binary Tree and inverts it. In other words, the function should swap every left
    node in the the tree for its corresponding right node.

    Each BinaryTree node has an integer value, a left child node,and a right child node. Children nodes can be either
    BinaryTree nodes themselves or None / null.

Input:

    tree =       1
             /    \
            2      3
          /  \    /  \
         4    5  6    7
       /  \
      8   9


Output:

                 1
             /    \
            3      2
          /  \    /  \
         7    6  5    4
                     /  \
                    9   8


"""


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Time: O(n) time, where n is the number of nodes in the tree
# Space: O(d) = O(lg(n)) space,  where d = lg(n) is the depth of the tree
def invert_binary_tree(tree):
    """ My recursive solution

    :param tree: BinaryTree object
    :return: input BinaryTree object inverted
    """
    if tree is None:
        return
    else:
        # Swap children
        tree.left, tree.right = tree.right, tree.left
        # Recursive calls on children
        invert_binary_tree(tree.left)
        invert_binary_tree(tree.right)


# Time: O(n) time, where n is the number of nodes in the tree
# Space: O(n) space
def invert_binary_tree_original_iterative(tree):
    """ Original iterative solution

    :param tree: BinaryTree object
    :return: input BinaryTree object inverted
    """
    queue = [tree]
    while len(queue):
        current = queue.pop(0)
        if current is None:
            continue
        swap_left_and_right(current)
        queue.append(current.left)
        queue.append(current.right)


# Time: O(n) time, where n is the number of nodes in the tree
# Space: O(d) = O(lg(n)) space,  where d = lg(n) is the depth of the tree
def invert_binary_tree_original_recursive(tree):
    """ Original recursive solution

    :param tree: BinaryTree object
    :return: input BinaryTree object inverted
    """
    if tree is None:
        return
    swap_left_and_right(tree)
    invert_binary_tree_original_recursive(tree.left)
    invert_binary_tree_original_recursive(tree.right)


def swap_left_and_right(tree):
    """ Helper function for original iterative and recursive solutions. Swaps nodes.

    :param tree: BinaryTree object
    :return: input BinaryTree object inverted
    """
    tree.left, tree.right = tree.right, tree.left
