class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        res = prices[:]
        for i in range(len(prices)):
            while stack and prices[i] <= prices[stack[-1]]:
                j = stack.pop()
                res[j] -= prices[i]
            stack.append(i)
        return res
            