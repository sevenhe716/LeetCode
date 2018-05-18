import unittest

from String.q833_find_and_replace_in_string import Solution


class TestFindAndReplaceInString(unittest.TestCase):
    """Test q833_find_and_replace_in_string.py"""

    def test_find_and_replace_in_string(self):
        s = Solution()

        self.assertEqual("eeebffff", s.findReplaceString("abcd", [0, 2], ["a", "cd"], ["eee", "ffff"]))
        self.assertEqual("eeecd", s.findReplaceString("abcd", [0, 2], ["ab", "ec"], ["eee", "ffff"]))
        self.assertEqual("b", s.findReplaceString("a", [0], ["a"], ["b"]))
        self.assertEqual("bc", s.findReplaceString("a", [0], ["a"], ["bc"]))
        self.assertEqual("a", s.findReplaceString("a", [0], ["b"], ["cb"]))
        self.assertEqual("vbfrssozp", s.findReplaceString("vmokgggqzp", [3,5,1], ["kg","ggq","mo"], ["s","so","bfr"]))
        self.assertEqual(
            "eajqquqrfptryagjllnsyssfenmdjwezbrvkrvhqxofbrskrxgjvdkmujwajubrkugqekfaizsxiomcigroaoeqoidhjnwsnxdedp",
            s.findReplaceString(
                "ehvfwtrvcodllgjctguxeicjoudmxbevzrvravkidnricwsbnxmxvdckzahmqzbrlqugtmjvoqbxarmlgjeqcorhnodvnoqfomdp",
                [1, 31, 44, 70, 23, 73, 76, 92, 90, 86, 42, 4, 50, 17, 53, 20, 55, 15, 38, 64, 25, 9, 7, 68, 60, 88, 96,
                 47, 57, 34, 81, 78, 28],
                ["hvf", "vzr", "cw", "jvo", "jo", "qb", "ar", "noqf", "dv", "rh", "ri", "wt", "mx", "gux", "dc", "eic",
                 "kz", "ct", "kidn", "lq", "ud", "odll", "vc", "tm", "qz", "no", "om", "bn", "ahm", "vra", "jeqco",
                 "ml", "xb"],
                ["ajq", "zb", "r", "fai", "e", "zs", "io", "snxd", "nw", "oi", "ofb", "quq", "gj", "nsys", "dk", "sf",
                 "muj", "ll", "hqx", "k", "n", "ptrya", "f", "qek", "u", "dhj", "e", "kr", "waj", "rvkr", "roaoeq",
                 "mci", "djw"]))


if __name__ == '__main__':
    unittest.main()
