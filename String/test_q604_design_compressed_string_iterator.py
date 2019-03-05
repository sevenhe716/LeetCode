import unittest

from common import test_by_reflect


class TestDesignCompressedStringIterator(unittest.TestCase):
    """Test q604_design_compressed_string_iterator.py"""

    def test_design_compressed_string_iterator(self):
        commands = ["StringIterator4", "next", "next", "next", "next", "next", "next", "hasNext", "next", "hasNext"]
        params = [["L1e2t1C1o1d1e1"], [], [], [], [], [], [], [], [], []]
        res = [None, "L", "e", "e", "t", "C", "o", True, "d", True]

        test_by_reflect(self, 'q604_design_compressed_string_iterator', commands, params, res)


if __name__ == '__main__':
    unittest.main()
