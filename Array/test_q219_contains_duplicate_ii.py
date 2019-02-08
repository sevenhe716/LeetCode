import unittest

from Array.q219_contains_duplicate_ii import Solution


class TestContainsDuplicateIi(unittest.TestCase):
    """Test q219_contains_duplicate_ii.py"""

    def test_contains_duplicate_ii(self):
        s = Solution()

        self.assertEqual(False, s.containsNearbyDuplicate([], 4))
        self.assertEqual(True, s.containsNearbyDuplicate([1, 2, 3, 1], 3))
        self.assertEqual(True, s.containsNearbyDuplicate([1, 0, 1, 1], 1))
        self.assertEqual(False, s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))


if __name__ == '__main__':
    unittest.main()
