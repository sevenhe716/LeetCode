import unittest

from PriorityQueue.q755_pour_water import Solution1


class TestPourWater(unittest.TestCase):
    """Test q755_pour_water.py"""

    def test_pour_water(self):
        s = Solution1()

        self.assertEqual([2, 2, 2, 3, 2, 2, 2], s.pourWater([2, 1, 1, 2, 1, 2, 2], 4, 3))
        self.assertEqual([2, 3, 3, 4], s.pourWater([1, 2, 3, 4], 2, 2))
        self.assertEqual([4, 4, 4], s.pourWater([3, 1, 3], 5, 1))
        self.assertEqual([1, 2, 3, 4, 3, 3, 2, 2, 3, 4, 3, 2, 1],
                         s.pourWater([1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1], 2, 5))


if __name__ == '__main__':
    unittest.main()
