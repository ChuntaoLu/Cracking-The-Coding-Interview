import unittest
from tree_utils import Node


def is_bst_compare(root):
    """Check if tree is bst by definition."""
    return _is_bst_compare(root, float('-inf'), float('inf'))

def _is_bst_compare(root, mini, maxi):
    """Recursively check if a node is in given range.
    
    Any node in a bst must be less than all right nodes and bigger
    than all left nodes.
    
    min and max value for each node is updated as level increases.
    For the starting level, min and max is not known yet, hence negative
    and positive infinity.

    Note here min and max are NOT the maximum from the left subtree
    and the minimum for the right subtree.
    
    Imagine the process as creating a bst: the root node has no limits,
    but as a new node being added, it has to restricted by its parents. 
    """
    if root is None:
        return True
    if not (mini < root.data < maxi):
        return False
    left = _is_bst_compare(root.left, mini, root.data)
    return left and  _is_bst_compare(root.right, root.data, maxi)

def is_bst_iterative_traversal(root):
    """In-order traversal should lead to the fact that every node is
    bigger than the previous one."""
    prev = float('-inf')
    stack = []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            if root.data < prev:
                return False
            prev = root.data
            root = root.right
    return True

def is_bst_recursive_traversal(root):
    """Recursive traversal and check with previous node."""
    prev = float('-inf')
    def _is_bst_recursive_traversal(root):
        nonlocal prev
        if root is None:
            return True
        
        if not _is_bst_recursive_traversal(root.left):
            return False

        if prev > root.data:
            return False
        else:
            prev = root.data

        if not _is_bst_recursive_traversal(root.right):
            return False

        return True
    return _is_bst_recursive_traversal(root)

class IsBstCompareTest(unittest.TestCase):
    def setUp(self):
        self.is_bst = is_bst_compare

    def test_None(self):
        self.assertTrue(self.is_bst(None))

    def test_one_node(self):
        self.assertTrue(self.is_bst(Node(0)))

    def test_true(self):
        tree = Node(2,
                Node(0,
                    None,
                    Node(1)),
                Node(4,
                    Node(3)))
        self.assertTrue(self.is_bst(tree))

    def test_false(self):
        tree = Node(2,
                Node(0,
                    None,
                    Node(5)),
                Node(4,
                    Node(3)))
        self.assertFalse(self.is_bst(tree))

class IsBstIterativeTraversalTest(IsBstCompareTest):
    def setUp(self):
        self.is_bst = is_bst_iterative_traversal

class IsBstRecursiveTraversalTest(IsBstCompareTest):
    def setUp(self):
        self.is_bst = is_bst_recursive_traversal

if __name__ == '__main__':
    unittest.main()
