import unittest

from Mock.m4222_microsoft import Solution


class TestMicrosoft(unittest.TestCase):
    """Test m4222_microsoft.py"""

    def test_microsoft(self):
        s = Solution()

        self.assertEqual(-1, s.compareVersion(version1="0.1", version2="1.1"))
        self.assertEqual(1, s.compareVersion(version1="1.0.1", version2="1"))
        self.assertEqual(-1, s.compareVersion(version1="7.5.2.4", version2="7.5.3"))
        self.assertEqual(0, s.compareVersion(version1="1.01", version2="1.001"))
        self.assertEqual(0, s.compareVersion(version1="1.0", version2="1.0.0"))


if __name__ == '__main__':
    unittest.main()
