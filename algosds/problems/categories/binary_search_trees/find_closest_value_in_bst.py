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
# number of nodes in the tree, hence average case is O(lg(n)). The worst case is O(n),
# when the tree is skewed and has, for example, only left sides (single chain)

# Space O(h), where h is the height of the tree and is the same as h = O(lg(n)). In the worst case
# the space is O(n) for the same reason as in the time complexity
def find_closest_value_in_bst_recursive(tree, target, value=float('inf'), diff=float('inf')):
    """ My recursive solution

    This solution keeps track of the closest value to the target and its difference.

    This solution works by everytime performing 3 checks. First it checks if the target is equal to the current node,
    this is to improve performance but it does not really affect the complexity of the algorithm. When it is, it return
    the value of the current node. The second and third checks are if the target is less than te current node or bigger
    than the current node. In either case, first the closest value and difference are updated, this is to see if the
    current node should be the new closest value. This is computed by taking the difference of current node and target
    comparing it to the difference of the previous closest value.

    After this has been done, the function is called again recursively and passes the left child or right child
    depending on if the target was smaller or bigger than the current node.

    The algorithm ends when the current node is None or when the target has the same value as the current node. This
    last second check is not necessary and does not affect the overall complexity but it does yield more efficiency.

    The worst case time complexity if O(log(n)), where n is the number of node sin the tree, this would be when the tree
    has only one branch. The average case time complexity is O(h) where h is the height of the tree given by lg(n), so
    essentially, the average case is O(lg(n)). This is because, at most, only one node at each level is going to be
    visited and, roughly half of the nodes are discarded on every step.

    The space complexity would be the same for both the average case and the worst case. This is because there are going
    to be at most one function call in the call stack for every level in the tree.

    :param tree: object of type BST representing a binary tree
    :param target: integer representing the target value to be searched for in the nodes of the bst
    :param value: integer representing the value of the current closest node to the target
    :param diff: integer representing the difference between the closest node to the target an the target itself
    :return: integer value corresponding to the closest node value to the target
    """
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
    """ Helper function for my recursive solution

    This function is for updating the current closest value to the target. To do this it computes the difference between
    the current tree value and the target and compares it to the difference between the current closest value to the
    target and the target itself. The value corresponding to the smallest difference is kept as the new closest value to
    the target.

    :param tree: object of type BST representing a binary tree
    :param target: integer representing the target value to be searched for in the nodes of the bst
    :param value: integer representing the value of the current closest node to the target
    :param diff: integer representing the difference between the closest node to the target an the target itself
    :return: integer value corresponding to the closest node value to the target between the previous value and the
    current one
    """
    if abs(target - tree.value) < diff:
        value = tree.value
        diff = abs(target - tree.value)

    return value, diff


# Time O(h) average case, where h is the the height of the tree which is h = lg(n) where n is the
# number of node sin the tree, hence average case is O(lg(n)). The worst case is O(n),
# when the tree is skewed and has, for example, only left sides (single chain)

# Space O(h), where h is the height of the tree and is the same as h = O(lg(n)). In the worst case
# the space is O(n) fr the same reason as in the time complexity
def find_closest_value_in_bst_recursive_clean(tree, target):
    """ My clean recursive solution

    This function is pretty much the same as the previous one (my recursive solution), the complexity is the same. There is just a small
    difference in the implementation to make the code cleaner. In this case the check for when the current node value is
    the same as the target is omitted. Everything else is pretty much the same.

    :param tree: object of type BST representing a binary tree
    :param target: integer representing the target value to be searched for in the nodes of the bst
    :return: integer value corresponding to the closest node value to the target
    """
    closest_value = {'value': None, 'diff': float('inf')}
    # print(closest_value)
    closest_value = get_value(tree, target, closest_value)
    # print(closest_value)
    return closest_value['value']


def get_value(tree, target, closest_value):
    """ Helper function for my recursive clean solution

    This function is the helper for my recursive clean solution and it takes care of all the logic.

    :param tree: object of type BST representing a binary tree
    :param target: integer representing the target value to be searched for in the nodes of the bst
    :param closest_value: integer representing the value of the current closest node to the target
    :return: integer value corresponding to the closest node value to the target
    """
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
# number of node sin the tree, hence average case is O(lg(n)). The worst case is O(n),
# when the tree is skewed and has, for example, only left sides (single chain)

# Space O(1)
def find_closest_value_in_bst_iterative_clean(tree, target):
    """ My iterative clean solution

    This solution solves the problem iteratively. It uses a while loop to check for the base case for when the current
    node is None.

    It is clean because it does not perform the check to see if the target is the same as the current node. It basically
    waits until the current nod eis None and then jst returns the closest value.

    Then, the first thin on every iteration is to update the closest value to the target based on the current node.

    Then it checks if the target is smaller or greater than the current node and updates the current node to the left or
    right child respectively.

    The time complexity is the same as the previous solutions, the space complexity is O(1) because there is no call
    stack.

    :param tree: object of type BST representing a binary tree
    :param target: integer representing the target value to be searched for in the nodes of the bst
    :return: integer value corresponding to the closest node value to the target
    """
    closest_value = {'value': None, 'diff': float('inf')}

    while tree is not None:

        closest_value = update_closest(closest_value, target, tree)

        if target >= tree.value:
            tree = tree.right

        elif target <= tree.value:
            tree = tree.left

    return closest_value['value']


# Time O(h) average case, where h is the the height of the tree which is h = lg(n) where n is the
# number of node sin the tree, hence average case is O(lg(n)). The worst case is O(n),
# when the tree is skewed and has, for example, only left sides (single chain)
# Space O(1)
def find_closest_value_in_bst_iterative(tree, target):
    """ My iterative solution

    This solution is the same as the previous one, the only difference is that it checks to see if the current node is
    the same as the target. This makes the solution a little more efficient but does not really affect the complexity.

    :param tree: object of type BST representing a binary tree
    :param target: integer representing the target value to be searched for in the nodes of the bst
    :return: integer value corresponding to the closest node value to the target
    """
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

    :param closest_value: dictionary containing the value of the closest node to the target and their difference
    :param target: integer representing the target value to be searched for in the nodes of the bst
    :param tree: object of type BST representing a binary tree
    :return: integer value corresponding to the closest node value to the target between the previous value and the
    current one
    """
    if abs(tree.value - target) < closest_value['diff']:
        closest_value['value'] = tree.value
        closest_value['diff'] = abs(tree.value - target)

    return closest_value


# Time O(h) average case, where h is the the height of the tree which is h = lg(n) where n is the
# number of node sin the tree, hence average case is O(lg(n)). The worst case is O(n),
# when the tree is skewed and has, for example, only left sides (single chain)

# Space O(h), where h is the height of the tree and is the same as h = O(lg(n)). In the worst case
# the space is O(n) fr the same reason as in the time complexity
def find_closest_value_in_bst_recursive_original(tree, target):
    """ Recursive original solution

    This solution is the same as my recursive clean solution

    :param tree: object of type BST representing a binary tree
    :param target: integer representing the target value to be searched for in the nodes of the bst
    :return: integer value corresponding to the closest node value to the target
    """
    return find_closest_value_recursive_original_helper(tree, target, tree.value)


def find_closest_value_recursive_original_helper(tree, target, closest):
    """ Helper function for recursive original solution

    This helper function takes care of all the logic

    :param tree: object of type BST representing a binary tree
    :param target: integer representing the target value to be searched for in the nodes of the bst
    :param closest: integer representing the value of the current closest node to the target
    :return: integer value corresponding to the closest node value to the target
    """
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
    """ Original iterative solution

    This is the same as my iterative clean solution

    :param tree: object of type BST representing a binary tree
    :param target: integer representing the target value to be searched for in the nodes of the bst
    :return: integer value corresponding to the closest node value to the target
    """
    return find_closest_value_recursive_original_helper(tree, target, tree.value)


def find_closest_value_iterative_original_helper(tree, target, closest):
    """ Helper function for original iterate solution

    This helper function takes care of the logic.
    
    :param tree: object of type BST representing a binary tree
    :param target: integer representing the target value to be searched for in the nodes of the bst
    :param closest: integer representing the value of the current closest node to the target
    :return: integer value corresponding to the closest node value to the target
    """
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
