import unittest

from Mock.m1324_google import Solution


class TestGoogle(unittest.TestCase):
    """Test m1324_google.py"""

    def test_google(self):
        s = Solution()

        self.assertEqual(105.00000, s.mincostToHireWorkers(quality=[10, 20, 5], wage=[70, 50, 30], K=2))
        self.assertEqual(30.66667, s.mincostToHireWorkers(quality=[3, 1, 10, 10, 1], wage=[4, 8, 2, 2, 7], K=3))


if __name__ == '__main__':
    unittest.main()
