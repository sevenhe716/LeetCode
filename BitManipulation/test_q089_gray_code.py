import unittest

from BitManipulation.q089_gray_code import Solution


class TestGrayCode(unittest.TestCase):
    """Test q089_gray_code.py"""

    def test_gray_code(self):
        s = Solution()

        self.assertEqual([0, 1, 3, 2, 6, 7, 5, 4], s.grayCode(3))
        self.assertEqual([0, 1, 3, 2], s.grayCode(2))
        self.assertEqual([0], s.grayCode(0))


if __name__ == '__main__':
    unittest.main()
