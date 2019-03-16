import unittest

from Mock.m1121_google import Solution


class TestInterview21(unittest.TestCase):
    """Test m1121_google.py"""

    def test_interview_2_1(self):
        s = Solution()

        self.assertEqual("5F3Z-2E9W", s.licenseKeyFormatting("5F3Z-2e-9-w", 4))
        self.assertEqual("2-5G-3J", s.licenseKeyFormatting("2-5g-3-J", 2))


if __name__ == '__main__':
    unittest.main()
