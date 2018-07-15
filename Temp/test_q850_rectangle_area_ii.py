import unittest

from Temp.q850_rectangle_area_ii import Solution


class TestRectangleAreaIi(unittest.TestCase):
    """Test q850_rectangle_area_ii.py"""

    def test_rectangle_area_ii(self):
        s = Solution()

        self.assertEqual(6, s.rectangleArea([[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]))
        self.assertEqual(49, s.rectangleArea([[0, 0, 1000000000, 1000000000]]))


if __name__ == '__main__':
    unittest.main()
