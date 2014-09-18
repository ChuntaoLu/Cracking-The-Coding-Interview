import unittest
from tree_utils import Node


class NodeWithParent(Node):
    """Node with link to its parent."""
    def __init__(self, data=None, left=None, right=None, parent=None):
        super().__init__(data, left, right)
        if left:
            left.parent = self
        if right:
            right.parent = self
        self.parent = parent

def suscessor(node):
    """Return the successor of a node in a bst.
    
    case 1: node has right subtree, return the leftmost node in the subtree;
    case 2: node has no right subtree, trace back its parent until it's not
            a right branch, return that parent;
            If it's al right branch up to root, return None.
    """
    if node is None:
        return None
    if node.right:
        res = node.right
        while res.left:
            res = res.left
    else:
        parent = node.parent
        while parent:
            if parent.left == node:
                break
            node = parent
            parent = node.parent
        res = parent
    return res

class SuccessorTest(unittest.TestCase):
    def setUp(self):
        nwp = NodeWithParent
        self.root = nwp(3,
                nwp(0,
                    None,
                    nwp(2,nwp(1))),
                nwp(4))

    def test_successor_none(self):
        self.assertEqual(suscessor(None), None)
        self.assertEqual(suscessor(self.root.right), None)

    def test_successor_right(self):
        self.assertEqual(suscessor(self.root).data, 4)
        self.assertEqual(suscessor(self.root.left).data, 1)
    
    def test_successor_parent(self):
        self.assertEqual(suscessor(self.root.left).data, 1)
        self.assertEqual(suscessor(self.root.left.right).data, 3)

if __name__ == '__main__':
    unittest.main()
