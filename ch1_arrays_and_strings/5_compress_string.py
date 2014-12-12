import unittest


def compress_string(s):
    can_compress = False
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] and s[i + 1] == s[i + 2]:
            can_compress = True
            break
    if not can_compress:
        return s

    count = 1
    last = s[0]
    compressed = ''
    for c in s[1:]:
        if c == last:
            count += 1
        else:
            compressed += last + str(count)
            last = c
            count = 1
    compressed += last + str(count)
    return compressed

class CompressStringTest(unittest.TestCase):
    def test_not_compressable(self):
        self.assertEqual('', compress_string(''))
        self.assertEqual('ab', compress_string('ab'))
        self.assertEqual('aab', compress_string('aab'))

    def test_compressable(self):
        self.assertEqual('a3b2', compress_string('aaabb'))
        self.assertEqual('a2b1c5a3', compress_string('aabcccccaaa'))

if __name__ == '__main__':
    unittest.main()
