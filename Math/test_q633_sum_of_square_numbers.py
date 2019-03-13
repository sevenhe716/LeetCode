import unittest

from Math.q633_sum_of_square_numbers import Solution


class TestSumOfSquareNumbers(unittest.TestCase):
    """Test q633_sum_of_square_numbers.py"""

    def test_sum_of_square_numbers(self):
        s = Solution()

        self.assertEqual(True, s.judgeSquareSum(5))
        self.assertEqual(False, s.judgeSquareSum(3))
        self.assertEqual(True, s.judgeSquareSum(0))
        self.assertEqual(True, s.judgeSquareSum(1))
        self.assertEqual(True, s.judgeSquareSum(2))


if __name__ == '__main__':
    unittest.main()
