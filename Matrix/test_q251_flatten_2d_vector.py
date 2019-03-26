import unittest

from common import test_by_reflect


class TestFlatten2DVector(unittest.TestCase):
    """Test q251_flatten_2d_vector.py"""

    def test_flatten_2d_vector(self):
        commands = ["Vector2D", "next", "next", "next", "hasNext", "hasNext", "next", "hasNext"]
        params = [[[[1, 2], [3], [4]]], [], [], [], [], [], [], []]
        res = [None, 1, 2, 3, True, True, 4, False]
        test_by_reflect(self, 'q251_flatten_2d_vector', commands, params, res)

        commands = ["Vector2D", "hasNext", "next", "hasNext"]
        params = [[[[], [3]]], [], [], []]
        res = [None, True, 3, False]
        test_by_reflect(self, 'q251_flatten_2d_vector', commands, params, res)

if __name__ == '__main__':
    unittest.main()
