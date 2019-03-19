import unittest

from Mock.m1322_google import Solution


class TestGoogle(unittest.TestCase):
    """Test m1322_google.py"""

    def test_google(self):
        s = Solution()

        self.assertEqual("1A3B", s.getHint(secret="1807", guess="7810"))
        self.assertEqual("1A1B", s.getHint(secret="1123", guess="0111"))
        self.assertEqual("3A0B", s.getHint(secret="1122", guess="1222"))


if __name__ == '__main__':
    unittest.main()
