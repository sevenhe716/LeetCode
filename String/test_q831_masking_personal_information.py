import unittest

from String.q831_masking_personal_information import Solution


class TestMaskingPersonalInformation(unittest.TestCase):
    """Test q831_masking_personal_information.py"""

    def test_masking_personal_information(self):
        s = Solution()

        self.assertEqual("l*****e@leetcode.com", s.maskPII("LeetCode@LeetCode.com"))
        self.assertEqual("a*****b@qq.com", s.maskPII("AB@qq.com"))
        self.assertEqual("***-***-7890", s.maskPII("1(234)567-890"))
        self.assertEqual("+**-***-***-5678", s.maskPII("86-(10)12345678"))


if __name__ == '__main__':
    unittest.main()
