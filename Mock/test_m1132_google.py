import unittest

from Mock.m1132_google import Solution


class TestInterview32(unittest.TestCase):
    """Test m1132_google.py"""

    def test_interview_3_2(self):
        s = Solution()

        self.assertEqual(2, s.kEmptySlots([1, 3, 2], 1))
        self.assertEqual(-1, s.kEmptySlots([1, 2, 3], 1))


if __name__ == '__main__':
    unittest.main()
