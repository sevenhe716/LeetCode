import unittest

from String.q065_valid_number import Solution


class TestValidNumber(unittest.TestCase):
    """Test q065_valid_number.py"""

    def test_valid_number(self):
        s = Solution()

        self.assertEqual(True, s.isNumber('0'))
        self.assertEqual(False, s.isNumber('0012'))
        self.assertEqual(True, s.isNumber(" 0.1 "))
        self.assertEqual(True, s.isNumber(" 3.1 "))
        self.assertEqual(False, s.isNumber(" 0000.1 "))
        self.assertEqual(True, s.isNumber(" 10.1123 "))
        self.assertEqual(False, s.isNumber("abc"))
        self.assertEqual(False, s.isNumber("1 a"))
        self.assertEqual(True, s.isNumber("2e10"))
        self.assertEqual(True, s.isNumber("1.232e10"))
        self.assertEqual(True, s.isNumber(".1"))
        self.assertEqual(False, s.isNumber("e"))
        self.assertEqual(False, s.isNumber("."))

if __name__ == '__main__':
    unittest.main()
