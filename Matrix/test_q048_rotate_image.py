import unittest

from Matrix.q048_rotate_image import Solution


class TestRotateImage(unittest.TestCase):
    """Test q048_rotate_image.py"""

    def test_rotate_image(self):
        s = Solution()

        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        s.rotate(matrix)
        self.assertEqual([
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ], matrix)

        matrix = [
            [5, 1, 9, 11],
            [2, 4, 8, 10],
            [13, 3, 6, 7],
            [15, 14, 12, 16]
        ]
        s.rotate(matrix)

        self.assertEqual([
            [15, 13, 2, 5],
            [14, 3, 4, 1],
            [12, 6, 8, 9],
            [16, 7, 10, 11]
        ], matrix)

        matrix = []
        s.rotate(matrix)

        self.assertEqual([], matrix)


if __name__ == '__main__':
    unittest.main()
