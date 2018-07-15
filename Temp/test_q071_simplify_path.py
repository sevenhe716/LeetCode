import unittest

from Temp.q071_simplify_path import Solution


class TestSimplifyPath(unittest.TestCase):
    """Test q071_simplify_path.py"""

    def test_simplify_path(self):
        s = Solution()

        self.assertEqual("/home", s.simplifyPath("/home/"))
        self.assertEqual("/c", s.simplifyPath("/a/./b/../../c/"))


if __name__ == '__main__':
    unittest.main()
