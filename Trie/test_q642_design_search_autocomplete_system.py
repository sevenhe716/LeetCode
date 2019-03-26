import unittest

from common import test_by_reflect


class TestDesignSearchAutocompleteSystem(unittest.TestCase):
    """Test q642_design_search_autocomplete_system.py"""

    def test_design_search_autocomplete_system(self):
        commands = ["AutocompleteSystem", "input", "input", "input", "input"]
        params = [[["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"]]
        res = [None, ["i love you", "island", "i love leetcode"], ["i love you", "i love leetcode"], [], []]
        test_by_reflect(self, 'q642_design_search_autocomplete_system', commands, params, res)

        commands = ["AutocompleteSystem", "input", "input", "input", "input", "input", "input", "input", "input",
                    "input", "input", "input", "input", "input", "input"]
        params = [[["abc", "abbc", "a"], [3, 3, 3]], ["b"], ["c"], ["#"], ["b"], ["c"], ["#"], ["a"], ["b"], ["c"],
                  ["#"], ["a"], ["b"], ["c"], ["#"]]
        res = [None, [], [], [], ["bc"], ["bc"], [], ["a", "abbc", "abc"], ["abbc", "abc"], ["abc"], [],
               ["abc", "a", "abbc"], ["abc", "abbc"], ["abc"], []]
        test_by_reflect(self, 'q642_design_search_autocomplete_system', commands, params, res)

        commands = ["AutocompleteSystem", "input", "input", "input", "input", "input", "input", "input", "input", "input", "input",
         "input", "input"]
        params = [[["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"], ["i"], [" "],
         ["a"], ["#"], ["i"], [" "], ["a"], ["#"]]
        res = [None, ["i love you", "island", "i love leetcode"], ["i love you", "i love leetcode"], [], [],
         ["i love you", "island", "i love leetcode"], ["i love you", "i love leetcode", "i a"], ["i a"], [],
         ["i love you", "island", "i a"], ["i love you", "i a", "i love leetcode"], ["i a"], []]
        test_by_reflect(self, 'q642_design_search_autocomplete_system', commands, params, res)


if __name__ == '__main__':
    unittest.main()
