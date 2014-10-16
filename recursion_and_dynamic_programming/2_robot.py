import unittest


def robot(x, y):
    """Returns number of ways a robot can reach (x, y) from (0, 0).
    
    (0, 0) is at upper left corner while (x, y) is at bottom right.
    robot can only move right and down.
    """
    cache = {(0, 0): 1}
    def _robot(m, n):
        if m < 0 or n < 0:
            return 0
        if (m, n) not in cache:
            cache[(m, n)] = _robot(m - 1, n) + _robot(m, n - 1)
        return cache[(m, n)]
    return _robot(x, y)

def path_finder(x, y, grid):
    """Returns path from (0, 0) to (x, y) when grid has unreachable spots."""
    parent = {}
    current = (0, 0)
    stack = [current]
    while stack:
        _x, _y = stack.pop()
        if (_x, _y) == (x, y):
            break
        if _x < x and grid[_x + 1][_y]:
            stack.append((_x + 1, _y))
            parent[(_x + 1, _y)] = (_x, _y)
        if _y < y and grid[_x][_y + 1]:
            stack.append((_x, _y + 1))
            parent[(_x, _y + 1)] = (_x, _y)
    p = (x, y)
    path = [(x, y)]
    while p != (0, 0):
        p = parent[p]
        path.append(p)
    return path[::-1]

def path_finder_recur(start, target, grid):
    if start == target:
        return True
    x, y = target
    _x, _y = start
    if _y < y and grid[_x][_y + 1]:
        if path_finder_recur((_x, _y + 1), target, grid):
            print(_x, _y + 1)
            return True
    if _x < x and grid[_x + 1][_y]:
        if path_finder_recur((_x + 1, _y), target, grid):
            print(_x + 1, _y)
            return True
    
class RobotTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_robot(self):
        self.assertEqual(1, robot(0, 0))
        self.assertEqual(1, robot(0, 1))
        self.assertEqual(1, robot(1, 0))
        self.assertEqual(2, robot(1, 1))
        self.assertEqual(6, robot(2, 2))

    def test_path_finder_1(self):
        grid = [[1, 1], [0, 1]]
        self.assertEqual([(0, 0), (0, 1), (1, 1)], path_finder(1, 1, grid))

    def test_path_finder_3(self):
        grid = [[1] * 4 for _ in range(4)]
        grid[1][1] = 0
        grid[2][2] = 0
        grid[1][3] = 0
        path = [(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (3, 2), (3, 3)]
        self.assertEqual(path, path_finder(3, 3, grid))

if __name__ == '__main__':
    unittest.main()
