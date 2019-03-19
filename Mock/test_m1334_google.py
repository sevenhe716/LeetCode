import unittest

from Mock.m1334_google import Solution


class TestGoogle(unittest.TestCase):
    """Test m1334_google.py"""

    def test_google(self):
        s = Solution()

        self.assertEqual([1, 1, 2, 3], s.numIslands2(3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]]))


if __name__ == '__main__':
    unittest.main()
