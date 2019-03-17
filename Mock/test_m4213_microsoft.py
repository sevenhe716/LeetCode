import unittest

from Mock.m4213_microsoft import Solution


class TestMicrosoft(unittest.TestCase):
    """Test m4213_microsoft.py"""

    def test_microsoft(self):
        s = Solution()

        self.assertEqual(3, s.coinChange(coins=[1, 2, 5], amount=11))
        self.assertEqual(-1, s.coinChange(coins=[2], amount=3))


if __name__ == '__main__':
    unittest.main()
