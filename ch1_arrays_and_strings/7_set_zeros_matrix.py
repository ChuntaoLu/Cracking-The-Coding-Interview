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

def print_matrix(m):
    for row in m:
        print row

def main():
    arrays = []
    arrays.append([[1, 0]])
    arrays.append([[1, 2]])
    arrays.append([[1, 2], [3, 4]])
    arrays.append([[1, 0], [3, 4]])
    arrays.append([[1, 0, 2], [3, 4, 5]])
    arrays.append([[1, 0, 2], [3, 4, 5], [0, 3, 8]])
    for a in arrays:
        print 'Before:'
        print_matrix(a)
        print 'After: '
        set_zeros(a)
        print_matrix(a)
        print '\n'

if __name__ == '__main__':
    main()
