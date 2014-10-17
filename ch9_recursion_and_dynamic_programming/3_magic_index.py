import unittest


def magic_index(array, low, high):
    """Returns a magic index in the sorted array of unique elements."""
    if low > high:
        return None
    mid = (low + high) // 2
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return magic_index(array, low, mid - 1)
    else:
        return magic_index(array, mid + 1, high)

def magic_index_dup(array, low, high):
    """Returns a magic index in an sorted array which may contain 
    duplicated elements. Returns None if no such element exists."""
    if low > high:
        return None
    mid = (low + high) // 2
    if array[mid] == mid:
        return mid
    left = magic_index_dup(array, low, min(mid - 1, array[mid]))
    if left:
        return left
    right = magic_index_dup(array, max(mid + 1, array[mid]), high)
    if right:
        return right
    return None
    
class MagicIndexTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_magic_index_non_exists(self):
        array = [-1, 2, 3, 5, 10, 11]
        self.assertEqual(None, magic_index(array, 0, 5))

    def test_magic_index_exists_simple(self):
        array = [0]
        self.assertEqual(0, magic_index(array, 0, 0))

    def test_magic_index_exists_multiple(self):
        array = [0, 1, 2]
        self.assertEqual(1, magic_index(array, 0, 2))

    def test_magic_index_exists_left(self):
        array = [-1, 1, 3, 5, 10, 11]
        self.assertEqual(1, magic_index(array, 0, 5))

    def test_magic_index_exists_right(self):
        array = [-1, 0, 1, 2, 3, 5]
        self.assertEqual(5, magic_index(array, 0, 5))

    def test_magic_index_exists_another(self):
        array = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
        self.assertEqual(7, magic_index(array, 0, 10))

    def test_magic_index_dup_non_exists(self):
        array = [5, 5, 6]
        self.assertEqual(None, magic_index_dup(array, 0, 2))

    def test_magic_index_dup_exists(self):
        array = [1, 1, 1, 4, 5, 5]
        self.assertEqual(1, magic_index_dup(array, 0, 5))

    def test_magic_index_dup_exists_another(self):
        array = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]
        self.assertEqual(2, magic_index_dup(array, 0, 10))

if __name__ == '__main__':
    unittest.main()
