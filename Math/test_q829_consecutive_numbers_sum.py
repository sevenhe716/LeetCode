import unittest

from Math.q829_consecutive_numbers_sum import SolutionF


class TestConsecutiveNumbersSum(unittest.TestCase):
    """Test q829_consecutive_numbers_sum.py"""

    def test_consecutive_numbers_sum(self):
        s = SolutionF()

        self.assertEqual(1, s.consecutiveNumbersSum(1))
        self.assertEqual(2, s.consecutiveNumbersSum(5))
        self.assertEqual(3, s.consecutiveNumbersSum(9))
        self.assertEqual(4, s.consecutiveNumbersSum(15))
        self.assertEqual(2, s.consecutiveNumbersSum(3))


if __name__ == '__main__':
    unittest.main()
