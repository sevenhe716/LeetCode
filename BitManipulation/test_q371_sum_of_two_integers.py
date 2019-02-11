import unittest

from BitManipulation.q371_sum_of_two_integers import Solution


class TestSumOfTwoIntegers(unittest.TestCase):
    """Test q371_sum_of_two_integers.py"""

    def test_sum_of_two_integers(self):
        s = Solution()

        self.assertEqual(3, s.getSum(1, 2))
        self.assertEqual(1, s.getSum(-2, 3))
        self.assertEqual(-20, s.getSum(-12, -8))


if __name__ == '__main__':
    unittest.main()
