import unittest


def string_permutations(s):
    if len(s) <= 1:
        return {s}
    out = set()
    last = s[-1]
    for i in string_permutations(s[:-1]):
        out |= {i[:j] + last + i[j:] for j in range(len(i) + 1)}    
    return out

class StringPermutationTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_string_permutations_length_0(self):
        self.assertEqual({''}, string_permutations(''))

    def test_string_permutations_length_1(self):
        self.assertEqual({'x'}, string_permutations('x'))

    def test_string_permutations_length_2(self):
        self.assertEqual({'xy', 'yx'}, string_permutations('xy'))

    def test_string_permutations_length_3(self):
        self.assertEqual({'xyz', 'yzx', 'zxy', 'xzy', 'yxz', 'zyx'}, string_permutations('xyz'))

    def test_string_permutations_length_3_with_duplicate(self):
        self.assertEqual({'xyx', 'xxy', 'yxx'}, string_permutations('xyx'))

    def test_string_permutations_long(self):
        from itertools import permutations
        _str = 'longstring'
        result = {''.join(i) for i in permutations(_str)}
        self.assertEqual(result, string_permutations(_str))

if __name__ == '__main__':
    unittest.main()
