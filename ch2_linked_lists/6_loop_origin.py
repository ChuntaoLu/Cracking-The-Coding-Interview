import unittest
from singly_linked_list import Node, LinkedList


def loop_origin(head):
    """Check if linked list has a loop, if so return the loop origin."""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    else:
        # no loop
        return False

    while head is not slow:
        head = head.next
        slow = slow.next
    return head

class LoopOriginTest(unittest.TestCase):
    def setUp(self):
        self.l = LinkedList()
        for i in 'ABCDE':
            self.l.append(i)

    def test_no_loop(self):
        self.assertFalse(loop_origin(self.l.first))

    def test_loop_origin(self):
        origin = self.l.first.next.next
        self.l.last.next = origin
        self.assertEqual(loop_origin(self.l.first), origin)

if __name__ == '__main__':
    unittest.main()
