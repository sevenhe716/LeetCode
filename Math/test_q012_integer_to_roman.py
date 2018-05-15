import unittest

from Math.q012_integer_to_roman import Solution


class TestIntegerToRoman(unittest.TestCase):
    """Test q012_integer_to_roman.py"""

    def test_integer_to_roman(self):
        s = Solution()

        self.assertEqual('I', s.intToRoman(1))
        self.assertEqual('III', s.intToRoman(3))
        self.assertEqual('IV', s.intToRoman(4))
        self.assertEqual('IX', s.intToRoman(9))
        self.assertEqual('LVIII', s.intToRoman(58))
        self.assertEqual('MCMXCIV', s.intToRoman(1994))
        self.assertEqual('MMCMXCIV', s.intToRoman(2994))
        self.assertEqual('MMMCMXCIX', s.intToRoman(3999))


if __name__ == '__main__':
    unittest.main()
