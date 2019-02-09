import unittest

from String.q242_valid_anagram import Solution


class TestValidAnagram(unittest.TestCase):
    """Test q242_valid_anagram.py"""

    def test_valid_anagram(self):
        s = Solution()

        self.assertEqual(True, s.isAnagram("anagram", "nagaram"))
        self.assertEqual(False, s.isAnagram("rat", "cat"))


if __name__ == '__main__':
    unittest.main()
