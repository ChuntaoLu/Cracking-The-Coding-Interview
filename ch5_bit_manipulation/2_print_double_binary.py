import unittest


def print_double(n):
    x = 0.5
    bits = ['.']
    while n:
        if n >= x:
            n -= x
            bits.append('1')
        else:
            bits.append('0')
        if len(bits) > 32:
            return 'ERROR'
        x /= 2
    return ''.join(bits)

class PrintDoubleTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_success(self):
        n = 0.1875
        self.assertEqual(print_double(n), '.0011')
        n = 0.5390625
        self.assertEqual(print_double(n), '.1000101')

    def test_error(self):
        n = 1 / 3
        self.assertEqual(print_double(n), 'ERROR')

if __name__ == '__main__':
    unittest.main()
