import unittest

from HashTable.q049_group_anagrams import Solution1


class TestGroupAnagrams(unittest.TestCase):
    """Test q049_group_anagrams.py"""

    def test_group_anagrams(self):

        s = Solution1()

        def compare(xs, ys):
            xs.sort()
            ys.sort()

            return all(xs[i].sort() == ys[i].sort() for i in range(len(xs)))

        # compare = lambda x, y : collections.Counter(x) == collections.Counter(y)

        self.assertTrue(compare([
            ["ate", "eat", "tea"],
            ["nat", "tan"],
            ["bat"]
        ], s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])))

        self.assertTrue(compare([["eat"]], s.groupAnagrams(["eat"])))
        self.assertEqual([], s.groupAnagrams([]))


if __name__ == '__main__':
    unittest.main()
