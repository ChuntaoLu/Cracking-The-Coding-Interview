import unittest
from singly_linked_list import LinkedList


def remove_dups(l):
    """Remove duplicate nodes in a linked list.

    Time: O(n), space: O(n)
    """
    if len(l) < 2:
        return
    current = l.first
    table = set()
    while current:
        if current.value in table:
            previous.next = current.next
        else:
            table.add(current.value)
            previous = current
        current = current.next

def remove_dups_runner(l):
    """Remove duplicate nodes without using a set.
    
    Time: O(n^2), space: O(1)
    """
    if len(l) < 2:
        return
    current = l.first
    while current:
        node = current
        while node.next:
            if node.next.value == current.value:
                node.next = node.next.next
            else:
                node = node.next
        current = current.next


class RemoveDupTest(unittest.TestCase):
    def setUp(self):
        self.l = LinkedList()
        self.l.append(0)
        self.l.append(1)
        self.l.append(2)
        self.old = self.l

    def test_remove_dups_when_no_duplicates_exist(self):
        remove_dups(self.l)
        self.assertEqual(self.l, self.old)

    def test_remove_dups_when_duplicates_exist(self):
        self.l.append(1)
        self.l.append(0)
        remove_dups(self.l)
        self.assertEqual(self.l, self.old)

    def test_remove_dups_runner_when_no_duplicates_exist(self):
        remove_dups_runner(self.l)
        self.assertEqual(self.l, self.old)

    def test_remove_dups_runner_when_duplicates_exist(self):
        self.l.append(1)
        self.l.append(0)
        remove_dups_runner(self.l)
        self.assertEqual(self.l, self.old)

if __name__ == '__main__':
    unittest.main()
