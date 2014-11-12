import unittest


def search_sorted_matrix(matrix, elt):
    """Search for elt in matrix whose rows and cols are all sorted."""
    row = 0
    col = len(matrix) - 1
    while col > -1 and row < len(matrix):
        if matrix[row][col] == elt:
            return row, col
        if matrix[row][col] > elt:
            col -= 1
        else:
            row += 1
    return None

class SearchMatrixTest(unittest.TestCase):
    def setUp(self):
        self.matrix = [[15, 20, 70, 85], [20, 35, 80, 95], [30, 55, 95, 105], [40, 80, 100, 120]]

    def test_general(self):
        self.assertEqual((2, 1), search_sorted_matrix(self.matrix, 55))
        self.assertEqual((0, 1), search_sorted_matrix(self.matrix, 20))

    def test_non_exist(self):
        self.assertEqual(None, search_sorted_matrix(self.matrix, 56))

    def test_corner(self):
        self.assertEqual((0, 3), search_sorted_matrix(self.matrix, 85))
        self.assertEqual((0, 0), search_sorted_matrix(self.matrix, 15))
        self.assertEqual((3, 0), search_sorted_matrix(self.matrix, 40))
        self.assertEqual((3, 3), search_sorted_matrix(self.matrix, 120))

if __name__ == '__main__':
    unittest.main()
