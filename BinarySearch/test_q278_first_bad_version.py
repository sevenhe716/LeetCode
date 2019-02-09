import unittest

from BinarySearch.q278_first_bad_version import Solution


class TestFirstBadVersion(unittest.TestCase):
    """Test q278_first_bad_version.py"""

    def test_first_bad_version(self):
        s = Solution()

        self.assertEqual(4, s.firstBadVersion(5, 4))
        self.assertEqual(1, s.firstBadVersion(1, 1))


if __name__ == '__main__':
    unittest.main()
