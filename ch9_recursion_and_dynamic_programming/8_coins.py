import unittest


def coins(amount):
    """Returns number of ways to represent 'amount' of coins."""
    _set = set()
    _coins(_set, [], 25, amount)
    return len(_set)
    
def _coins(_set, nums, denom, amount):
    """Returns all the combinations to represent 'amount' of coins."""
    if denom == 1:
        _set.add(tuple(nums + [amount]))
        return
    next_denom = {25: 10, 10: 5, 5: 1}[denom]
    for i in range(0, amount + 1, denom):
        _coins(_set, nums + [i // denom], next_denom, amount - i)

def make_change(amount, denom):
    """Returns number of ways to represent 'amount' coins.
    
    Start from the coin of biggest value, use from 1 to as many as possible,
    then move on to the next coin.
    """
    if denom == 1:
        return 1
    next_denom = {25: 10, 10: 5, 5: 1}[denom]
    ways = 0
    for i in range(0, amount + 1, denom):
        ways += make_change(amount - i, next_denom)
    return ways

class CoinsTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_coins_0(self):
        self.assertEqual(1, coins(0))
        self.assertEqual(1, make_change(0, 25))

    def test_coins_1(self):
        self.assertEqual(1, coins(1))
        self.assertEqual(1, make_change(1, 25))

    def test_coins_5(self):
        self.assertEqual(2, coins(5))
        self.assertEqual(2, make_change(5, 25))

    def test_coins_6(self):
        self.assertEqual(2, coins(6))
        self.assertEqual(2, make_change(6, 25))

    def test_coins_10(self):
        self.assertEqual(4, coins(10))
        self.assertEqual(4, make_change(10, 25))

    def test_coins_15(self):
        self.assertEqual(6, coins(15))
        self.assertEqual(6, make_change(15, 25))

    def test_coins_25(self):
        self.assertEqual(13, coins(25))
        self.assertEqual(13, make_change(25, 25))

    def test_coins_100(self):
        self.assertEqual(coins(1000), make_change(1000, 25))

if __name__ == '__main__':
    unittest.main()
