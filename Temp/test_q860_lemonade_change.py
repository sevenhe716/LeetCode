import unittest

from q860_lemonade_change import Solution


class TestLemonadeChange(unittest.TestCase):
    """Test q860_lemonade_change.py"""

    def test_lemonade_change(self):
        s = Solution()

        self.assertEqual(True, s.lemonadeChange([5, 5, 5, 10, 20]))
        self.assertEqual(True, s.lemonadeChange([5, 5, 10]))
        self.assertEqual(False, s.lemonadeChange([10, 10]))
        self.assertEqual(False, s.lemonadeChange([5, 5, 10, 10, 20]))


if __name__ == '__main__':
    unittest.main()
