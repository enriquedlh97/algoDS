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

    This solution works similar to how breath-first search works.

    First, a queue is initialized for helping to traverse the nodes at each level. AT every level, the left and right
    nodes are immediately swapped.

    For the example

    queue: []

    tree:       1
             /    \
            2      3
          /  \    /  \
         4    5  6    7
       /  \
      8   9


    The initial node is first added to the queue. We get the following.

    queue: [1]

    popped:

    tree:       1
             /    \
            2      3
          /  \    /  \
         4    5  6    7
       /  \
      8   9

    Then, the node is popped and that indicates that something is going to be done with it. In this case, the child
    nodes are swapped. Immediately after that, both child nodes are added to the queue.

    So first the nodes are swapped

    queue: []

    popped: 1

    tree:       1
             /    \
            3      2
          /  \    /  \
         6    7  4    5
               /  \
              8   9

    Then the child nodes are added to the queue.

    queue: [3, 2]

    tree:       1
             /    \
            3      2
          /  \    /  \
         6    7  4    5
               /  \
              8   9

    Then, the next element from the queue is popped and we work on it (in this case the node with value 3).

    queue: [2]

    popped: 3

    tree:       1
             /    \
            3      2
          /  \    /  \
         6    7  4    5
               /  \
              8   9

    We immediately swap the child nodes of the popped node and get the following.

    queue: [2]

    popped: 3

    tree:       1
             /    \
            3      2
          /  \    /  \
         7    6  4    5
               /  \
              8   9

    We then add the child node of this popped node to the queue (in this case the nodes with values 7 and 6).

    queue: [2, 7, 6]

    popped: 3

    tree:       1
             /    \
            3      2
          /  \    /  \
         7    6  4    5
               /  \
              8   9

    We now pop the next element from the queue (node with value 2) and swap its children.

    queue: [7, 6]

    popped: 2

    tree:       1
             /    \
            3      2
          /  \    /  \
         7    6  5    4
                     /  \
                    8   9

    Now we add the children (5 and 4) to the queue.

    queue: [7, 6, 5, 4]

    popped: 2

    tree:       1
             /    \
            3      2
          /  \    /  \
         7    6  5    4
                     /  \
                    8   9

    We now pop the next element form the queue.

    queue: [6, 5, 4]

    popped: 7

    tree:       1
             /    \
            3      2
          /  \    /  \
         7    6  5    4
                     /  \
                    8   9

    In this case we can swap the None children nodes of 7. We add the None children nodes to the queue but we know that
    whenever we reach a None node from the queue we skip them.

    This procedure continues for all nodes and until the queue is empty. When the queue is finally empty it will mean
    that all nodes have been traversed and the tree is inverted.

    The algorithm takes O(n) time because every single node is seen. The operations for swapping nodes and adding to the
    queue (which are performed for every node) are O(1) time operations.

    Similarly, since nodes are being kept track of in the queue, the algorithm takes O(n) space.
    This is because, eventually, all leaf nodes will be in the queue at the same time. Since a (balance) binary tree
    has roughly n/2 leaf nodes, it takes O(n/2) which essentially becomes O(n) space.

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
