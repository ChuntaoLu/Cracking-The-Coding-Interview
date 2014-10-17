import unittest
import random
from fractions import Fraction
from collections import defaultdict


def line_with_most_points(points):
    """Return the line with most points in a given points list."""
    table = defaultdict(int)
    num = len(points)
    for i in range(num):
        for j in range(i + 1, num):
            line = compute_line(points[i], points[j])
            table[line] += 1
    return max(table, key=lambda x: table[x])

def compute_line(x, y):
    """Compute the line between two points, return a tuple of slope and
    y axis intercept.
    
    If line is vertical, return a tuple of 'inf' and x axis intercept.
    """
    if x[0] == y[0]:
        return 'inf', x[0]
    slope = Fraction((y[1] - x[1]), (y[0] - x[0]))
    intercept = x[1] - slope * x[0]
    return slope, intercept
    
    
class LineWithMostPointsTest(unittest.TestCase):
    def setUp(self):
        rint = random.randint
        self.points = [(rint(0,100), rint(0,100)) for _ in range(10)]
        self.ponits = list(set(self.points))

    def test_normal(self):
        self.points.extend([(1, 1), (2, 2), (3, 3), (4, 4)])
        self.assertEqual(line_with_most_points(self.points), (1, 0))

    def test_vertical(self):
        self.points.extend([(1, 1), (2, 1), (3, 1), (4, 1)])
        self.assertEqual(line_with_most_points(self.points), (0, 1))

    def test_horizontal(self):
        self.points.extend([(2, 1), (2, 2), (2, 3), (2, 4)])
        self.assertEqual(line_with_most_points(self.points), ('inf', 2))

if __name__ == '__main__':
    unittest.main()
