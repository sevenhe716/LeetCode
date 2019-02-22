import unittest

from Temp.q389_find_the_difference import Solution


class TestFindTheDifference(unittest.TestCase):
    """Test q389_find_the_difference.py"""

    def test_find_the_difference(self):
        s = Solution()

        self.assertEqual('e', s.findTheDifference('abcd', 'abcde'))


if __name__ == '__main__':
    unittest.main()
