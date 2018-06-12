import unittest

from DynamicProgramming.q062_unique_paths import Solution


class TestUniquePaths(unittest.TestCase):
    """Test q062_unique_paths.py"""

    def test_unique_paths(self):
        s = Solution()

        self.assertEqual(3, s.uniquePaths(3, 2))
        self.assertEqual(28, s.uniquePaths(7, 3))
        self.assertEqual(193536720, s.uniquePaths(23, 12))


if __name__ == '__main__':
    unittest.main()
