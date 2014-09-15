import unittest


class MyQueue(object):
    """Queue implemented with two lists.
    
    new always has newly enqueued items.
    old keeps the top items and lazily get items when empty.
    """
    def __init__(self):
        self.new = []
        self.old = []

    def enqueue(self, item):
        """Always enqueue to new."""
        self.new.append(item)

    def dequeue(self):
        """Old has the top items."""
        self._shift_stacks()
        try:
            return self.old.pop()
        except IndexError:
            raise IndexError('dequeue from empty queue')

    def _shift_stacks(self):
        """When old is empty, pop items from new to old."""
        if not self.old:
            while self.new:
                self.old.append(self.new.pop())

class MyQueueTest(unittest.TestCase):
    def setUp(self):
        self.queue = MyQueue()

    def test_my_queue(self):
        self.queue.enqueue(0)
        self.queue.enqueue(1)
        self.assertEqual(self.queue.dequeue(), 0)
        self.assertEqual(self.queue.dequeue(), 1)
        with self.assertRaises(IndexError):
            self.queue.dequeue()

if __name__ == '__main__':
    unittest.main()
