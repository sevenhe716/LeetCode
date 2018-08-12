import unittest

from Temp.q879_profitable_schemes import Solution


class TestProfitableSchemes(unittest.TestCase):
    """Test q879_profitable_schemes.py"""

    def test_profitable_schemes(self):
        s = Solution()

        self.assertEqual(2, s.profitableSchemes(5, 3, [2,2], [2,3]))
        self.assertEqual(7, s.profitableSchemes(10, 5, [2,3,5], [6,7,8]))


if __name__ == '__main__':
    unittest.main()
