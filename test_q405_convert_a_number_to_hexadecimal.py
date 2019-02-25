import unittest

from q405_convert_a_number_to_hexadecimal import Solution


class TestConvertANumberToHexadecimal(unittest.TestCase):
    """Test q405_convert_a_number_to_hexadecimal.py"""

    def test_convert_a_number_to_hexadecimal(self):
        s = Solution()

        self.assertEqual("0", s.toHex(0))
        self.assertEqual("a", s.toHex(10))
        self.assertEqual("1a", s.toHex(26))
        self.assertEqual("ffffffff", s.toHex(-1))


if __name__ == '__main__':
    unittest.main()
