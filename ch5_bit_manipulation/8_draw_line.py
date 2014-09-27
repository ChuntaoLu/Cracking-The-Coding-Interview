import unittest


def draw_line(screen, width, x1, x2, y):
    """Draw horizontal line between x1 and x2 on the yth row of a screen.
    
    screen is in form of bytearray, and each bit corresponds to a pixel.
    """
    above = y * (width // 8)
    start = above + x1 // 8
    end = above + x2 // 8

    for index in range(start + 1, end):
        screen[index] = 0xff

    start_mask = 0xff >> (x1 % 8)
    screen[start] |= start_mask

    end_mask = 0xff >> ((x2 % 8) + 1)
    screen[end] = screen[end] - end_mask if screen[end] else 0xff - end_mask
    
class DrawLineTest(unittest.TestCase):
    def setUp(self):
        self.width = 80
        self.screen = bytearray([0] * 100)

    def test_draw_line_1(self):
        draw_line(self.screen, self.width, 0, 6, 0)
        self.assertEqual(self.screen, bytearray([0xfe] + [0] * 99))

    def test_draw_line_2(self):
        draw_line(self.screen, self.width, 0, 10, 0)
        self.assertEqual(self.screen, bytearray([0xff, 0xe0] + [0] * 98))

    def test_draw_line_3(self):
        draw_line(self.screen, self.width, 9, 10, 0)
        self.assertEqual(self.screen, bytearray([0, 0x60] + [0]* 98))

    def test_draw_line_4(self):
        draw_line(self.screen, self.width, 29, 57, 6)
        target = bytearray([0] * 63 + [0x07] + [0xff] * 3 + [0xc0] + [0] * 32)
        self.assertEqual(self.screen, target)

if __name__ == '__main__':
    unittest.main()
