import unittest


class Node:
    """Node with left subtree size."""
    def __init__(self, value=None, left_size=0):
        self.value = value
        self.left_size = left_size
        self.left = None
        self.right = None

class BST:
    """Binary search tree that tracks size of each node's left subtree."""
    def __init__(self, root=None):
        self.root = root

    def add(self, node):
        """Add a node to tree."""
        if self.root is None:
            self.root = node
        else:
            self._add(self.root, node)

    def _add(self, root, node):
        """Helper for add, recursively add node to tree.
        When adding to a node's left, node's left_size increases by 1.
        """
        if node.value == root.value:
            root.left_size += 1
        elif node.value < root.value:
            if root.left is None:
                root.left = node
            else:
                self._add(root.left, node)
            root.left_size += 1
        else:
            if root.right is None:
                root.right = node
            else:
                self._add(root.right, node)

    def get_rank(self, value):
        """Returns the number of nodes that have less value."""
        return self._get_rank(self.root, value)

    def _get_rank(self, root, value):
        """Recursively get the ranke of the node."""
        if root is None:
            return None
        if root.value == value:
            return root.left_size
        elif value < root.value:
            return self._get_rank(root.left, value)
        else:
            right_size = self._get_rank(root.right, value)
            if right_size is None:
                return None
            else:
                return root.left_size + 1 + right_size


class GetRankTest(unittest.TestCase):
    def setUp(self):
        self.bst = BST()
        for i in [5, 1, 4, 4, 5, 9, 7, 13, 3]:
            self.bst.add(Node(i))

    def test_non_exist(self):
        self.assertEqual(None, self.bst.get_rank(10))
        self.assertEqual(None, self.bst.get_rank(0))

    def test_root(self):
        self.assertEqual(5, self.bst.get_rank(5))

    def test_left(self):
        self.assertEqual(0, self.bst.get_rank(1))
        self.assertEqual(1, self.bst.get_rank(3))
        self.assertEqual(3, self.bst.get_rank(4))

    def test_right(self):
        self.assertEqual(6, self.bst.get_rank(7))
        self.assertEqual(7, self.bst.get_rank(9))
        self.assertEqual(8, self.bst.get_rank(13))

if __name__ == '__main__':
    unittest.main()
