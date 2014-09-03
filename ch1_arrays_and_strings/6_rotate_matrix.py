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


def print_matrix(array):
    for row in array:
        print row


def main():
    arrays = []
    arrays.append([[1]])
    arrays.append([[1, 2], [3, 4]])
    arrays.append([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    for a in arrays:
        print 'Before:'
        print_matrix(a)
        print 'After right_rotate:'
        print_matrix(right_rotate(a))
        print 'After right_rotate_inplace:'
        right_rotate_inplace(a)
        print_matrix(a)
        print '\n'

if __name__ == '__main__':
    main()
