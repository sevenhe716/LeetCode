import unittest

from Math.q043_multiply_strings import Solution


class TestMultiplyStrings(unittest.TestCase):
    """Test q043_multiply_strings.py"""

    def test_multiply_strings(self):
        s = Solution()

        self.assertEqual('6', s.multiply('2', '3'))
        self.assertEqual('56088', s.multiply('123', '456'))
        self.assertEqual('0', s.multiply('123', '0'))
        self.assertEqual('0', s.multiply('0', '0'))


if __name__ == '__main__':
    unittest.main()
