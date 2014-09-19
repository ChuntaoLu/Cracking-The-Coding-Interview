import unittest
from functools import partial
from tree_utils import NodeWithParent as nwp


def common_ancestor_with_parent(x, y):
    """Find first common ancestor if nodes have link to parents."""
    lx, ly = _get_level(x), _get_level(y)
    x, y = (y, x) if ly < lx else (x, y)
    for _ in range(abs(lx - ly)):
        y = y.parent
    while x != y:
        x = x.parent
        y = y.parent
    return x

def _get_level(node):
    """Helper for common_ancestor_with_parent, returns node depth."""
    level = 0
    while node.parent:
        node = node.parent
        level += 1
    return level

def common_ancestor_recursive(root, x, y):
    """Recusively find the first common ancestor of two nodes given root.
    
    If root is one of the nodes, root is the common ancestor.
    If two nodes on two different subtrees, root is the common ancestor.
    If both nodes on one of the subtree, recurse on that subtree.
    """
    if root in {None, x, y}:
        return root

    is_x_on_left = _is_ancestor(root.left, x)
    is_y_on_left = _is_ancestor(root.left, y)

    if is_x_on_left != is_y_on_left:
        return root

    side = root.left if is_x_on_left else root.right
    return common_ancestor_recursive(side, x, y)

def _is_ancestor(root, node):
    """Helper for common_ancestor_recursive, check if root is node's ancestor."""
    if root is None:
        return False
    if root == node:
        return True
    return _is_ancestor(root.left, node) or _is_ancestor(root.right, node)
    
def common_ancestor_optimized(root, x, y):
    """Find first common ancestor without repeatly checking if root is ancestor of a node.
    
    If root's subtree contains x but not y, return x
    If root's subtree contains y but not x, return y
    If root's subtree contains neither x nor y, return None
    Else, retun the common ancestor
    """
    if root in {None, x, y}:
        return root

    left = common_ancestor_optimized(root.left, x, y)
    if left and left != x and left != y:
        return left

    right = common_ancestor_optimized(root.right, x, y)
    if right and right != x and right != y:
        return right
    
    if left and right:
        return root
    else:
        return left or right
    
class CommonAncestorWithParentTest(unittest.TestCase):
    def setUp(self):
        self.common_ancestor = common_ancestor_with_parent
        self.root = nwp(1,
                nwp(2,
                    nwp(3),
                    nwp(4,
                        nwp(5),
                        nwp(6))),
                nwp(7))

    def test_common_ancestor(self):
        x = self.root
        y = x.left.right
        self.assertEqual(self.common_ancestor(x, x), x)
        self.assertEqual(self.common_ancestor(x, y), x)
        self.assertEqual(self.common_ancestor(x.left.left, y.right), x.left)

class CommonAncestorRecursive(CommonAncestorWithParentTest):
    def setUp(self):
        super().setUp()
        self.common_ancestor = partial(common_ancestor_recursive, self.root)

class CommonAncestorOptimized(CommonAncestorWithParentTest):
    def setUp(self):
        super().setUp()
        self.common_ancestor = partial(common_ancestor_optimized, self.root)

if __name__ == '__main__':
    unittest.main()
