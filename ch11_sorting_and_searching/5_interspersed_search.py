import unittest


def interspersed_search(array, elt):
    return _interspersed_search(array, elt, 0, len(array) - 1)

def _interspersed_search(array, elt, low, high):
    """Binary search with interspersed empty strings."""
    if low > high:
        return None
    mid = (low + high) // 2
    _mid = mid
    while mid > -1 and array[mid] == '':
        mid -= 1
    if mid == -1:
        return _interspersed_search(array, elt, _mid + 1, high)
    if array[mid] == elt:
        return mid
    elif array[mid] > elt:
        return _interspersed_search(array, elt, low, mid - 1)
    else:
        return _interspersed_search(array, elt, _mid + 1, high)

class InterspersedSearchTest(unittest.TestCase):
    def setUp(self):
        self.array = ['', 'app', '', 'ball', '', '', '', 'get']

    def test_non_exist(self):
        self.assertEqual(None, interspersed_search(self.array, 'ad'))

    def test_head(self):
        self.assertEqual(1, interspersed_search(self.array, 'app'))

    def test_mid(self):
        self.assertEqual(3, interspersed_search(self.array, 'ball'))

    def test_mid(self):
        self.assertEqual(7, interspersed_search(self.array, 'get'))

if __name__ == '__main__':
    unittest.main()
