import unittest

from common import test_by_reflect


class TestDesignHitCounter(unittest.TestCase):
    """Test q362_design_hit_counter.py"""

    def test_design_hit_counter(self):
        commands = ["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
        params = [[], [1], [2], [3], [4], [300], [300], [301]]
        res = [None, None, None, None, 3, None, 4, 3]
        test_by_reflect(self, 'q362_design_hit_counter', commands, params, res)


if __name__ == '__main__':
    unittest.main()
