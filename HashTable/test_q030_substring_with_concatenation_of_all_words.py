import unittest

from HashTable.q030_substring_with_concatenation_of_all_words import Solution1


class TestSubstringWithConcatenationOfAllWords(unittest.TestCase):
    """Test q030_substring_with_concatenation_of_all_words.py"""

    def test_substring_with_concatenation_of_all_words(self):
        s = Solution1()

        self.assertEqual([0, 9], s.findSubstring('barfoothefoobarman', ["foo", "bar"]))
        self.assertEqual([], s.findSubstring('wordgoodstudentgoodword', ["word", "student"]))
        self.assertEqual([8], s.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))
        self.assertEqual([974], s.findSubstring(
            "cvecqxjemfumiqgppzqadaduhzxwymeahkdzhodtvyhfqouipmitmlpvmmsmayniishpglkbltgbhclxptsdgjzvxrhxpufxmpouaavltdodgaaxvuccdbxauezlbhipwykwahjulxxtzzsvtuzyywasczefgovenfapmjjzjiukhmfchecfcczhedmmsjrhotwdfieqqzaalgeumhzrlzapemewwxfmqerxmwnevoggulbiuczfdbxiodgmaoasssqgqdklrtrnguwaxxfczekphrdjfdczxsfnvrypkscqoasnyaqzeaootrxawbzwtejrykiickbsltgltwmawaqstnsrpsnkyxdwjlhlykfldlwzhibgkryfgqwxkmkjlnhuzohzymkeygffqincznhhgfhqrrbcejyfxfeysoeqwjxornqsazbgfizyzadgjbljhsjzinrfwqtpdmjelkmqvlpumsaxtoicgrbqeuvclrtqdcwopjhkwwekqhklxsofkrvqorvbiornrobgzisxgyiyfskcmahytdphwkkgactrswzthrqnsaoxuychalfvqwdoipujrpclocevvxkpzypuyrdyeiuxhznroiaizftpjakgzvwyvlsuevskgohppvggfjogojwxlgdkdbjzmbvqznbfekwvhcbmlrvbdryozezffigujbkkqnpuylsfqtudnpfqifehjdorlulxvxhmlzilmascwogjdlzlsfvcjjvueitbfbpsayfmayrwmxhskifcocgxmdtslnvtqllsjrglrxifwpxiaflohtnvxgnkvldnwrfhkmsbjcgiugquldiuxvqwdfibqmomfuvpioqtqybkeservomulcsrhbsapgouckjmyzgqzjdgbjxzylvlpoczruzgdnahxjuxkcqjltppcnqcanoqbqpunoasdabdlxcvzsfnlucojsskfgcjzrdohggmgjpshspgkutyrxocrgmxpqiohncqtkdctswcmllzggxzenbvvoukgeaqscgnojpkenmszzrhgqgkfhhbxcleimuaqaqhmhrsvfmufgbnyjxeqgfoissrgotxqjeerxwoelilrlypuxvkecaovuhbibabmgfffetkpdxioyxkvvvbxxqssxwcawdnflskpoweruogslqpinrgnhafgyjhxpucaompcjvwfjcxwumfkfnxmnevmncjeyleoztrkqnpzroyndfziswxfcstsuewurbirwbdnqtohjmxmrwvjvurxmmpirmckpmblohyeanolzlytjveepxedktndhrnwdrirygwavmlxzjqigwpxutaeonjwgwukpcbnlzngnzfmkvxrumoohruvgdtnboxrqaedcumpvrefpbyjppxwirrowldxzcordtvhnjwkaarpdqashxorqifmvlkwnynqtkxitwswyklccoulnlcetjsouckidzaymahfwbbwnpyrdvcqggwbsprmtbwyczxozgwxjztzosqtpvmvbiytzpitsgtufsleahbkgxjxrbsgwedapbtoqdjikdcrxpwywzifwtenuwvrdyrszmgpsszexevutrsstczrvdhsbclgdeycqhukztoyzkstdllwpmqnrxfubqbeuzjmidxjylhyxatbngzcsppjoudsmewigfvoksyjfhjdhcguifzaxqlnnqfzxcidjftuztfebojksphcxgcuwpjlfplctvhcadyzwdfztpmngtpfbtbzillqawuttexthwufbzhvqtizmaentgmcrzut",
            ["hbkgxjxrbsgwedapbtoqdjikdc", "rwbdnqtohjmxmrwvjvurxmmpir", "qbeuzjmidxjylhyxatbngzcspp",
             "mckpmblohyeanolzlytjveepxe", "dktndhrnwdrirygwavmlxzjqig", "abmgfffetkpdxioyxkvvvbxxqs",
             "szexevutrsstczrvdhsbclgdey", "wpxutaeonjwgwukpcbnlzngnzf", "wumfkfnxmnevmncjeyleoztrkq",
             "dohggmgjpshspgkutyrxocrgmx", "lkwnynqtkxitwswyklccoulnlc", "rxpwywzifwtenuwvrdyrszmgps",
             "gqgkfhhbxcleimuaqaqhmhrsvf", "rgnhafgyjhxpucaompcjvwfjcx", "umpvrefpbyjppxwirrowldxzco",
             "rdtvhnjwkaarpdqashxorqifmv", "rxwoelilrlypuxvkecaovuhbib", "zosqtpvmvbiytzpitsgtufslea",
             "cqhukztoyzkstdllwpmqnrxfub", "npzroyndfziswxfcstsuewurbi", "bvvoukgeaqscgnojpkenmszzrh",
             "sxwcawdnflskpoweruogslqpin", "fzaxqlnnqfzxcidjftuztfeboj", "pqiohncqtkdctswcmllzggxzen",
             "mufgbnyjxeqgfoissrgotxqjee", "etjsouckidzaymahfwbbwnpyrd", "mkvxrumoohruvgdtnboxrqaedc",
             "vcqggwbsprmtbwyczxozgwxjzt", "joudsmewigfvoksyjfhjdhcgui"]))


if __name__ == '__main__':
    unittest.main()
