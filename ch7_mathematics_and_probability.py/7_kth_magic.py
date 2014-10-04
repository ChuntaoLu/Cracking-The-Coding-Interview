import unittest
from collections import deque


def kth_magic(n):
    """Returns the kth number that is a multiply of only 3, 5, ,7."""
    current_min = 1
    q3, q5, q7 = deque([3]), deque([5]), deque([7])
    while n:
        h3, h5, h7 = q3[0], q5[0], q7[0]
        current_min = min(h3, h5, h7)
        if current_min == h3:
            q3.popleft()
            q3.append(current_min * 3)
            q5.append(current_min * 5)
        elif current_min == h5:
            q5.popleft()
            q5.append(current_min * 5)
        else:
            q7.popleft()
        q7.append(current_min * 7)
        n -= 1
    return current_min

class KthMagicTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_kth_magic(self):
        self.assertEqual(kth_magic(0), 1)
        self.assertEqual(kth_magic(1), 3)
        self.assertEqual(kth_magic(3), 7)
        self.assertEqual(kth_magic(8), 27)

if __name__ == '__main__':
    unittest.main()
