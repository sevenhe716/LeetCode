import unittest

from String.q247_strobogrammatic_number_ii import Solution1


class TestStrobogrammaticNumberIi(unittest.TestCase):
    """Test q247_strobogrammatic_number_ii.py"""

    def test_strobogrammatic_number_ii(self):
        s = Solution1()

        self.assertEqual(["101", "111", "181", "609", "619", "689", "808", "818", "888", "906", "916", "986"],
                         s.findStrobogrammatic(3))
        self.assertEqual(["11", "69", "88", "96"], s.findStrobogrammatic(2))
        self.assertEqual(["0", "1", "8"], s.findStrobogrammatic(1))
        self.assertEqual([""], s.findStrobogrammatic(0))


if __name__ == '__main__':
    unittest.main()
