import unittest

from DynamicProgramming.q123_best_time_to_buy_and_sell_stock_iii import Solution


class TestBestTimeToBuyAndSellStockIii(unittest.TestCase):
    """Test q123_best_time_to_buy_and_sell_stock_iii.py"""

    def test_best_time_to_buy_and_sell_stock_iii(self):
        s = Solution()

        self.assertEqual(0, s.maxProfit([]))
        self.assertEqual(6, s.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
        self.assertEqual(4, s.maxProfit([1, 2, 3, 4, 5]))


if __name__ == '__main__':
    unittest.main()
