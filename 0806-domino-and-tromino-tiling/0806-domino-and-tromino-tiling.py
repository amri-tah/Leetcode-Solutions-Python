class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        if n == 1 or n==2: return n
        dp = [0] * (n + 3)
        dp[0], dp[1], dp[2] = 1, 2, 5
        
        for i in range(3, n):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD
        
        return dp[n - 1]