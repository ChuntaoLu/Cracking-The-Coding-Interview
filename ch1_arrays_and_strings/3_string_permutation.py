import unittest


def is_permutation(s1, s2):
    """O(n), assuming chars in string are ascii"""
    count = [0 for _ in range(256)]
    for i in s1:
        count[ord(i)] += 1

    for i in s2:
        count[ord(i)] -= 1
        if count[ord(i)] < 0:
            return False
    return True

class IsPermutationTest(unittest.TestCase):
    def test_is_permutation(self):
        self.assertTrue(is_permutation('this', 'isht'))
        self.assertTrue(is_permutation('this ', 'i sht'))
        self.assertFalse(is_permutation('th', 'i sht'))
        self.assertTrue(is_permutation('', ''))

if __name__ == '__main__':
    unittest.main()
