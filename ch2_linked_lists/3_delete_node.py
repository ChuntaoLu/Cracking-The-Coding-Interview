import unittest
from singly_linked_list import LinkedList


def delete_node(node):
    """Delete a node from a linked list when only the node is given.
    
    Note: node = node.next won't work, because it merely reassign
    the variable 'node' to the next node, thus does not mutate the node.
    To mutuate the node, one has to change the node object's attributes.

    If the node given is the last node, there is no way to delete it.
    node = None will not work here in a function call, node is a reference
    variable that points to the node object on the heap, assign it to
    None does not change the fact that prevous node's next attribute still
    points to the node object on the heap.

    Argument passing is passing-by-object-reference.
    """
    if node is None or node.next is None:
        return false
    next_node = node.next
    node.value = next_node.value
    node.next = next_node.next
    return True
    
class DeleteNodeTest(unittest.TestCase):
    def setUp(self):
        self.l = LinkedList()
        for i in range(3):
            self.l.append(i)
        self.node = self.l.first.next

    def test_delete_node(self):
        res = delete_node(self.node)
        self.assertTrue(res)
        self.assertEqual(str(self.l), 'Linked list: [0->2]')

if __name__ == '__main__':
    unittest.main()
