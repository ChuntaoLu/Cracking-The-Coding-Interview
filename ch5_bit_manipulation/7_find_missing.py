import unittest


def find_missing(array):
    """Find the missing number of an array which contains 0 to n."""
    length = len(array)
    last = 1
    for index in range(0, length):
        current = array[index] & 1
        if current == last:
            return index
        last = current
    return length

    
class FindMissingTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_find_missing(self):
        a = [1]
        self.assertEqual(find_missing(a), 0)
        a = [0]
        self.assertEqual(find_missing(a), 1)
        a = [0, 1, 2, 4, 5, 6]
        self.assertEqual(find_missing(a), 3)
        a = [1, 2, 3, 4, 5, 6]
        self.assertEqual(find_missing(a), 0)
        a = [0, 1, 2, 3, 4, 5]
        self.assertEqual(find_missing(a), 6)

if __name__ == '__main__':
    unittest.main()
