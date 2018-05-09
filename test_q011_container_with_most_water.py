import unittest

from q011_container_with_most_water import Solution


class TestContainerWithMostWater(unittest.TestCase):
    """Test q011_container_with_most_water.py"""

    def test_container_with_most_water(self):
        s = Solution()

        self.assertEqual(1, s.maxArea([1, 1]))
        self.assertEqual(6, s.maxArea([1, 3, 5, 4, 2]))
        self.assertEqual(6, s.maxArea([1, 2, 3, 3, 2, 1]))


if __name__ == '__main__':
    unittest.main()
