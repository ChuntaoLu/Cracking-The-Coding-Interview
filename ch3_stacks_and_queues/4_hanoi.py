import unittest

class Stack(list):
    def __init__(self, *args, name):
        list.__init__(self, *args)
        self.name = name

    push = list.append

def hanoi(left, mid, right, n):
    if n == 1:
        disk = left.pop()
        right.push(disk)
        print('Moving {} from {} to {}'.format(disk, left.name, right.name))
        return
    hanoi(left, right, mid, n - 1)
    disk = left.pop()
    right.push(disk)
    print('Moving {} from {} to {}'.format(disk, left.name, right.name))
    hanoi(mid, left, right, n - 1)

class HanoiTest(unittest.TestCase):
    def setUp(self):
        self.stack1 = Stack(range(3, 0, -1), name='left')
        self.stack2 = Stack(name='mid')
        self.stack3 = Stack(name='right')

    def test_description(self):
        old = self.stack1[:]
        hanoi(self.stack1, self.stack2, self.stack3, len(self.stack1))
        self.assertEqual(self.stack1, [])
        self.assertEqual(self.stack2, [])
        self.assertEqual(self.stack3, old)

if __name__ == '__main__':
    unittest.main()
