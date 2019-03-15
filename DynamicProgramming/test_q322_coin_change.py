import unittest

from DynamicProgramming.q322_coin_change import Solution


class TestCoinChange(unittest.TestCase):
    """Test q322_coin_change.py"""

    def test_coin_change(self):
        s = Solution()

        self.assertEqual(3, s.coinChange([1, 2, 5], 11))
        self.assertEqual(-1, s.coinChange([2], 3))


if __name__ == '__main__':
    unittest.main()
