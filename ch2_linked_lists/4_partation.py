import unittest
from singly_linked_list import Node, LinkedList


def partation(node, val):
    """Partation a linked list given its head node, so that all nodes of value
    less than val comes first than those bigger of euqal nodes.
    """
    big = None
    while node:
        if node.value >= val:
            big = big or node
        else:
            if big:
                big.value, node.value = node.value, big.value
                big = big.next
        node = node.next

def partation_merging(node, val):
    """Create two list first then merge into one."""
    small_first = small_last = big_first = big_last = None
    while node:
        next_node = node.next
        node.next = None
        if node.value < val:
            if small_first is None:
                small_first = small_last = node
            else:
                small_last.next = node
                small_last = node
        else:
            if big_first is None:
                big_first = big_last = node
            else:
                big_last.next = node
                big_last = node
        node = next_node
    if small_first is None:
        return big_first
    else:
        small_last.next = big_first
        return small_first

class PartationTest(unittest.TestCase):
    def setUp(self):
        # set up a linked list of 2->3->2->1->0, and partation around 2
        nodes = [Node(i) for i in range(4)]
        for i in range(3, 0, -1):
            nodes[i].next = nodes[i - 1]
        self.val = 2
        self.node = Node(2, nodes[-1])
        self.l = LinkedList()
        self.l.first = self.node
        self.l.last = nodes[0]

    def test_partation(self):
        partation(self.node, self.val)
        self.assertEqual(str(self.l), 'Linked list: [1->0->2->2->3]')

    def test_partation_merge(self):
        l = LinkedList()
        l.first = partation_merging(self.node, self.val)
        self.assertEqual(str(l), 'Linked list: [1->0->2->3->2]')

if __name__ == '__main__':
    unittest.main()

