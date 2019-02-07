import unittest

from DynamicProgramming.q119_pascal_triangle_ii import Solution


class TestPascalTriangleIi(unittest.TestCase):
    """Test q119_pascal_triangle_ii.py"""

    def test_pascal_triangle_ii(self):
        s = Solution()

        self.assertEqual([1, 3, 3, 1], s.getRow(3))


if __name__ == '__main__':
    unittest.main()
