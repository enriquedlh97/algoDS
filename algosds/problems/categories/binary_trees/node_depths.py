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
    """ My recursive solution

    This function recursively computes the sum of depths of nodes

    :param root: object of type BinaryTree that correspond to a node of the binary tree
    :return: integer representing the sum of depths of all nodes in the binary tree
    """
    depth_sums = 0
    depth_sums = sum_node_depths(root, depth_sums, 0)
    return depth_sums


def sum_node_depths(node, current_sum, level):
    """ Helper function for my recursive solution

    This function first checks for the base case, which is when a node (object of type BinaryTree) is None. When it is
    None, it means the its parent had no child.

    On each node the sum of depths is updated by adding the value of the current node's depth. Then, the recursive
    function is called for both the right and the left children.

    :param node: object of type BinaryTree that correspond to a node of the binary tree
    :param current_sum: integer representing the current sum of depths of nodes
    :param level: integer representing the current level in the tree for the node at hand
    :return: integer representing the updated current sum of depths of nodes
    """
    # Base case
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
    """ Original recursive solution

    This function is almost the same as my recursive solution. It first checks for the base case, which is when a node
    (object of type BinaryTree) is None. When it is None, it means the its parent had no child.

    If it is not the base case, then the recursive function for both the right and the left children. This has the same
    effect as my recursive function.

    :param root: object of type BinaryTree that correspond to a node of the binary tree
    :param depth:
    :return: integer representing the sum of depths of all nodes in the binary tree
    """
    # Base case
    if root is None:
        return 0

    return depth + node_depths_recursive_original(root.left, depth + 1) + \
           node_depths_recursive_original(root.right, depth + 1)


# Time O(n), where n is the number of vertices (nodes) in the tree
# Space O(h),where h is the height of the tree
def node_depths_while(root):
    """ Original iterative solution using while

    This function has a global variable called sum_of_depths to keep track of the sum of depths of all nodes. It then
    uses a stack to keep track of the visited nodes. The nodes are visited in a depth first search manner.

    The stack used for keeping track of the visited nodes has a dictionary for each node, where the dictionary contains
    the node object of type BinaryTree and the nodes depth. This depth is being updated for children nodes by taking as
    starting point the root nod eof depth 0 and then adding one unit for each level.

    :param root: object of type BinaryTree that correspond to a node of the binary tree
    :return: integer representing the sum of depths of all nodes in the binary tree
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
