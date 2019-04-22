import unittest

from Array.q220_contains_duplicate_iii import Solution


class TestContainsDuplicateIii(unittest.TestCase):
    """Test q220_contains_duplicate_iii.py"""

    def test_contains_duplicate_iii(self):
        s = Solution()

        self.assertEqual(True, s.containsNearbyAlmostDuplicate([2, 0, 4], 3, 3))


if __name__ == '__main__':
    unittest.main()
