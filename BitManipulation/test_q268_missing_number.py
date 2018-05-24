import unittest

from BitManipulation.q268_missing_number import Solution


class TestMissingNumber(unittest.TestCase):
    """Test q268_missing_number.py"""

    def test_missing_number(self):
        s = Solution()

        self.assertEqual(2, s.missingNumber([3, 0, 1]))
        self.assertEqual(8, s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
        self.assertEqual(0, s.missingNumber([]))
        self.assertEqual(0, s.missingNumber([1]))
        self.assertEqual(1, s.missingNumber([0]))


if __name__ == '__main__':
    unittest.main()
