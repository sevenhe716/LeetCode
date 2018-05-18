import unittest

from Contests.c084 import Solution3
from Contests.c084 import Solution
from Contests.c084 import SolutionF


class TestC084(unittest.TestCase):
    """Test test_c084.py"""

    def test_c084(self):
        # s = Solution1()
        #
        # self.assertEqual([[1], [0]], s.flipAndInvertImage([[0], [1]]))
        # self.assertEqual([[1, 0, 0], [0, 1, 0], [1, 1, 1]], s.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
        # self.assertEqual([[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]],
        #                  s.flipAndInvertImage([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))

        s = SolutionF()

        # self.assertEqual("eeebffff", s.findReplaceString("abcd", [0, 2], ["a", "cd"], ["eee", "ffff"]))
        # self.assertEqual("eeecd", s.findReplaceString("abcd", [0, 2], ["ab", "ec"], ["eee", "ffff"]))
        # self.assertEqual("b", s.findReplaceString("a", [0], ["a"], ["b"]))
        # self.assertEqual("bc", s.findReplaceString("a", [0], ["a"], ["bc"]))
        # self.assertEqual("a", s.findReplaceString("a", [0], ["b"], ["cb"]))
        # self.assertEqual("vbfrssozp", s.findReplaceString("vmokgggqzp", [3,5,1], ["kg","ggq","mo"], ["s","so","bfr"]))
        # self.assertEqual(
        #     "eajqquqrfptryagjllnsyssfenmdjwezbrvkrvhqxofbrskrxgjvdkmujwajubrkugqekfaizsxiomcigroaoeqoidhjnwsnxdedp",
        #     s.findReplaceStringOneLine(
        #         "ehvfwtrvcodllgjctguxeicjoudmxbevzrvravkidnricwsbnxmxvdckzahmqzbrlqugtmjvoqbxarmlgjeqcorhnodvnoqfomdp",
        #         [1, 31, 44, 70, 23, 73, 76, 92, 90, 86, 42, 4, 50, 17, 53, 20, 55, 15, 38, 64, 25, 9, 7, 68, 60, 88, 96,
        #          47, 57, 34, 81, 78, 28],
        #         ["hvf", "vzr", "cw", "jvo", "jo", "qb", "ar", "noqf", "dv", "rh", "ri", "wt", "mx", "gux", "dc", "eic",
        #          "kz", "ct", "kidn", "lq", "ud", "odll", "vc", "tm", "qz", "no", "om", "bn", "ahm", "vra", "jeqco",
        #          "ml", "xb"],
        #         ["ajq", "zb", "r", "fai", "e", "zs", "io", "snxd", "nw", "oi", "ofb", "quq", "gj", "nsys", "dk", "sf",
        #          "muj", "ll", "hqx", "k", "n", "ptrya", "f", "qek", "u", "dhj", "e", "kr", "waj", "rvkr", "roaoeq",
        #          "mci", "djw"]))

        s = Solution3()
        # self.assertEqual(3, s.largestOverlap([[1, 1, 0],
        #                                       [0, 1, 0],
        #                                       [0, 1, 0]],
        #                                      [[0, 0, 0],
        #                                       [0, 1, 1],
        #                                       [0, 0, 1]]))
        # self.assertEqual(1, s.largestOverlap([[1]], [[1]]))
        # self.assertEqual(0, s.largestOverlap([[1]], [[0]]))
        # self.assertEqual(0, s.largestOverlap([], []))
        # self.assertEqual(4, s.largestOverlap([[1, 1, 1], [1, 0, 0], [0, 1, 1]],
        #                                      [[1, 1, 0], [1, 1, 1], [1, 1, 0]]))
        # self.assertEqual(1, s.largestOverlap1([[1, 0], [0, 0]], [[0, 1], [1, 0]]))
        # self.assertEqual(3, s.largestOverlap1([[0, 1], [1, 1]], [[1, 1], [1, 0]]))

        s = Solution()
        self.assertEqual([0], s.sumOfDistancesInTree(1, []))
        self.assertEqual([1, 1], s.sumOfDistancesInTree(2, [[0, 1]]))
        self.assertEqual([8, 12, 6, 10, 10, 10], s.sumOfDistancesInTree(6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]))
        self.assertEqual([18, 25, 13, 14, 20, 20, 21, 19, 26],
                         s.sumOfDistancesInTree(9, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5], [3, 6], [3, 7], [7, 8]]))


if __name__ == '__main__':
    unittest.main()
