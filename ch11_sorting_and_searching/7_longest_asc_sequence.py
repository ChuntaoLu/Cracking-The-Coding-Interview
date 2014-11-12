import unittest

def longest_asc_sequence(array):
    """Returns the longest ascending sequence in an array.
    Each element in the array is a tuple, the next tuple has to
    be bigger in both positions."""
    sorted_array = sorted(array, key=lambda x: x[0])
    return max(asc_sequences(sorted_array), key=len)

def asc_sequences(array):
    """Returns a list of longest ascending sequences that are ended with
    each element in the array."""
    if not array:
        return []
    seqs = asc_sequences(array[:-1])
    options = [i for i in seqs if i[-1][1] < array[-1][1]]
    if options:
        seqs.append(max(options, key=len) + [array[-1]])
    else:
        seqs.append([array[-1]])
    return seqs
    

class LongestAscSequenceTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_description(self):
        array = [(5, 12), (1, 7), (0, 13), (4, 11), (2, 14), (3, 10)]
        self.assertEqual([(1, 7), (3, 10), (4, 11), (5, 12)], longest_asc_sequence(array))

if __name__ == '__main__':
    unittest.main()
