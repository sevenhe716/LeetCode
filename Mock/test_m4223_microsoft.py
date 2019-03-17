import unittest

from Mock.m4223_microsoft import Solution


class TestMicrosoft(unittest.TestCase):
    """Test m4223_microsoft.py"""

    def test_microsoft(self):
        s = Solution()

        self.assertEqual('6', s.multiply(num1="2", num2="3"))
        self.assertEqual('56088', s.multiply(num1="123", num2="456"))
        self.assertEqual('0', s.multiply(num1="123", num2="0"))
        self.assertEqual('0', s.multiply(num1="0", num2="456"))
        self.assertEqual('0', s.multiply(num1="0", num2="0"))


if __name__ == '__main__':
    unittest.main()
