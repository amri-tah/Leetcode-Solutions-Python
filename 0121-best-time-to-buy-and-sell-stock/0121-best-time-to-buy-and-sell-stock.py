class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = buy + 1
        maxprofit = 0
        
        while sell<len(prices):
            if prices[buy]>=prices[sell]:
                buy = sell
            else:
                maxprofit = max(maxprofit, prices[sell]-prices[buy])
            sell+=1
        return maxprofit