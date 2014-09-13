import unittest


class StackWithMin(object):
    """Stack that supports current minimum lookup in O(1)."""
    def __init__(self):
        """Use a list to track minimums when new item is pushed."""
        self.stack = []
        self.mins = []

    def pop(self):
        """If popped matches the current minimum, pop from mins."""
        popped = self.stack.pop()
        if popped == self.mins[-1]:
            self.mins.pop()
        return popped

    def push(self, item):
        """If pushed item is no bigger than current minimum, push it to mins."""
        self.stack.append(item)
        if not self.mins or item <= self.mins[-1]:
            self.mins.append(item)

    def current_min(self):
        """mins list stores sequentially pushed minimums."""
        if not self.mins:
            raise IndexError('stack is empty')
        return self.mins[-1]

class StackWithMinTest(unittest.TestCase):
    def setUp(self):
        self.stack = StackWithMin()

    def test_current_min(self):
        self.stack.push(5)
        self.assertEqual(self.stack.current_min(), 5)
        self.stack.push(8)
        self.assertEqual(self.stack.current_min(), 5)
        self.stack.push(3)
        self.assertEqual(self.stack.current_min(), 3)
        self.stack.pop()
        self.assertEqual(self.stack.current_min(), 5)
        self.stack.pop()
        self.assertEqual(self.stack.current_min(), 5)
        self.stack.pop()
        self.assertRaises(IndexError, self.stack.current_min)

if __name__ == '__main__':
    unittest.main()
