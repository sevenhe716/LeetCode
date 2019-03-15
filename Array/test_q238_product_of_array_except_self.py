import unittest

from Array.q238_product_of_array_except_self import Solution


class TestProductOfArrayExceptSelf(unittest.TestCase):
    """Test q238_product_of_array_except_self.py"""

    def test_product_of_array_except_self(self):
        s = Solution()

        self.assertEqual([24, 12, 8, 6], s.productExceptSelf([1, 2, 3, 4]))


if __name__ == '__main__':
    unittest.main()
