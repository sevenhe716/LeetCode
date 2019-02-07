import unittest

from DynamicProgramming.q714_best_time_to_buy_and_sell_stock_with_transaction_fee import Solution1


class TestBestTimeToBuyAndSellStockWithTransactionFee(unittest.TestCase):
    """Test q714_best_time_to_buy_and_sell_stock_with_transaction_fee.py"""

    def test_best_time_to_buy_and_sell_stock_with_transaction_fee(self):
        s = Solution1()

        # self.assertEqual(8, s.maxProfit([1, 3, 2, 8, 4, 9], 2))
        # self.assertEqual(4, s.maxProfit([1, 4, 3, 6, 7], 2))
        self.assertEqual(2, s.maxProfit([1, 4, 1, 4], 2))


if __name__ == '__main__':
    unittest.main()
