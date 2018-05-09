import unittest

from q008_string_to_integer_atoi import SolutionF


class TestStringToIntegerAtoi(unittest.TestCase):
    """Test q008_string_to_integer_atoi.py"""

    def test_string_to_integer_atoi(self):
        s = SolutionF()
        self.assertEqual(42, s.myAtoi("42"))
        self.assertEqual(42, s.myAtoi("+42"))
        self.assertEqual(-42, s.myAtoi("-42"))
        self.assertEqual(-42, s.myAtoi("   -42"))
        self.assertEqual(4193, s.myAtoi("4193 with words"))
        self.assertEqual(-2147483648, s.myAtoi("-91283472332"))
        self.assertEqual(2147483647, s.myAtoi("91283472332"))
        self.assertEqual(0, s.myAtoi(""))
        self.assertEqual(0, s.myAtoi("+"))
        self.assertEqual(0, s.myAtoi("-"))
        self.assertEqual(123, s.myAtoi("0123"))


if __name__ == '__main__':
    unittest.main()
