import unittest
from singly_linked_list import Node, LinkedList


def is_palindrome_reverse(head):
    """Iteratively check if is palindrome by comparing to reversed."""
    prev = None
    current = head
    counter = 0
    while current:
        counter += 1
        node = Node(current.value)
        node.next = prev
        prev = node
        current = current.next

    for _ in range(counter // 2):
        if head.value != prev.value:
            return False
        head = head.next
        prev = prev.next
    return True

def is_palindrome_stack(head):
    """Push the first half to a stack and compare with the second half.
    
    Use runner trick when length unkown. Look out for odd/even length.
    """
    slow = fast = head
    stack = []
    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next

    # take care the odd length case
    if fast:
        slow = slow.next

    # compare stack with the second half
    while slow:
        if stack.pop() != slow.value:
            return False
        slow = slow.next
    return True

def _is_palindrome_recursive(head, length):
    """Each recursion returns of (is_current_palindrome, next_node_to_compare).
    
    Suppose length of the linked list is given.
    """
    if length == 0:
        return True, head
    if length == 1:
        return True, head.next

    res, node = _is_palindrome_recursive(head.next, length - 2)
    if not res:
        return res, None
    else:
        return head.value == node.value, node.next

def is_palindrome_recursive(head):
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    return _is_palindrome_recursive(head, length)[0]

class IsPalindromeTest(unittest.TestCase):
    def setUp(self):
        self.l = LinkedList()
        for i in 'abcba':
            self.l.append(i)
    
for name in ['reverse', 'stack', 'recursive']:
    func = globals()['is_palindrome_' + name]

    def _test_empty(self, name=name):
        self.assertTrue(func(None))
    setattr(IsPalindromeTest, 'test_empty_' + name, _test_empty)

    def _test_one_node(self, name=name):
        node = Node('x')
        self.assertTrue(func(node))
    setattr(IsPalindromeTest, 'test_one_node_' + name, _test_one_node)

    def _test_multiple_nodes(self, name=name):
        self.assertTrue(func(self.l.first))
        self.l.append('c')
        self.assertFalse(func(self.l.first))
    setattr(IsPalindromeTest, 'test_multiple_nodes_' + name, _test_multiple_nodes)

if __name__ == '__main__':
    unittest.main()
