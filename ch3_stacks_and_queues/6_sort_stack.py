import unittest
from random import shuffle


def sort_stack_recursive(stack):
    """Sort a stack in place recursively using only one helper stack."""
    if len(stack) < 2:
        return
    item = stack.pop()
    sort_stack_recursive(stack)
    helper = []
    while stack and stack[-1] > item:
        helper.append(stack.pop())
    stack.append(item)
    while helper:
        stack.append(helper.pop())

def sort_stack_iterative(stack):
    """Sort a stack in place iteratively using only one helper stack."""
    if len(stack) < 2:
        return
    helper = []
    while stack:
        helper.append(stack.pop())
    while helper:
        item = helper.pop()
        while stack and stack[-1] > item:
            helper.append(stack.pop())
        stack.append(item)

class SortStackTest(unittest.TestCase):
    def setUp(self):
        self.sr = list(range(10))
        shuffle(self.sr)
        self.si = self.sr[:]

    def test_sort_stack_recursive(self):
        sort_stack_recursive(self.sr)
        self.assertEqual(self.sr, list(range(10)))

    def test_sort_stack_iterative(self):
        sort_stack_iterative(self.si)
        self.assertEqual(self.si, list(range(10)))
 
if __name__ == '__main__':
    unittest.main()
