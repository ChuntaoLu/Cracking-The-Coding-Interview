import unittest


def right_rotate(array):
    """
    Assume N-by-N matrix is represented by 2-d array
    """
    n = len(array)
    rotated = [[0 for _ in range(n)] for _ in range(n)]
    for row in range(n):
        for col in range(n):
            rotated[col][n - 1 - row] = array[row][col] 
    return rotated

def right_rotate_inplace(array):
    """
    Assume N-by-N matrix is represented by 2-d array
    """
    n = len(array)
    for layer in range(n / 2):
        start = layer
        end = n - 1 - layer
        for i in range(start, end):
            offset = i - start
            tmp = array[start][i]

            # left -> top
            array[start][i] = array[end - offset][start]

            # bottom -> left
            array[end - offset][start] = array[end][end - offset]

            # right -> bottom
            array[end][end - offset] = array[i][end]

            # top -> right
            array[i][end] = tmp

class RightRotateTest(unittest.TestCase):
    def test_right_rotate(self):
        self.assertEqual([[1]], right_rotate([[1]]))
        self.assertEqual([[3, 1], [4, 2]], right_rotate([[1, 2], [3, 4]]))
        self.assertEqual([[7, 4, 1], [8, 5, 2], [9, 6, 3]],
                right_rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    def test_right_rotate_inplace(self):
        array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        right_rotate_inplace(array)
        self.assertEqual([[7, 4, 1], [8, 5, 2], [9, 6, 3]], array)

if __name__ == '__main__':
    unittest.main()
