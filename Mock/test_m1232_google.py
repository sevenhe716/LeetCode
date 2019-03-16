import unittest

from Mock.m1232_google import Solution


class TestGoogle(unittest.TestCase):
    """Test m1232_google.py"""

    def test_google(self):
        s = Solution()

        self.assertEqual("eeebffff",
                         s.findReplaceString(S="abcd", indexes=[0, 2], sources=["a", "cd"], targets=["eee", "ffff"]))
        self.assertEqual("eeecd",
                         s.findReplaceString(S="abcd", indexes=[0, 2], sources=["ab", "ec"], targets=["eee", "ffff"]))
        self.assertEqual("vbfrssozp",
                         s.findReplaceString("vmokgggqzp", [3, 5, 1], ["kg", "ggq", "mo"], ["s", "so", "bfr"]))


if __name__ == '__main__':
    unittest.main()
