"""
Problem:

Write a function that takes in a Binary Search Tree (BST) and a target integer value and returns the closest value to
that target value contained in the BST.

You can assume that there will only be one closest value.

Each BST node has an integer value, a left child node, and a right child node. A node is said to be a valid BST node if
and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its
value is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes
themselves or None / null.

Input:
    graph:     10
             /    \
            5      15
          /  \    /  \
         2    5  13   22
       /          \
      1           14

      target: 12

Output:
    13

"""


# This is the class of the input tree.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Time O(h) average case, where h is the the height of the tree which is h = lg(n) where n is the
#			number of node sin the tree, hence average case is O(lg(n)). The worst case is O(n),
#			when the tree is skewed and has, for example, only left sides (single chain)
# Space O(h), where h is the height of the tree and is the same as h = O(lg(n)). In the worst case
# 			the space is O(n) fr the same reason as in the time complexity
def find_closest_value_in_bst_recursive(tree, target, value=float('inf'), diff=float('inf')):
    #  Base case
    if tree is None:
        return value
    elif target == tree.value:
        return tree.value
    elif target < tree.value:
        value, diff = abs_diff(target, tree, value, diff)
        return find_closest_value_in_bst_recursive(tree.left, target, value, diff)
    elif target > tree.value:
        value, diff = abs_diff(target, tree, value, diff)
        return find_closest_value_in_bst_recursive(tree.right, target, value, diff)


def abs_diff(target, tree, value, diff):
    if abs(target - tree.value) < diff:
        value = tree.value
        diff = abs(target - tree.value)

    return value, diff


# Time O(h) average case, where h is the the height of the tree which is h = lg(n) where n is the
#			number of node sin the tree, hence average case is O(lg(n)). The worst case is O(n),
#			when the tree is skewed and has, for example, only left sides (single chain)
# Space O(h), where h is the height of the tree and is the same as h = O(lg(n)). In the worst case
# 			the space is O(n) fr the same reason as in the time complexity
def find_closest_value_in_bst_recursive_clean(tree, target):
    closest_value = {'value': None, 'diff': float('inf')}
    # print(closest_value)
    closest_value = get_value(tree, target, closest_value)
    # print(closest_value)
    return closest_value['value']


def get_value(tree, target, closest_value):
    #  Base case
    if tree is None:
        return closest_value
    else:
        closest_value = update_closest(closest_value, target, tree)

    if target <= tree.value:
        return get_value(tree.left, target, closest_value)

    elif target >= tree.value:
        return get_value(tree.right, target, closest_value)


# Time O(h) average case, where h is the the height of the tree which is h = lg(n) where n is the
#			number of node sin the tree, hence average case is O(lg(n)). The worst case is O(n),
#			when the tree is skewed and has, for example, only left sides (single chain)
# Space O(1)
def find_closest_value_in_bst_iterative(tree, target):
    closest_value = {'value': None, 'diff': float('inf')}

    while tree is not None:

        closest_value = update_closest(closest_value, target, tree)

        if target >= tree.value:
            tree = tree.right

        elif target <= tree.value:
            tree = tree.left

    return closest_value['value']


# Time O(h) average case, where h is the the height of the tree which is h = lg(n) where n is the
#			number of node sin the tree, hence average case is O(lg(n)). The worst case is O(n),
#			when the tree is skewed and has, for example, only left sides (single chain)
# Space O(1)
def find_closest_value_in_bst_iterative_clean(tree, target):
    closest_value = {'value': None, 'diff': float('inf')}

    while tree is not None:

        closest_value = update_closest(closest_value, target, tree)

        if closest_value['diff'] == 0:
            return closest_value['value']

        elif target > tree.value:
            tree = tree.right

        elif target < tree.value:
            tree = tree.left

    return closest_value['value']


def update_closest(closest_value, target, tree):
    """ Helper function to update closest value to target for get_value() in recursive clean and iterative solutions

    :param closest_value:
    :param target:
    :param tree:
    :return:
    """
    if abs(tree.value - target) < closest_value['diff']:
        closest_value['value'] = tree.value
        closest_value['diff'] = abs(tree.value - target)

    return closest_value


# Time O(h) average case, where h is the the height of the tree which is h = lg(n) where n is the
#			number of node sin the tree, hence average case is O(lg(n)). The worst case is O(n),
#			when the tree is skewed and has, for example, only left sides (single chain)
# Space O(h), where h is the height of the tree and is the same as h = O(lg(n)). In the worst case
# 			the space is O(n) fr the same reason as in the time complexity
def find_closest_value_in_bst_recursive_original(tree, target):
    return find_closest_value_recursive_original_helper(tree, target, tree.value)


def find_closest_value_recursive_original_helper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return find_closest_value_recursive_original_helper(tree.left, target, closest)
    elif target > tree.value:
        return find_closest_value_recursive_original_helper(tree.right, target, closest)
    else:
        return closest


def find_closest_value_in_bst_iterative_original(tree, target):
    return find_closest_value_recursive_original_helper(tree, target, tree.value)


def find_closest_value_iterative_original_helper(tree, target, closest):
    current_node = tree

    while current_node is not None:
        if abs(target - closest) > abs(target - current_node.value):
            closest = current_node.value

        if target < current_node.value:
            current_node = current_node.left

        elif target > current_node.value:
            current_node = current_node.right

        else:
            break

        return closest
