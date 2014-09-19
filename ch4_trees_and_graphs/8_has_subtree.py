import unittest
from tree_utils import Node


def has_subtree(x, y):
    """Check if tree x has subtree y."""
    if y is None:
        return True

    if x is None:
        return False

    if is_equal_tree(x, y):
        return True

    return has_subtree(x.left, y) or has_subtree(x.right, y)

def is_equal_tree(x, y):
    """Two trees are equal if they have the same structure and same data
    for corresponding nodes."""
    if None in {x, y}:
        return x == y

    if x.data != y.data:
        return False

    return is_equal_tree(x.left, y.left) and is_equal_tree(x.right, y.right)

class HasSubtreeTest(unittest.TestCase):
    def setUp(self):
        self.x = Node(0,
                Node(1,
                    None,
                    Node(3)),
                Node(2))
        self.y = Node(0, Node(2))
        self.z = Node(1, None, Node(3))
        

    def test_has_subtree(self):
        self.assertTrue(has_subtree(None, None))
        self.assertTrue(has_subtree(self.x, None))
        self.assertFalse(has_subtree(None, self.x))
        self.assertFalse(has_subtree(self.x, self.y))
        self.assertTrue(has_subtree(self.x, self.z))

if __name__ == '__main__':
    unittest.main()
