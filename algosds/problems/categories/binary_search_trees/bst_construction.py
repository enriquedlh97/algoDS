"""
Problem:

Write a BST class for a Binary Search Tree. The class should support:

• Inserting values with the insert method.
• Removing values with the remove method; this method should only remove the first instance of a given value.
• Searching for values with the contains method.

Note that you can't remove values from a single-node tree. In other words, calling the remove method on a single
node tree should simply not do anything.

Each BST node has an integer value, a left child node, and a right child node. A node is said to be a valid BST node if
and only if it satisfies the BST property. Its value is strictly greater than the values of every node to its left; its
value is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes
themselves or None / null .

When a node with 2 children is removed, the smallest node of its right branch should take the place of the removed node.
This smallest node from the right branch should be moved from its current position to the position fo the node to be
removed.

Sample usage:

     This is an already related bst
               10
             /    \
            5      15
          /  \    /  \
         2    5  13   22
       /          \
      1           14

     The following operations are performed sequentially

     insert(12):

               10
             /     \
            5       15
          /  \     /  \
         2    5   13   22
       /         /  \
      1         12  14

      remove(10):

               12
             /    \
            5      15
          /  \    /  \
         2    5  13   22
       /          \
      1           14

      contains(15): True
"""


class BST:
    def __init__(self, value):
        """ Binary Search Tree

        This is the main class for the binary search tree. Every node is initialized with a value (required as
        parameter) and with left and right nodes as None.

        :param value: int value corresponding to the value of the node
        """
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        """ Method for inserting nodes in BST

        :param value: int value corresponding to the value of the node to be inserted in the BST
        :return: self, corresponding to the root value of the BST
        """

        node = self
        parent = None  # Keeps track of parent node, is initialized as None for root node

        while node is not None:

            if value < node.value:
                left = True
                parent = node
                node = node.left

            elif value >= node.value:
                left = False
                parent = node
                node = node.right

        if left:
            parent.left = BST(value)
        else:
            parent.right = BST(value)

        return self

    def contains(self, value):
        """ Method for checking if a value is in a BST

        :param value: integer value corresponding to the value to be searched in the BST
        :return: True if the value is in the BST; False otherwise
        """

        node, parent, found = self.search(value)

        return found

    def search(self, value):
        """ Helper method for contains method. Used for actually searching for the value in the BST

        :param value: integer value corresponding to the value to be searched in the BST
        :return: node, parent, bool: Three elements are returned. The "bool" element is True if the value was found in
                 the BST; False otherwise. The "node" element is a BST object corresponding to the searched node (only
                 if it was found), if it was not found, the node element has a value of None. Parent is a BST object
                 corresponding to the parent node of the searched node. If the searched node was not found, then
                 parent = None. If the searched node was found, then one of its children points to the searched node. If
                 the searched node corresponds to the root nod eof the BST, then the parent = None.
        """
        node = self
        parent = None

        while node is not None:

            if value == node.value:
                return node, parent, True

            elif value < node.value:
                parent = node
                node = node.left

            elif value > node.value:
                parent = node
                node = node.right

        return node, parent, False

    def remove(self, value, exclude_parent=False):
        """ Method for removing a node form a BST

        :param value: integer value representing the node to be removed
        :param exclude_parent: optional boolean argument. 
        :return:
        """

        if not exclude_parent:
            node, parent, found = self.search(value)
        else:
            parent = self
            # Search right branch first
            node_right, _, found_right = self.right.search(value)
            if found_right:  # If searched value is in right branch, keep its values
                node, found = node_right, found_right
            else:  # If it was not in right branch, then the values from left branch must be used
                # We ignore the returned parent because this case is for when we don't want the search to include the
                # parent. And we already set the parent as self, we just don't want the search to include the parent
                # because we could get in a loop an infinite loop when the parent value is the same as the searched
                # value.
                node, _, found = self.left.search(value)

        if found:  # Proceed if node to be removed is in deed in the bst
            # Case 1: No Children
            if node.left is None and node.right is None:
                # print("Case 1")
                # This if handles for when root node is deleted and there is no node left.
                # When this happens, the None value is returned; otherwise more checks are performed
                if parent is not None:
                    # This statement checks for when the parent of the node to be deleted has one None child. Since the
                    # node to be deleted exists, then it means that the parent node has at least one children. This
                    # check has to be performed because there is no guarantee that the parent node has 2 children. So,
                    # when checking "if parent.left.value is not None" and the parent has no left child, an error
                    # occurs.
                    if parent.left is not None and parent.left.value == value:
                        # Removes child node from parent if the node corresponds to the left child
                        parent.left = None
                    # Since we know that the parent has at least one child, (because the node to be deleted has been
                    # found), no further checks need to be performed like in the left child case above.
                    else:
                        parent.right = None
                else:
                    return None

            # Case 2: 2 Children
            elif node.left is not None and node.right is not None:
                # print("Case 2")
                # Find smallest node from right branch
                smallest = node.find_smallest(node.right)
                # Remove smallest node from right branch
                # We want to exclude the parent in the search when the parent has the same value as the smallest value
                # in its right branch. We do this because if these values are both the same, when we call the remove
                # method, it would get stuck in an infinite loop. For instance, imagine parent.value = 10 and
                # parent.right.value = 10 and parent.right.right.value = parent.left.left.value = None
                # This would make a tree with just 2 nodes, 10 - 10
                # If we want to remove the root node. We call this method, we get the smallest value from the right
                # branch, which is also 10 (but it is not the same node), then the remove method is called to remove
                # this second node. But the remove method looks for the first node with value 10, so it would find first
                # the root node again. And the process would repeat because it would never find the second node with
                # value 10. this is because the remove method always removes the first occurrence of a value.
                # For this reason, in cases like this, we have to tell the remove method to ignore the parent in the
                # search.
                if node.value == smallest:
                    node.remove(smallest, exclude_parent=True)
                else:
                    node.remove(smallest, exclude_parent=False)
                # Replace current node with smallest node from right branch
                node.value = smallest

            # Case 3: 1 Child
            else:
                # print("Case 3")
                if parent is not None:
                    if parent.left is not None and parent.left.value == value:
                        # Removes node from its parent
                        if node.left is not None:
                            parent.left = node.left
                        elif node.right is not None:
                            parent.left = node.right
                    elif parent.right is not None and parent.right.value == value:
                        # Removes node from its parent
                        if node.left is not None:
                            parent.right = node.left
                        elif node.right is not None:
                            parent.right = node.right

                else:
                    if node.left is not None:
                        node = node.left
                    elif node.right is not None:
                        node = node.right
                    self.value = node.value
                    self.left = node.left
                    self.right = node.right

                return self

        else:  # Node to be removed is not in bst, return bst as it is
            return self

    @staticmethod
    def find_smallest(node):
        smallest = node.value

        while node.left is not None:
            node = node.left
            smallest = node.value

        return smallest
