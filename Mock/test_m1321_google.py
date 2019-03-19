import unittest

from Mock.m1321_google import Solution


class TestGoogle(unittest.TestCase):
    """Test m1321_google.py"""

    def test_google(self):
        s = Solution()

        self.assertEqual(True, s.isToeplitzMatrix(matrix=[
            [1, 2, 3, 4],
            [5, 1, 2, 3],
            [9, 5, 1, 2]
        ]))
        self.assertEqual(False, s.isToeplitzMatrix(matrix=[
            [1, 2],
            [2, 2]
        ]))


if __name__ == '__main__':
    unittest.main()
