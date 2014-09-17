import math
import unittest
from tree_utils import Node


def build_minimal_bst(array, start, end):
    """Build a minimal height binary search tree given a sorted arry.
    Child trees have equal size, so the resulted bst might not be complete.
    """
    if start >= end:
        return None
    mid = (start + end) // 2
    root = Node(array[mid])
    root.left = build_minimal_bst(array, start, mid)
    root.right = build_minimal_bst(array, mid + 1, end)
    return root

def build_complete_bst(array, start, end):
    """Build a complete binary search tree given a sorted array."""
    if start >= end:
        return None
    # find the root node index in the given array
    l = end - start
    height = int(math.log(l, 2))
    num_of_leafs = l - (2 ** height - 1)
    if num_of_leafs > 2 ** (height - 1):
        left_tree_size = 2 ** height - 1
    else:
        left_tree_size = l - 2 ** (height - 1)
    root_index = start + left_tree_size
    # recursively build bst
    root = Node(array[root_index])
    root.left = build_complete_bst(array, start, root_index)
    root.right = build_complete_bst(array, root_index + 1, end)
    return root
    
class BuildMinimalBSTTest(unittest.TestCase):
    def setUp(self):
        self.build_bst = build_minimal_bst

    def test_build_empty(self):
        self.assertEqual(self.build_bst([], 0, 0), None)

    def test_build_one_node(self):
        root = self.build_bst([0], 0, 1)
        self.assertEqual(root.data, 0)
        self.assertEqual(root.left, None)
        self.assertEqual(root.right, None)

    def test_build_full(self):
        root = self.build_bst([0, 1, 2], 0, 3)
        self.assertEqual(root.left.data, 0)
        self.assertEqual(root.left.left, None)
        self.assertEqual(root.left.right, None)
        self.assertEqual(root.data, 1)
        self.assertEqual(root.right.data, 2)
        self.assertEqual(root.right.left, None)
        self.assertEqual(root.right.right, None)

    def test_build_complete(self):
        root = self.build_bst([0, 1, 2, 3], 0, 4)
        self.assertEqual(root.data, 2)
        self.assertEqual(root.left.data, 1)
        self.assertEqual(root.left.left.data, 0)
        self.assertEqual(root.left.left.left, None)
        self.assertEqual(root.left.left.right, None)
        self.assertEqual(root.left.right, None)
        self.assertEqual(root.right.data, 3)
        self.assertEqual(root.right.left, None)
        self.assertEqual(root.right.right, None)

class BuildCompleteBSTTest(BuildMinimalBSTTest):
    def setUp(self):
        self.build_bst = build_complete_bst

if __name__ == '__main__':
    unittest.main()
