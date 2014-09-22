import unittest


def next_smallest_and_biggest(x):
    if x == 0:
        return None, None
    return _next_smallest(x), _next_biggest(x)

def _next_smallest(n):
    """Find the next smallest number that is bigger than n and has the same
    number of ones as n.

    Flip the first 0 that has at leat a 1 to its right, clear all its right
    bits and add right amount of ones to the right most.
    
    101 -> 110
    1100 -> 10001
    101100 -> 110001
    """

    m = n
    num_trailing_zeros = 0
    num_right_ones = 0

    while (m & 1) == 0:
        num_trailing_zeros += 1
        m >>= 1

    while (m & 1) == 1:
        num_right_ones += 1
        m >>= 1

    if num_trailing_zeros + num_right_ones > 31:
        return

    # filp the 0 and clear all right bits
    n += 1 << num_trailing_zeros
    # add back right number of 1s
    n += (1 << (num_right_ones - 1)) - 1
    return n

def _next_biggest(n):
    """Find the biggest number that is smaller than n and has the same
    number of ones as n.
    
    Flip the first 1 that has at least a 0 to its right, clear all its 
    right bits and add back the right amount of 1s.

    101 -> 11
    1100 -> 1010
    101100 -> 101010
    111 -> None
    """
    m = n
    num_trailing_ones = 0
    num_right_zeros = 0

    while (m & 1) == 1:
        num_trailing_ones += 1
        m >>= 1

    # all ones only, no number is smaller and has same amount of ones
    if m == 0:
        return

    while (m & 1) == 0:
        num_right_zeros += 1
        m >>= 1

    # flip the 0 and all right bits to 1
    n -= 1 << num_trailing_ones
    # remove right amout of ones
    n -= (1 << (num_right_zeros - 1)) -1
    return n

class NestSamllestAndBiggestTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_next_smallest_and_biggest(self):
        x = 0b0
        self.assertEqual(next_smallest_and_biggest(x), (None, None))
        x = 0b101
        self.assertEqual(next_smallest_and_biggest(x), (0b110, 0b11))
        x = 0b111
        self.assertEqual(next_smallest_and_biggest(x), (0b1011, None))
        x = 0b1100
        self.assertEqual(next_smallest_and_biggest(x), (0b10001, 0b1010))
        x = 0b101100
        self.assertEqual(next_smallest_and_biggest(x), (0b110001, 0b101010))

if __name__ == '__main__':
    unittest.main()
