import unittest

from DynamicProgramming.q256_paint_house import Solution


class TestPaintHouse(unittest.TestCase):
    """Test q256_paint_house.py"""

    def test_paint_house(self):
        s = Solution()

        self.assertEqual(10, s.minCost([[17, 2, 17], [16, 16, 5], [14, 3, 19]]))
        self.assertEqual(0, s.minCost([]))


if __name__ == '__main__':
    unittest.main()
