import unittest


def swap_bits(n):
    """Swap the odd and even bits of an integer."""
    odd_mask = 0xaaaaaaaa
    even_mask = 0x55555555
    return ((n & odd_mask) >> 1) | ((n & even_mask) << 1)

class SwapBitsTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_swap_bits(self):
        self.assertEqual(swap_bits(0), 0)
        self.assertEqual(swap_bits(1), 0b10)
        self.assertEqual(swap_bits(0b10101010), 0b01010101)

if __name__ == '__main__':
    unittest.main()
