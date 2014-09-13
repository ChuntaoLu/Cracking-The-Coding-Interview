import unittest


class MultiStacks(object):
    """Multiple stacks implemented using one list.
    
    Each stack has fixed size.
    """
    def __init__(self, size=100, num=3):
        self.size = size
        self.num = num
        self.array = [None] * size * num
        self.pointers = [-1] * num

    def pop(self, n):
        """Pop an item from the nth stack, n starts from 0."""
        if self.pointers[n] < 0:
            raise IndexError('pop from empty stack')
        out = self.array[n * self.size + self.pointers[n]]
        self.pointers[n] -= 1
        return out

    def push(self, n, item):
        """Push an item to the nth stack, n starts from 0."""
        if self.pointers[n] == self.size - 1:
            raise IndexError('stack is full')
        self.pointers[n] += 1
        self.array[n * self.size + self.pointers[n]] = item
        
    def peek(self, n):
        """Peek the stack top of nth stack."""
        if self.pointers[n] < 0:
            return None
        return self.array[n * self.size + self.pointers[n]]

class MultiStacksTest(unittest.TestCase):
    def setUp(self):
        self.stacks = MultiStacks(100, 3)
        for i in range(50):
            self.stacks.push(0, i)

    def test_pop(self):
        self.assertRaises(IndexError, self.stacks.pop, 1)
        self.assertEqual(self.stacks.pop(0), 49)

    def test_push(self):        
        self.stacks.push(1, 39)
        self.assertEqual(self.stacks.pop(1), 39)
        for i in range(100):
            self.stacks.push(1, i)
        self.assertRaises(IndexError, self.stacks.push, 1, 4)

    def test_peek(self):
        self.assertEqual(self.stacks.peek(0), 49)
        self.assertEqual(self.stacks.peek(1), None)
    
if __name__ == '__main__':
    unittest.main()
