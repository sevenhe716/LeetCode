import unittest

from String.q722_remove_comments import Solution1


class TestRemoveComments(unittest.TestCase):
    """Test q722_remove_comments.py"""

    def test_remove_comments(self):
        s = Solution1()

        self.assertEqual(["int main()", "{ ", "  ", "int a, b, c;", "a = b + c;", "}"], s.removeComments(
            source=["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;",
                    "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]))

        self.assertEqual(["ab"], s.removeComments(source=["a/*comment", "line", "more_comment*/b"]))

        self.assertEqual(["struct Node{","    ","    int size;","    int val;","};"], s.removeComments(source=["struct Node{", "    /*/ declare members;/**/", "    int size;", "    /**/int val;", "};"]))


if __name__ == '__main__':
    unittest.main()
