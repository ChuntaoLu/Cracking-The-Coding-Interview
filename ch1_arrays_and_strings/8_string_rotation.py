import unittest


def is_rotation(s1, s2):
    s = s1 + s1
    if len(s1) == len(s2):
        return is_substring(s, s2)
    return False

def is_substring(s1, s2):
    return s2 in s1

class IsRotationTest(unittest.TestCase):
    def setUp(self):
        self.s = 'waterbottle'

    def test_true(self):
        self.assertFalse(is_rotation('', self.s))
        self.assertFalse(is_rotation('aterbottle', self.s))
        self.assertFalse(is_rotation('this_must_not_be', self.s))
    
    def test_false(self):
        self.assertTrue(is_rotation('aterbottlew', self.s))
        self.assertTrue(is_rotation('ottlewaterb', self.s))

if __name__ == '__main__':
    unittest.main()
