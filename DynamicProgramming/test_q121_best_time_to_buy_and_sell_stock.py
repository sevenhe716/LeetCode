import unittest

from DynamicProgramming.q121_best_time_to_buy_and_sell_stock import Solution


class TestBestTimeToBuyAndSellStock(unittest.TestCase):
    """Test q121_best_time_to_buy_and_sell_stock.py"""

    def test_best_time_to_buy_and_sell_stock(self):
        s = Solution()

        self.assertEqual(5, s.maxProfit([7, 1, 5, 3, 6, 4]))
        self.assertEqual(0, s.maxProfit([7, 6, 4, 3, 1]))


if __name__ == '__main__':
    unittest.main()
