import unittest


def sieve_of_eratosthenes(num):
    """Return a list of all the prime numbers that is no bigger than num.
    
    Implements the algorithm of sieve of eratosthenes."""
    nums = list(range(num + 1))
    current = 2
    out = []
    while current <= num:
        out.append(current)
        # mark all mutiple of current prime to None
        for i in range(current * current, num + 1, current):
            nums[i] = None
        # find the next prime number
        for i in range(current + 1, num + 1):
            if nums[i]:
                current = nums[i]
                break
        else:
            break
    return out
    
class SieveOfEratosthenesTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_sieve_of_eratosthenes(self):
        self.assertEqual(sieve_of_eratosthenes(19), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(sieve_of_eratosthenes(20), [2, 3, 5, 7, 11, 13, 17, 19])

if __name__ == '__main__':
    unittest.main()
