import unittest


def running_stairs(n):
    """Return number of ways to running up stairs with 1, 2, 3 hops."""
    return _running_dp(n, {0: 1})

def _running_dp(n, cache):
    """Helper for running_stairs. DP approach."""
    if n < 0:
        return 0
    if n not in cache:
        cache[n] = _running_dp(n - 1, cache) +  _running_dp(n - 2,
                cache) + _running_dp(n - 3, cache)
    return cache[n]

class RuningStairsTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_running_stairs(self):
        self.assertEqual(1, running_stairs(1))
        self.assertEqual(2, running_stairs(2))
        self.assertEqual(4, running_stairs(3))
        self.assertEqual(7, running_stairs(4))

if __name__ == '__main__':
    unittest.main()
