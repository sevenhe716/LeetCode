import unittest

from HashTable.q811_subdomain_visit_count import Solution


class TestSubdomainVisitCount(unittest.TestCase):
    """Test q811_subdomain_visit_count.py"""

    def test_subdomain_visit_count(self):
        s = Solution()

        self.assertEqual(sorted(["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]), sorted(s.subdomainVisits(["9001 discuss.leetcode.com"])))
        self.assertEqual(sorted(["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]), sorted(s.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])))


if __name__ == '__main__':
    unittest.main()
