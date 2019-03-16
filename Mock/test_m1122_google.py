import unittest

from Mock.m1122_google import Solution


class TestInterview22(unittest.TestCase):
    """Test m1122_google.py"""

    def test_interview_2_2(self):
        s = Solution()

        self.assertEqual(32, s.lengthLongestPath(
            "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
        self.assertEqual(20, s.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))


if __name__ == '__main__':
    unittest.main()
