import unittest

from DynamicProgramming.q122_best_time_to_buy_and_sell_stock_ii import Solution


class TestBestTimeToBuyAndSellStockIi(unittest.TestCase):
    """Test q122_best_time_to_buy_and_sell_stock_ii.py"""

    def test_best_time_to_buy_and_sell_stock_ii(self):
        s = Solution()

        self.assertEqual(7, s.maxProfit([7, 1, 5, 3, 6, 4]))
        self.assertEqual(4, s.maxProfit([1, 2, 3, 4, 5]))


if __name__ == '__main__':
    unittest.main()
