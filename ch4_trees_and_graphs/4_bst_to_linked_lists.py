import unittest
from tree_utils import Node
from ch2_linked_lists.singly_linked_list import LinkedList


def bst_to_linked_lists_bfs(root):
    res = []
    current = LinkedList()
    current.append(root)
    while len(current):
        res.append(current)
        parents = current
        current = LinkedList()
        for node in parents:
            tree_node = node.value
            if tree_node.left:
                current.append(tree_node.left)
            if tree_node.right:
                current.append(tree_node.right)
    return res

def bst_to_linked_lists_dfs(root):
    res = []
    _bst_to_linked_lists_dfs(res, root, 0)
    return res

def _bst_to_linked_lists_dfs(res, root, level):
    if root is None:
        return
    if level == len(res):
        res.append(LinkedList())
    res[level].append(root)
    _bst_to_linked_lists_dfs(res, root.left, level + 1)

class BstToLinkedListsTest(unittest.TestCase):
    def setUp(self):
        self.root = Node(0,
                Node(1, 
                    Node(2), 
                    Node(3, 
                        None,
                        Node(4))),
                Node(5,
                    Node(6),
                    None))

    def test_bst_to_linked_lists_bfs(self):
        linked_lists = bst_to_linked_lists_bfs(self.root)
        self.assertEqual(len(linked_lists), 4)
        self.assertEqual(str(linked_lists[0]), 'Linked list: [0]')
        self.assertEqual(str(linked_lists[1]), 'Linked list: [1->5]')
        self.assertEqual(str(linked_lists[2]), 'Linked list: [2->3->6]')
        self.assertEqual(str(linked_lists[3]), 'Linked list: [4]')

    def test_bst_to_linked_lists_dfs(self):
        linked_lists = bst_to_linked_lists_dfs(self.root)
        self.assertEqual(len(linked_lists), 4)
        self.assertEqual(str(linked_lists[0]), 'Linked list: [0]')
        self.assertEqual(str(linked_lists[1]), 'Linked list: [1->5]')
        self.assertEqual(str(linked_lists[2]), 'Linked list: [2->3->6]')
        self.assertEqual(str(linked_lists[3]), 'Linked list: [4]')

if __name__ == '__main__':
    unittest.main()
