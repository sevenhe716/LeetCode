import unittest

from Mock.m1313_google import Solution


class TestGoogle(unittest.TestCase):
    """Test m1313_google.py"""

    def test_google(self):
        s = Solution()

        self.assertEqual(9, s.numberOfPatterns(1, 1))


if __name__ == '__main__':
    unittest.main()
