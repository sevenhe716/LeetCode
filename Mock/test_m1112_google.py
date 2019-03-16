import unittest

from Mock.m1112_google import Solution


class TestInterview12(unittest.TestCase):
    """Test m1112_google.py"""

    def test_interview_1_2(self):
        s = Solution()

        self.assertEqual(3, s.totalFruit([1, 2, 1]))
        self.assertEqual(3, s.totalFruit([0, 1, 2, 2]))
        self.assertEqual(4, s.totalFruit([1, 2, 3, 2, 2]))
        self.assertEqual(5, s.totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))


if __name__ == '__main__':
    unittest.main()
