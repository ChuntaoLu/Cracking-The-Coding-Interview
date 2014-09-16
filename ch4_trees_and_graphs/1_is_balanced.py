import unittest


class Node(object):
    """Node for binary tree."""
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def _check_height(node):
    """Recursively check if subtree is balanced, if so return height,
    otherwise return None."""
    if node is None:
        return 0

    left_height = _check_height(node.left)
    if left_height is None:
        return None

    right_height = _check_height(node.right)
    if right_height is None:
        return None

    if abs(left_height - right_height) < 2:
        return max(left_height, right_height) + 1
    else:
        return None

def is_balanced(node):
    return _check_height(node) is not None
    
class IsBalancedTest(unittest.TestCase):
    def setUp(self):
        self.t1 = Node(1)
        self.t2 = Node(2, Node(2))
        self.t3 = Node(3, Node(2), Node(1))
        self.t4 = Node(3, Node(2, Node(1)))


    def test_is_balanced_None(self):
        self.assertTrue(is_balanced(None))
    
    def test_is_balanced_one_node(self):
        self.assertTrue(is_balanced(self.t1))

    def test_is_balanced_true(self):
        self.assertTrue(is_balanced(self.t2))
        self.assertTrue(is_balanced(self.t3))

    def test_is_balanced_false(self):
        self.assertFalse(is_balanced(self.t4))

if __name__ == '__main__':
    unittest.main()
