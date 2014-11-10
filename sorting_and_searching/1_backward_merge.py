import unittest
from random import randint


def backward_merge(a, b):
    """a has enough buffer to hold b at the end so merge a and b backwards."""
    i = len(b) - 1
    j = len(a) - len(b) - 1
    end = len(a) - 1
    while i > -1:
        if j > -1 and a[j] > b[i]:
            a[end] = a[j]
            j -= 1
        else:
            a[end] = b[i]
            i -= 1
        end -= 1

class TestBackwardMerge(unittest.TestCase): 
    def test_backward_merge(self):
        for _ in range(50):
            a = [randint(0, 1000000) for _ in range(1000)]
            a.sort()
            a += [None] * 50
            b = [randint(0, 1000000) for _ in range(50)]
            b.sort()
            to_match = sorted(a[:-50] + b)
            backward_merge(a, b)
            self.assertEqual(to_match, a)

if __name__ == '__main__':
    unittest.main()
