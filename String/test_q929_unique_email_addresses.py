import unittest

from String.q929_unique_email_addresses import Solution1


class TestUniqueEmailAddresses(unittest.TestCase):
    """Test q929_unique_email_addresses.py"""

    def test_unique_email_addresses(self):
        s = Solution1()

        self.assertEqual(2, s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))


if __name__ == '__main__':
    unittest.main()
