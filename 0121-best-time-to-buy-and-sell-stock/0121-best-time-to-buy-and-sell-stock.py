class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf, minPrice = 0 , float('inf')
        for price in prices:
            minPrice = min(minPrice, price)
            maxProf = max(maxProf, price-minPrice)
        return maxProf
