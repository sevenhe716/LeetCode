import unittest

from Array.q041_first_missing_positive import Solution


class TestFirstMissingPositive(unittest.TestCase):
    """Test q041_first_missing_positive.py"""

    def test_first_missing_positive(self):
        s = Solution()

        self.assertEqual(3, s.firstMissingPositive([1, 2, 0]))
        self.assertEqual(2, s.firstMissingPositive([3, 4, -1, 1]))
        self.assertEqual(1, s.firstMissingPositive([7, 8, 9, 11, 12]))
        self.assertEqual(5, s.firstMissingPositive([3, 1, 2, 4]))
        self.assertEqual(5, s.firstMissingPositive([3, 1, 0, 2, 4]))
        self.assertEqual(3, s.firstMissingPositive([-1, 4, 2, 1, 9, 10]))


if __name__ == '__main__':
    unittest.main()
