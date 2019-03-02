import unittest

from String.q246_strobogrammatic_number import Solution


class TestStrobogrammaticNumber(unittest.TestCase):
    """Test q246_strobogrammatic_number.py"""

    def test_strobogrammatic_number(self):
        s = Solution()

        self.assertEqual(True, s.isStrobogrammatic('69'))
        self.assertEqual(True, s.isStrobogrammatic('88'))
        self.assertEqual(False, s.isStrobogrammatic('962'))


if __name__ == '__main__':
    unittest.main()
