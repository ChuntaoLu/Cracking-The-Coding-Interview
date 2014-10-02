import unittest


def multiply(x, y):
    out = 0
    for _ in range(abs(y)):
        out += x
    return out if y > 0 else negate(out)

def subtract(x, y):
    return x + negate(y)

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError

    out = 0
    abs_x, abs_y = abs(x), abs(y)
    while multiply(out + 1, abs_y) <= abs_x:
        out += 1

    if x > 0 and y > 0 or x < 0 and y < 0:
        return out
    else:
        return negate(out)

def negate(x):
    out = 0
    unit = -1 if x > 0 else 1
    while x != 0:
        out += unit
        x += unit
    return out

class OperationsByAddTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_multiply(self):
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(0, -5), 0)
        self.assertEqual(multiply(4, 5), 20)
        self.assertEqual(multiply(-4, 5), -20)

    def test_subtract(self):
        self.assertEqual(subtract(4, 4), 0)
        self.assertEqual(subtract(4, 3), 1)
        self.assertEqual(subtract(4, 5), -1)
        self.assertEqual(subtract(4, -5), 9)

    def test_divide(self):
        self.assertEqual(divide(4, 5), 0)
        self.assertEqual(divide(4, 4), 1)
        self.assertEqual(divide(4, 3), 1)
        self.assertEqual(divide(4, 2), 2)
        self.assertEqual(divide(4, 1), 4)
        self.assertEqual(divide(4, -1), -4)
        self.assertEqual(divide(4, -2), -2)
        self.assertEqual(divide(4, -3), -1)
        self.assertEqual(divide(4, -4), -1)
        self.assertEqual(divide(4, -5), 0)
        with self.assertRaises(ZeroDivisionError):
            divide(4, 0)

if __name__ == '__main__':
    unittest.main()
