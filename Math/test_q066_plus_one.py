import unittest

from Math.q066_plus_one import Solution


class TestPlusOne(unittest.TestCase):
    """Test q066_plus_one.py"""

    def test_plus_one(self):
        s = Solution()

        self.assertEqual([1, 2, 4], s.plusOne([1, 2, 3]))
        self.assertEqual([4, 3, 2, 2], s.plusOne([4, 3, 2, 1]))
        self.assertEqual([1], s.plusOne([0]))
        self.assertEqual([2, 0, 0], s.plusOne([1, 9, 9]))
        self.assertEqual([1, 0, 0, 0], s.plusOne([9, 9, 9]))


if __name__ == '__main__':
    unittest.main()
