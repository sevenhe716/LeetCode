import unittest

from String.q482_license_key_formatting import Solution


class TestLicenseKeyFormatting(unittest.TestCase):
    """Test q482_license_key_formatting.py"""

    def test_license_key_formatting(self):
        s = Solution()

        self.assertEqual("5F3Z-2E9W", s.licenseKeyFormatting("5F3Z-2e-9-w", 4))
        self.assertEqual("2-5G-3J", s.licenseKeyFormatting("2-5g-3-J", 2))
        self.assertEqual("2", s.licenseKeyFormatting("2", 2))


if __name__ == '__main__':
    unittest.main()
