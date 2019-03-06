import unittest

from HashTable.q311_sparse_matrix_multiplication import Solution


class TestSparseMatrixMultiplication(unittest.TestCase):
    """Test q311_sparse_matrix_multiplication.py"""

    def test_sparse_matrix_multiplication(self):
        s = Solution()

        self.assertEqual([
            [7, 0, 0],
            [-7, 0, 3]
        ], s.multiply([
            [1, 0, 0],
            [-1, 0, 3]
        ], [
            [7, 0, 0],
            [0, 0, 0],
            [0, 0, 1]
        ]))

        self.assertEqual(
            [[17]], s.multiply([[1, -5]], [[12], [-1]]))

    if __name__ == '__main__':
        unittest.main()
