import unittest

from Mock.m1111_google import Solution


class TestInterview11(unittest.TestCase):
    """Test m1111_google.py"""

    def test_interview_1_1(self):
        s = Solution()

        self.assertEqual(2, s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))


if __name__ == '__main__':
    unittest.main()
