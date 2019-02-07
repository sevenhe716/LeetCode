import unittest

from DynamicProgramming.q118_pascal_triangle import Solution


class TestPascalTriangle(unittest.TestCase):
    """Test q118_pascal_triangle.py"""

    def test_pascal_triangle(self):
        s = Solution()

        self.assertEqual([], s.generate(0))
        self.assertEqual([[1]], s.generate(1))
        self.assertEqual([
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ], s.generate(5))


if __name__ == '__main__':
    unittest.main()
