import unittest

from Math.q013_roman_to_integer import Solution


class TestRomanToInteger(unittest.TestCase):
    """Test q013_roman_to_integer.py"""

    def test_roman_to_integer(self):
        s = Solution()

        self.assertEqual(1, s.romanToInt('I'))
        self.assertEqual(3, s.romanToInt('III'))
        self.assertEqual(4, s.romanToInt('IV'))
        self.assertEqual(9, s.romanToInt('IX'))
        self.assertEqual(58, s.romanToInt('LVIII'))
        self.assertEqual(1994, s.romanToInt('MCMXCIV'))
        self.assertEqual(2994, s.romanToInt('MMCMXCIV'))
        self.assertEqual(3999, s.romanToInt('MMMCMXCIX'))


if __name__ == '__main__':
    unittest.main()
