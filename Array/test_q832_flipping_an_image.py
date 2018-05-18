import unittest

from Array.q832_flipping_an_image import Solution


class TestFlippingAnImage(unittest.TestCase):
    """Test q832_flipping_an_image.py"""

    def test_flipping_an_image(self):
        s = Solution()

        self.assertEqual([[1], [0]], s.flipAndInvertImage([[0], [1]]))
        self.assertEqual([[1, 0, 0], [0, 1, 0], [1, 1, 1]], s.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
        self.assertEqual([[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]],
                         s.flipAndInvertImage([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))

if __name__ == '__main__':
    unittest.main()