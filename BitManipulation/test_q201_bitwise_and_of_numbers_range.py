import unittest

from BitManipulation.q201_bitwise_and_of_numbers_range import Solution


class TestBitwiseAndOfNumbersRange(unittest.TestCase):
    """Test q201_bitwise_and_of_numbers_range.py"""

    def test_bitwise_and_of_numbers_range(self):
        s = Solution()

        self.assertEqual(4, s.rangeBitwiseAnd([5, 7]))
        self.assertEqual(0, s.rangeBitwiseAnd([0, 1]))


if __name__ == '__main__':
    unittest.main()
