import unittest


def bit_insert(n, m, i, j):
    left = (~0) << (j + 1)
    right = 1 << i - 1
    mask = left | right
    return (n & mask) | (m << i)
    
class BitInsertTest(unittest.TestCase):
    def setUp(self):
        self.m = 0b10011

    def test_bit_insert_0(self):
        self.n = 0b10000000000
        self.assertEqual(bit_insert(self.n, self.m, 2, 6), 0b10001001100)

    def test_bit_insert_1(self):
        self.n = 0b10001101000
        self.assertEqual(bit_insert(self.n, self.m, 2, 6), 0b10001001100)

    def test_bit_insert_2(self):
        self.n = 0b10001001000
        self.assertEqual(bit_insert(self.n, self.m, 2, 6), 0b10001001100)

if __name__ == '__main__':
    unittest.main()
