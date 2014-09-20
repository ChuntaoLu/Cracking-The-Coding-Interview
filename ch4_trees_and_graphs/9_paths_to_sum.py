import unittest
from tree_utils import Node


def _paths_to_sum(root, num, path, level, res):
    """Keep track the path from root to current node using an array,
    sum backwards until root, if suitable path found then add it to result.

    path array has as many elements as the tree level, backtrace starting
    index is always the current level.
    
    Does not stop backtracking when a path is found, so capable of finding all
    suitable paths.
    """
    if root is None:
        return

    path[level] = root.data
    
    _sum = 0
    for i in range(level, -1, -1):
        _sum += path[i]
        if _sum == num:
            res.append(path[i: level + 1])

    _paths_to_sum(root.left, num, path, level + 1, res)
    _paths_to_sum(root.right, num, path, level + 1, res)

def _get_depth(root):
    """Recursively compute tree depth."""
    if root is None:
        return 0
    return 1 + max(_get_depth(root.left), _get_depth(root.right))

def paths_to_sum(root, num):
    """Return all paths from all nodes that adds up to num."""
    depth = _get_depth(root)
    path = [None for _ in range(depth)]
    res = []
    _paths_to_sum(root, num, path, 0, res)
    return res
    
class PathsToSumTest(unittest.TestCase):
    def setUp(self):
        self.root = Node(1,
                Node(7,
                    Node(3,
                        Node(0)),
                    Node(5)),
                Node(4,
                    Node(3),
                    Node(2,
                        Node(1))))

    def test_paths_to_sum(self):
        self.assertEqual(paths_to_sum(None, 10), [])
        self.assertEqual(paths_to_sum(self.root, 20), [])
        self.assertEqual(paths_to_sum(self.root, 10), [[7, 3], [7, 3, 0]])
        self.assertEqual(paths_to_sum(self.root, 7), [[7], [4, 3], [1, 4, 2], [4, 2, 1]])

if __name__ == '__main__':
    unittest.main()
