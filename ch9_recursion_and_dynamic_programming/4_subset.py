import unittest


def subset(x):
    """Return a list of all subsets of a given set."""
    if x == set():
        return [x]
    y = list(x)
    set_list, last = subset(set(y[:-1])), y[-1]
    set_list_plus_last = [i | {last} for i in set_list]
    return set_list + set_list_plus_last

def subset_comb(x):
    """Returns all subsets of given set x, combinatorics approach."""
    _max = 2 ** len(x)
    _set = list(x)
    ret = []
    for i in range(_max):
        ret.append(subset_by_bits(i, _set))
    return ret

def subset_by_bits(num, x):
    """Return a subset of x based on the 1 digits in the binary form of x."""
    ret = set()
    count = len(x) - 1
    while num > 0:
        if num & 1 == 1:
            ret.add(x[count])
        num = num >> 1
        count -= 1
    return ret

class SubsetTest(unittest.TestCase):
    def to_frozen(self, set_list):
        return {frozenset(i) for i in set_list}

for name in ['subset', 'subset_comb']:
    func = globals()[name]

    def test_single_element(self):
        subsets = [set(), {1}]
        self.assertEqual(self.to_frozen(subsets), self.to_frozen(func({1})))
    setattr(SubsetTest, 'test_' + name + '_single_element', test_single_element)

    def test_multiple_elements(self):
        subsets = [set(), {1}, {2}, {1, 2}]
        self.assertEqual(self.to_frozen(subsets), self.to_frozen(func({1, 2})))
    setattr(SubsetTest, 'test_' + name + '_multiple_elements', test_multiple_elements)

    def test_more_elements(self):
        subsets = [set(), {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}]
        self.assertEqual(self.to_frozen(subsets), self.to_frozen(func({1, 2, 3})))
    setattr(SubsetTest, 'test_' + name + '_more_elements', test_more_elements)

if __name__ == '__main__':
    unittest.main()
