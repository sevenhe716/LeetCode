import unittest

from Mock.m1331_google import Solution


class TestGoogle(unittest.TestCase):
    """Test m1331_google.py"""

    def test_google(self):
        s = Solution()

        self.assertEqual([
            ["abc", "bcd", "xyz"],
            ["az", "ba"],
            ["acef"],
            ["a", "z"]
        ], s.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))


if __name__ == '__main__':
    unittest.main()
