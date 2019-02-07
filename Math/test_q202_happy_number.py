import unittest

from Math.q202_happy_number import Solution


class TestHappyNumber(unittest.TestCase):
    """Test q202_happy_number.py"""

    def test_happy_number(self):
        s = Solution()

        self.assertEqual(True, s.isHappy(19))


if __name__ == '__main__':
    unittest.main()
