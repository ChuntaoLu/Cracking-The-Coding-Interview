import unittest


def are_all_chars_unique(strr):
    """without using additional data structures"""
    for index in range(len(strr) - 1):
        c = strr[index]
        if _contains(strr[index + 1:], c):
            return False
    return True

def _contains(s, c):
    for i in s:
        if c == i:
            return True
    return False

class AllUniqueCharsTest(unittest.TestCase):
    def test_empty(self):
        self.assertTrue(are_all_chars_unique(''))

    def test_non_empty(self):
        self.assertTrue(are_all_chars_unique('a'))
        self.assertTrue(are_all_chars_unique('abcdef'))
        self.assertFalse(are_all_chars_unique('abcdabd'))

if __name__ == '__main__':
    unittest.main()
