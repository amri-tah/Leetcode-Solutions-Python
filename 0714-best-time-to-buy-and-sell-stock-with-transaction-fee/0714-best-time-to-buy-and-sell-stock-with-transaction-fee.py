class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit = 0
        buy = prices[0]
        for i in range(1,len(prices)):
            profit = max(profit, prices[i]-buy-fee)
            buy = min(buy, prices[i]-profit)
        return profit
        