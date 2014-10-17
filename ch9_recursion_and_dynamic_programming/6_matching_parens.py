import unittest


def matching_parens(num):
    """Returns a set of all num pairs of mataching parens."""
    out = set()
    _build_parens(out, 0, 0, num, '')
    return out

def _build_parens(_set, left, right, num, _str):
    """Build parens matching string position after position.
    
    Each position can be '(' or ')', make two recursive calls for the position.
    Once all parens are used up, add the built string to set.
    Keeping left parens not less than right parens makes sure parens match.
    """
    if left == right == num:
        _set.add(_str)
        return
    if left > num or left < right:
        return
    _build_parens(_set, left + 1, right, num, _str + '(')
    _build_parens(_set, left, right + 1, num, _str + ')')

class MatchingParensTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_matching_parens_1(self):
        self.assertEqual({'()'}, matching_parens(1))

    def test_matching_parens_2(self):
        self.assertEqual({'()()', '(())'}, matching_parens(2))

    def test_matching_parens_3(self):
        self.assertEqual({'(())()', '()(())', '(()())', '()()()', '((()))'}, matching_parens(3))

if __name__ == '__main__':
    unittest.main()
