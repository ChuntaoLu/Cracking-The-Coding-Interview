import unittest
from string import ascii_letters
from random import choice, randint, shuffle
from collections import defaultdict
from itertools import chain


def sort_anagram(array):
    """Sort the array of strings based on alphabetic order."""
    return array.sort(key=lambda x: sorted(x))

def sort_anagram_hash(array):
    """Group the strings of same sorted order using hash, then
    convert back to list."""
    _dict = defaultdict(list)
    for word in array:
        _dict[''.join(sorted(word))].append(word)
    return list(chain.from_iterable(_dict.values()))

def _make_word():
    """Helper to make a random word."""
    return ''.join(choice(ascii_letters) for _ in range(1, randint(2, 7)))
    
def _make_anagram_pairs():
    """Helper to create a pair of anagrams."""
    word = _make_word()
    chars = list(word)
    shuffle(chars)
    return word, ''.join(chars)

class TestSortAnagram(unittest.TestCase):
    def setUp(self):
        left = list(chain.from_iterable(_make_anagram_pairs() for _ in range(10)))
        right = [_make_word() for _ in range(10)]
        self.array = left + right
        shuffle(self.array)

    def test_sort_anagram(self):
        sort_anagram(self.array)
        print(self.array)

    def test_sort_anagram_hash(self):
        print(sort_anagram_hash(self.array))

if __name__ == '__main__':
    unittest.main()
