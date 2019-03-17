import unittest

from Mock.m4333_microsoft import Solution


class TestMicrosoft(unittest.TestCase):
    """Test m4333_microsoft.py"""

    def test_microsoft(self):
        s = Solution()

        self.assertEqual(["int main()", "{ ", "  ", "int a, b, c;", "a = b + c;", "}"], s.removeComments(
            source=["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;",
                    "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]))

        self.assertEqual(["ab"], s.removeComments(source=["a/*comment", "line", "more_comment*/b"]))


if __name__ == '__main__':
    unittest.main()
