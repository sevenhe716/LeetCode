import unittest

from Array.q217_contains_duplicate import Solution


class TestContainsDuplicate(unittest.TestCase):
    """Test q217_contains_duplicate.py"""

    def test_contains_duplicate(self):
        s = Solution()

        self.assertEqual(True, s.containsDuplicate([1, 2, 3, 1]))
        self.assertEqual(False, s.containsDuplicate([1, 2, 3, 4]))
        self.assertEqual(True, s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))


if __name__ == '__main__':
    unittest.main()
