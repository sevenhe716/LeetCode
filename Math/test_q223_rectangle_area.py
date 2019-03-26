import unittest

from Math.q223_rectangle_area import Solution


class TestRectangleArea(unittest.TestCase):
    """Test q223_rectangle_area.py"""

    def test_rectangle_area(self):
        s = Solution()

        self.assertEqual(45, s.computeArea(A=-3, B=0, C=3, D=4, E=0, F=-1, G=9, H=2))


if __name__ == '__main__':
    unittest.main()
