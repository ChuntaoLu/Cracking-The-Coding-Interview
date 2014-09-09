import unittest
from singly_linked_list import LinkedList


def kth_to_last(l, k):
    """Find the kth to last node given length is known"""
    counter = 0
    current = l.first
    length = len(l)
    index = length - 1 - k
    if index < 0:
        return None
    while current:
        if counter == index:
            return current
        else:
            current = current.next
            counter += 1

def kth_to_last_recursive(node, k):
    """Find the kth to last node given the first node of a linked list.
    
    Recursive approach: suppose func(last, k) returns 0 and return value
    increases one by every step, then func(first, k) returns length - 1.
    At some intermediate step, the return value will equal k, and the 
    corresponding node is the kth node.
    """
    res = []
    def _kth_to_last(node, k):
        if node is None:
            return -1
        else:
            num = _kth_to_last(node.next, k) + 1
            if num == k:
                res.append(node)
        return num
    _kth_to_last(node, k)
    return res[0] if res else None

def kth_to_last_iterative(node, k):
    """Two pointer runner pattern."""
    slow = fast = node
    for _ in range(k):
        fast = fast.next
        if fast is None:
            return None
    while fast.next:
        slow = slow.next
        fast = fast.next
    return slow

class FindKthTest(unittest.TestCase):
    def setUp(self):
        self.l = LinkedList()
        for i in range(5):
            self.l.append(i)
        self.node = self.l.first

    # naive approach
    def test_first(self):
        self.assertEqual(kth_to_last(self.l, 4), self.l.first)

    def test_last(self):
        self.assertEqual(kth_to_last(self.l, 0), self.l.last)

    def test_middle(self):
        self.assertEqual(kth_to_last(self.l, 3), self.l.first.next)

    def test_out_of_range(self):
        self.assertEqual(kth_to_last(self.l, 5), None)

    # recursive
    def test_first_recursive(self):
        self.assertEqual(kth_to_last_recursive(self.node, 4), self.l.first)

    def test_last_recursive(self):
        self.assertEqual(kth_to_last_recursive(self.node, 0), self.l.last)

    def test_middle_recursive(self):
        self.assertEqual(kth_to_last_recursive(self.node, 3), self.l.first.next)

    def test_out_of_range_recursive(self):
        self.assertEqual(kth_to_last_recursive(self.node, 5), None)

    # iterative
    def test_first_iterative(self):
        self.assertEqual(kth_to_last_iterative(self.node, 4), self.l.first)

    def test_last_iterative(self):
        self.assertEqual(kth_to_last_iterative(self.node, 0), self.l.last)

    def test_middle_iterative(self):
        self.assertEqual(kth_to_last_iterative(self.node, 3), self.l.first.next)

    def test_out_of_range_iterative(self):
        self.assertEqual(kth_to_last_iterative(self.node, 5), None)


if __name__ == '__main__':
    unittest.main()
