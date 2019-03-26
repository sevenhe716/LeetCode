import unittest

from String.q388_longest_absolute_file_path import Solution


class TestLongestAbsoluteFilePath(unittest.TestCase):
    """Test q388_longest_absolute_file_path.py"""

    def test_longest_absolute_file_path(self):
        s = Solution()

        self.assertEqual(32, s.lengthLongestPath(
            "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
        self.assertEqual(20, s.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))


if __name__ == '__main__':
    unittest.main()
