import unittest

from Mock.m3112_amazon import Solution


class TestAmazon(unittest.TestCase):
    """Test m3112_amazon.py"""

    def test_amazon(self):
        s = Solution()

        self.assertEqual([0, 0, 1, 1, 0, 0, 0, 0], s.prisonAfterNDays(cells=[0, 1, 0, 1, 1, 0, 0, 1], N=7))
        self.assertEqual([0, 0, 1, 1, 1, 1, 1, 0], s.prisonAfterNDays(cells=[1, 0, 0, 1, 0, 0, 1, 0], N=1000000000))


if __name__ == '__main__':
    unittest.main()
