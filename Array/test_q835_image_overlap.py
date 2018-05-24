import unittest

from Array.q835_image_overlap import Solution


class TestImageOverlap(unittest.TestCase):
    """Test q835_image_overlap.py"""

    def test_image_overlap(self):
        s = Solution()

        self.assertEqual(3, s.largestOverlap([[1, 1, 0],
                                              [0, 1, 0],
                                              [0, 1, 0]],
                                             [[0, 0, 0],
                                              [0, 1, 1],
                                              [0, 0, 1]]))
        self.assertEqual(1, s.largestOverlap([[1]], [[1]]))
        self.assertEqual(0, s.largestOverlap([[1]], [[0]]))
        self.assertEqual(0, s.largestOverlap([], []))
        self.assertEqual(4, s.largestOverlap([[1, 1, 1], [1, 0, 0], [0, 1, 1]],
                                             [[1, 1, 0], [1, 1, 1], [1, 1, 0]]))
        self.assertEqual(1, s.largestOverlap([[1, 0], [0, 0]], [[0, 1], [1, 0]]))
        self.assertEqual(2, s.largestOverlap([[0, 1], [1, 1]], [[1, 1], [1, 0]]))


if __name__ == '__main__':
    unittest.main()
