class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # How many coins to get to denomination i
        dp = [amount+1]*(amount+1)
        dp[0] = 0 # No of coins to get amt 0 = 0
        
        for i in range(1, amount+1):
            for d in coins:
                if i-d>=0: dp[i] = min(dp[i], 1+dp[i-d])
                
        return dp[amount] if dp[-1]!=amount+1 else -1