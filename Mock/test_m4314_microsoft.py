import unittest

from common import test_by_reflect


class TestMicrosoft(unittest.TestCase):
    """Test m4314_microsoft.py"""

    def test_lru_cache(self):
        commands = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
        params = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
        res = [None, None, None, 1, None, -1, None, -1, 3, 4]

        test_by_reflect(self, 'm4314_microsoft', commands, params, res)

        commands = ["LRUCache", "put", "put", "get", "put", "put", "get"]
        params = [[2], [2, 1], [2, 2], [2], [1, 1], [4, 1], [2]]
        res = [None, None, None, 2, None, None, -1]
        test_by_reflect(self, 'm4314_microsoft', commands, params, res)


if __name__ == '__main__':
    unittest.main()
