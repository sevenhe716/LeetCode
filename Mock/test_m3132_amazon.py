import unittest

from Mock.m3132_amazon import Solution


class TestAmazon(unittest.TestCase):
    """Test m3132_amazon.py"""

    def test_amazon(self):
        s = Solution()

        self.assertEqual([[-2, 2]], s.kClosest(points=[[1, 3], [-2, 2]], K=1))
        self.assertEqual([[3, 3], [-2, 4]], s.kClosest(points=[[3, 3], [5, -1], [-2, 4]], K=2))


if __name__ == '__main__':
    unittest.main()
