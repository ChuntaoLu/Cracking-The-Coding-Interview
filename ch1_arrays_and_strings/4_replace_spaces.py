import re
import unittest


def replace_spaces_regex(s):
    """using regular expression"""
    return re.sub('\s', '20%', s.strip())

def replace_spaces_inplace(s):
    """
    without using regex.
    Assume 's' is a char array, replace spaces in place.
    construct string by char array, and iterating backwards.
    """
    while s and s[-1] == ' ':
        s.pop()
    length = len(s)
    space_count = sum(1 for i in s if i == ' ')
    new_end = length + 2 * space_count
    s[length: new_end] = [''] * 2 * space_count
    for index in range(length - 1, -1, -1):
        if s[index] == ' ':
            s[new_end - 3: new_end] = list('20%')
            new_end -= 3
        else:
            s[new_end - 1] = s[index]
            new_end -= 1

class ReplaceSpacesTest(unittest.TestCase):
    def setUp(self):
        self.s = "Mr John  Smith   "
        self.expected = "Mr20%John20%20%Smith"

    def test_replace_space_regex(self):
        self.assertEqual(self.expected, replace_spaces_regex(self.s))

    def test_replace_space_inplace(self):
        chars = list(self.s)
        replace_spaces_inplace(chars)
        self.assertEqual(self.expected, ''.join(chars))

if __name__ == '__main__':
    unittest.main()
