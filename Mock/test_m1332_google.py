import unittest

from Mock.m1332_google import Solution


class TestGoogle(unittest.TestCase):
    """Test m1332_google.py"""

    def test_google(self):
        s = Solution()

        self.assertEqual(1, s.numIslands(
            [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"],
             ["0", "0", "0", "0", "0"]]))


if __name__ == '__main__':
    unittest.main()
