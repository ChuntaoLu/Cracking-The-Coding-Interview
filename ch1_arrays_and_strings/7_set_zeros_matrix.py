import unittest


def set_zeros(array):
    """
    Assume M-by-N matrix is represented by 2-d array
    """
    m = len(array)
    n = len(array[0])
    rows, cols = set(), set()
    for r in range(m):
        for c in range(n):
            if array[r][c] == 0:
                rows.add(r)
                cols.add(c)

    for r in range(m):
        for c in range(n):
            if r in rows or c in cols:
                array[r][c] = 0

class SetZerosTest(unittest.TestCase):
    def test_non_zero(self):
        matrix = [[1, 2], [3, 4]]
        set_zeros(matrix)
        self.assertEqual(matrix, matrix)

    def test_has_zeros(self):
        matrix = [[1, 0], [3, 4]]
        set_zeros(matrix)
        self.assertEqual([[0, 0], [3, 0]], matrix)

    def test_has_zeros_2(self):
        matrix = [[1, 0, 2], [3, 4, 5], [0, 3, 8]]
        set_zeros(matrix)
        self.assertEqual([[0, 0, 0], [0, 0, 5], [0, 0, 0]], matrix)

if __name__ == '__main__':
    unittest.main()
