import unittest

from Mock.m2232_facebook import Solution


class TestFacebook(unittest.TestCase):
    """Test m2232_facebook.py"""

    def test_facebook(self):
        s = Solution()

        arr = [1, 2, 3]
        s.nextPermutation(arr)
        self.assertEqual([1, 3, 2], arr)

        arr = [3, 2, 1]
        s.nextPermutation(arr)
        self.assertEqual([1, 2, 3], arr)

        arr = [1, 1, 5]
        s.nextPermutation(arr)
        self.assertEqual([1, 5, 1], arr)

        arr = [2, 3, 1]
        s.nextPermutation(arr)
        self.assertEqual([3, 1, 2], arr)


if __name__ == '__main__':
    unittest.main()
