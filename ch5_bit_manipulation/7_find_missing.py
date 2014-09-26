import unittest
from random import shuffle


def find_missing(array):
    """Find the missing number of an array which contains 0 to n."""
    return _find_missing(array, 0)

def _find_missing(array, ith):
    """Recursively find each digit of the missing number in an array.
    
    At any ith digit, when no number is missing, no matter the array
    is odd or even, number of zeors always >= than number of ones.

    At ith digit, if number of zeros <= number of ones, it means the
    missing number's ith digit is zero, other wise one.

    When array is empty, it means all higher digits are zeros.
    """
    if not array:
        return 0

    zeros, ones = [], []
    for elt in array:
        if _ith_digit(elt, ith):
            ones.append(elt)
        else:
            zeros.append(elt)

    if len(zeros) <= len(ones):
        n = _find_missing(zeros, ith + 1)
        out = (n << 1) | 0
    else:
        n = _find_missing(ones, ith + 1)
        out = (n << 1) | 1
    return out
    

def _ith_digit(n, i):
    """Return the ith digit of number n."""    
    return (1 << i) & n
    
class FindMissingTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_find_missing(self):
        a = [1]
        self.assertEqual(find_missing(a), 0)
        a = [0]
        self.assertEqual(find_missing(a), 1)
        a = [0, 1, 2, 4, 5, 6]
        shuffle(a)
        self.assertEqual(find_missing(a), 3)
        a = [1, 2, 3, 4, 5, 6]
        shuffle(a)
        self.assertEqual(find_missing(a), 0)
        a = [0, 1, 2, 3, 4, 5]
        shuffle(a)
        self.assertEqual(find_missing(a), 6)
        a = list(range(10000))
        shuffle(a)
        x = a.pop()
        self.assertEqual(find_missing(a), x)

if __name__ == '__main__':
    unittest.main()
