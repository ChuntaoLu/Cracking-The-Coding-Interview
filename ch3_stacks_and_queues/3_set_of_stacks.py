import unittest


class EmptyStackError(Exception):
    pass

class FullStackError(Exception):
    pass

class Node(object):
    """Node for linked list."""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack(object):
    """Stack with capacity implemented with linked list."""
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.top = None
        self.bottom = None

    def pop(self):
        """Pop item off the stack, raises exception when empty."""
        if self.top is None:
            raise EmptyStackError('pop from empty stack')
        data = self.top.data
        if self.bottom is self.top:
            self.bottom = None
        self.top = self.top.next
        self.size -= 1
        return data

    def push(self, data):
        """Push item onto stack, raises exception when full."""
        if self.size == self.capacity:
            raise FullStackError('stack is full')
        node = Node(data, self.top)
        self.top = node
        if self.bottom is None:
            self.bottom = node
        self.size += 1

    def remove_bottom(self):
        if self.bottom is None:
            raise EmptyStackError('remove bottom from empty stack')
        bottom = self.bottom
        if self.bottom is self.top:
            self.top = self.bottom = None
        else:
            current = self.top
            while current.next.next:
                current = current.next
            self.bottom = current
            current.next = None
        self.size -= 1
        return bottom.data

    def __str__(self):
        elts = []
        current = self.top
        while current:
            elts.append(str(current.data))
            current = current.next
        elts.extend(['_'] * (self.capacity - self.size))
        return '[{}]'.format(', '.join(elts[::-1]))

class SetOfStacks(object):
    """SetOfStacks implemented with a linked list of stacks with capacity."""
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []
    
    def pop(self):
        """Pop item off the stacks, a stack is poped when empty."""
        try:
            return self.stacks[-1].pop()
        except IndexError:
            raise EmptyStackError('pop from empty stack')
        except EmptyStackError:
            self.stacks.pop()
            return self.pop()

    def pop_at(self, index):
        """Pop item off the stack at specific index, raise error when index out of range."""
        if index >= len(self.stacks):
            raise IndexError('index is out of range')
        return self.stacks[index].pop()

    def push(self, value):
        """Push item onto stack, create a new stack when current full."""
        try:
            self.stacks[-1].push(value)
        except (IndexError, FullStackError):
            stack = Stack(self.capacity)
            stack.push(value)
            self.stacks.append(stack)

    def __str__(self):
        return '<{}>'.format(', '.join(map(str, self.stacks)))

class SetOfStacksRollOver(SetOfStacks):
    """SetofStacks that support roll-over pop_at method."""
    def pop_at(self, index):
        """Push the bottom item from next stack to current stack when stack at index pops."""
        if index >= len(self.stacks):
            raise IndexError('index is out of range')
        data = self.stacks[index].pop()
        for i in range(index, len(self.stacks) - 1):
            roll_over = self.stacks[i + 1].remove_bottom()
            self.stacks[i].push(roll_over)
        if self.stacks[-1].size == 0:
            self.stacks.pop()
        return data

class SetOfStacksTest(unittest.TestCase):
    def setUp(self):
        self.s1 = SetOfStacks(2)
        self.s2 = SetOfStacksRollOver(2)
        for i in range(4):
            self.s1.push(i)
            self.s2.push(i)

    def test_set_of_stacks(self):
        self.assertEqual(self.s1.pop(), 3)
        self.assertEqual(self.s1.pop(), 2)
        self.assertEqual(self.s1.pop(), 1)

    def test_set_of_stacks_roll_over(self):
        self.assertEqual(self.s2.pop(), 3)
        self.assertEqual(self.s2.pop(), 2)
        self.assertEqual(self.s2.pop(), 1)

    def test_pop_at(self):
        self.assertRaises(IndexError, self.s1.pop_at, 2)
        self.assertEqual(self.s1.pop_at(1), 3)
        self.assertEqual(self.s1.pop_at(0), 1)
        self.assertEqual(self.s1.pop_at(0), 0)
        self.assertRaises(EmptyStackError, self.s1.pop_at, 0)

    def test_pop_at_roll_over(self):
        self.assertRaises(IndexError, self.s2.pop_at, 2)
        self.assertEqual(self.s2.pop_at(1), 3)
        self.assertEqual(self.s2.pop_at(0), 1)
        self.assertEqual(self.s2.pop_at(0), 2)
        self.assertRaises(IndexError, self.s2.pop_at, 1)

if __name__ == '__main__':
    unittest.main()
