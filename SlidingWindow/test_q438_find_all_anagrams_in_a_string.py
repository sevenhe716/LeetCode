import unittest

from SlidingWindow.q438_find_all_anagrams_in_a_string import Solution


class TestFindAllAnagramsInAString(unittest.TestCase):
    """Test q438_find_all_anagrams_in_a_string.py"""

    def test_find_all_anagrams_in_a_string(self):
        s = Solution()

        self.assertEqual([0, 6], s.findAnagrams("cbaebabacd", "abc"))
        self.assertEqual([0, 1, 2], s.findAnagrams("abab", "ab"))


if __name__ == '__main__':
    unittest.main()
