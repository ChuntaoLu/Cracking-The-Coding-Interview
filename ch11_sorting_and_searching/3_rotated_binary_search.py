import unittest


def rotated_binary_search(array, elt):
    return _rotated_binary_search(array, elt, 0, len(array) - 1)
    
def _rotated_binary_search(array, elt, low, high):
    """No matter how many times the sorted array rotates, one side is
    strictly increasing. Decide the side to search based on mid value.
    Also need take duplicates into consideration."""
    if low > high:
        return None
    mid = (low + high) // 2
    if array[mid] == elt:
        return mid
    if array[low] < array[mid]:
        if array[low] <= elt <= array[mid]:
            return _rotated_binary_search(array, elt, low, mid - 1)
        else:
            return _rotated_binary_search(array, elt, mid + 1, high)
    elif array[mid] < array[low]:
        if array[mid] <= elt <= array[high]:
            return _rotated_binary_search(array, elt, mid + 1, high)
        else:
            return _rotated_binary_search(array, elt, low, mid - 1)
    else: # low to mid are all duplicates
        if array[high] != array[mid]:
            return _rotated_binary_search(array, elt, mid + 1, high)
        else: # search both sides
            left = _rotated_binary_search(array, elt, low, mid - 1)
            if left is None:
                return _rotated_binary_search(array, elt, mid + 1, high)
            else:
                return left

class RotatedBinarySearchTest(unittest.TestCase):
    def setUp(self):
        self.array = list(range(0, 10))

    def test_none_exist(self):
        self.assertEqual(None, rotated_binary_search(self.array, 20))

    def test_no_rotation(self):
        self.assertEqual(5, rotated_binary_search(self.array, 5))

    def test_left_increasing(self):
        self.array = list(range(3, 10)) + list(range(3))
        self.assertEqual(2, rotated_binary_search(self.array, 5))

    def test_right_increasing(self):
        self.array = list(range(7, 10)) + list(range(7))
        self.assertEqual(8, rotated_binary_search(self.array, 5))

    def test_duplicates_left(self):
        self.array = [2, 3, 4, 2, 2, 2, 2]
        self.assertEqual(1, rotated_binary_search(self.array, 3))

    def test_duplicates_right(self):
        self.array = [2, 2, 2, 2, 3, 4, 2]
        self.assertEqual(4, rotated_binary_search(self.array, 3))

if __name__ == '__main__':
    unittest.main()
