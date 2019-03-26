import unittest

from String.q165_compare_version_numbers import Solution


class TestCompareVersionNumbers(unittest.TestCase):
    """Test q165_compare_version_numbers.py"""

    def test_compare_version_numbers(self):
        s = Solution()

        self.assertEqual(-1, s.compareVersion(version1="0.1", version2="1.1"))
        self.assertEqual(1, s.compareVersion(version1="1.0.1", version2="1"))
        self.assertEqual(-1, s.compareVersion(version1="7.5.2.4", version2="7.5.3"))
        self.assertEqual(0, s.compareVersion(version1="1.01", version2="1.001"))
        self.assertEqual(0, s.compareVersion(version1="1.0", version2="1.0.0"))


if __name__ == '__main__':
    unittest.main()
