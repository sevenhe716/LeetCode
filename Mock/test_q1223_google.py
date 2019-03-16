import unittest

from Mock.q1223_google import Solution


class TestGoogle(unittest.TestCase):
    """Test q1223_google.py"""

    def test_google(self):
        s = Solution()

        self.assertEqual(0, s.longestLine([]))
        self.assertEqual(3, s.longestLine([[0, 1, 1, 0],
                                           [0, 1, 1, 0],
                                           [0, 0, 0, 1]]))


if __name__ == '__main__':
    unittest.main()
