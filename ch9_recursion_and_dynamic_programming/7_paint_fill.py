import unittest


def paint_fill(screen, x, y, original, to):
    """Paint the pixel at (x, y) and the ones next to it with same 
    color from orignal to to."""
    if x < 0 or x >= len(screen[0]) or y < 0 or y >= len(screen):
        return
    if screen[x][y] == original:
        screen[x][y] = to
        paint_fill(screen, x - 1, y, original, to)
        paint_fill(screen, x + 1, y, original, to)
        paint_fill(screen, x, y - 1, original, to)
        paint_fill(screen, x, y + 1, original, to)

class PaintFillTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_paint_fill_1(self):
        screen = [[1]]
        paint_fill(screen, 0, 0, 1, 2)
        self.assertEqual([[2]], screen)

    def test_paint_fill_2(self):
        screen = [[0, 1], [1, 0]]
        paint_fill(screen, 0, 1, 1, 2)
        self.assertEqual([[0, 2], [1, 0]], screen)

    def test_paint_fill_5(self):
        screen = [[None] * 5 for _ in range(5)]
        screen[0][3] = 1
        screen[1][3] = 1
        screen[2][2] = 1
        screen[2][3] = 1
        screen[3][1] = 1
        screen[3][2] = 1
        paint_fill(screen, 2, 2, 1, 2)
        after = [[None] * 5 for _ in range(5)]
        after[0][3] = 2
        after[1][3] = 2
        after[2][2] = 2
        after[2][3] = 2
        after[3][1] = 2
        after[3][2] = 2
        self.assertEqual(after, screen)

if __name__ == '__main__':
    unittest.main()
