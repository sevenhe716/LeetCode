import unittest

from Mock.m2221_facebook import Solution


class TestFacebook(unittest.TestCase):
    """Test m2221_facebook.py"""

    def test_facebook(self):
        s = Solution()

        arr = [0, 1, 0, 3, 12]
        s.moveZeroes(arr)
        self.assertEqual([1, 3, 12, 0, 0], arr)


if __name__ == '__main__':
    unittest.main()
