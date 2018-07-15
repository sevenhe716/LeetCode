import unittest

from q861_score_after_flipping_matrix import Solution


class TestScoreAfterFlippingMatrix(unittest.TestCase):
    """Test q861_score_after_flipping_matrix.py"""

    def test_score_after_flipping_matrix(self):
        s = Solution()

        self.assertEqual(39, s.matrixScore([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]))
        self.assertEqual(11, s.matrixScore([[0, 1], [0, 1], [0, 1], [0, 0]]))


if __name__ == '__main__':
    unittest.main()
