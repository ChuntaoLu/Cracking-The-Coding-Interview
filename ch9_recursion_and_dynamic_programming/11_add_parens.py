import unittest


def _parens(exp, boolean, start, end, cache):
    """Recursively add parens to make the exp evlautes to boolean.
    
    Returns the number of ways to add parens.
    Iterate through the exp operators and treat each operator as the
    only operator such that the left and right part are grouped by parens.
    Based on the operator make recursive calls to the left and right parts
    and cache the result because a lot of calls have same parameters.

    Base case is when the exp is only one character.
    """
    if (boolean, start, end) in cache:
        return cache[(boolean, start, end)]

    if start == end: 
        if exp[end] == '1' and boolean:
            return 1
        if exp[end] == '0' and not boolean:
            return 1
        return 0

    c = 0
    if boolean:
        for i in range(start + 1, end, 2):
            if exp[i] == '|':
                c += _parens(exp, True, start, i - 1, cache) * _parens(exp, False, i + 1, end, cache)
                c += _parens(exp, False, start, i - 1, cache) * _parens(exp, True, i + 1, end, cache)
                c += _parens(exp, True, start, i - 1, cache) * _parens(exp, True, i + 1, end, cache)
            if exp[i] == '&':
                c += _parens(exp, True, start, i - 1, cache) * _parens(exp, True, i + 1, end, cache)
            if exp[i] == '^':
                c += _parens(exp, True, start, i - 1, cache) * _parens(exp, False, i + 1, end, cache)
                c += _parens(exp, False, start, i - 1, cache) * _parens(exp, True, i + 1, end, cache)
    else:
        for i in range(start + 1, end, 2):
            if exp[i] == '|':
                c += _parens(exp, False, start, i - 1, cache) * _parens(exp, False, i + 1, end, cache)
            if exp[i] == '&':
                c += _parens(exp, True, start, i - 1, cache) * _parens(exp, False, i + 1, end, cache)
                c += _parens(exp, False, start, i - 1, cache) * _parens(exp, True, i + 1, end, cache)
                c += _parens(exp, False, start, i - 1, cache) * _parens(exp, False, i + 1, end, cache)
            if exp[i] == '^':
                c += _parens(exp, True, start, i - 1, cache) * _parens(exp, True, i + 1, end, cache)
                c += _parens(exp, False, start, i - 1, cache) * _parens(exp, False, i + 1, end, cache)
    cache[(boolean, start, end)] = c
    return c

def add_parens(exp, boolean):
    return _parens(exp, boolean, 0, len(exp) - 1, {})
    
class AddParensTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_parens_single(self):
        self.assertEqual(1, add_parens('1', True))
        self.assertEqual(0, add_parens('1', False))
        self.assertEqual(0, add_parens('0', True))
        self.assertEqual(1, add_parens('0', False))
    
    def test_add_parens_simple(self):
        self.assertEqual(1, add_parens('1^0', True))
        self.assertEqual(0, add_parens('1^0', False))
        self.assertEqual(1, add_parens('1|0', True))
        self.assertEqual(0, add_parens('1|0', False))
        self.assertEqual(0, add_parens('1&0', True))
        self.assertEqual(1, add_parens('1&0', False))

    def test_add_parens(self):
        self.assertEqual(2, add_parens('1^0|0|1', False))

if __name__ == '__main__':
    unittest.main()
