import unittest

from common import test_by_reflect


class TestImplementTriePrefixTree(unittest.TestCase):
    """Test q208_implement_trie_prefix_tree.py"""

    def test_implement_trie_prefix_tree(self):
        commands = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
        params = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
        res = [None, None, True, False, True, None, True]
        test_by_reflect(self, 'q208_implement_trie_prefix_tree', commands, params, res)


if __name__ == '__main__':
    unittest.main()
