import unittest

from DynamicProgramming.q309_best_time_to_buy_and_sell_stock_with_cooldown import Solution


class TestBestTimeToBuyAndSellStockWithCooldown(unittest.TestCase):
    """Test q309_best_time_to_buy_and_sell_stock_with_cooldown.py"""

    def test_best_time_to_buy_and_sell_stock_with_cooldown(self):
        s = Solution()

        self.assertEqual(3, s.maxProfit([1, 2, 3, 0, 2]))


if __name__ == '__main__':
    unittest.main()
