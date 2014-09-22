import unittest


def num_of_diff_bits(x, y):
    """Return the number of different bits between x and y."""
    num = x ^ y
    counter = 0
    #while num:
        #counter += num & 1
        #num >>= 1
    while num:
        # clear the right most '1' bit
        num = num & (num - 1)
        counter += 1
    return counter

class NumOfDiffBitsTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_num_of_diff_bits(self):
        a, b, c = 0b11111, 0b1110, 0
        self.assertEqual(num_of_diff_bits(a, a), 0)
        self.assertEqual(num_of_diff_bits(a, b), 2)
        self.assertEqual(num_of_diff_bits(a, c), 5)

if __name__ == '__main__':
    unittest.main()
