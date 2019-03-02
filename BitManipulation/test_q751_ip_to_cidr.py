import unittest

from BitManipulation.q751_ip_to_cidr import Solution


class TestIpToCidr(unittest.TestCase):
    """Test q751_ip_to_cidr.py"""

    def test_ip_to_cidr(self):
        s = Solution()

        self.assertEqual(["255.0.0.7/32", "255.0.0.8/29", "255.0.0.16/32"], s.ipToCIDR("255.0.0.7", 10))


if __name__ == '__main__':
    unittest.main()
