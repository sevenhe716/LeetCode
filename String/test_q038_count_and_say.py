import unittest

from String.q038_count_and_say import Solution


class TestCountAndSay(unittest.TestCase):
    """Test q038_count_and_say.py"""

    def test_count_and_say(self):
        s = Solution()

        self.assertEqual("1", s.countAndSay(1))
        self.assertEqual("1211", s.countAndSay(4))


if __name__ == '__main__':
    unittest.main()
