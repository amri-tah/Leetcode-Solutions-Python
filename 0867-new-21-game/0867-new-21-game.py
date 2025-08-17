class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # Brute force
        # self.result = 0.0
        # def dfs(score, prob):
        #     if score >= k:
        #         if score <= n: self.result += prob
        #         return
        #     for draw in range(1, maxPts+1):
        #         dfs(score + draw, prob/maxPts)
        # dfs(0, 1.0)
        # return self.result

        if k==0 or n>=k-1+maxPts: return 1
        dp = [0]*(n+1)
        dp[0]=1
        currsum, res = 1, 0
        for i in range(1, n+1):
            dp[i] = currsum/maxPts
            if i < k: currsum += dp[i]   # still playing → add prob to window
            else: res += dp[i]       # stopped → add prob to final result
            if i-maxPts >= 0: currsum -= dp[i - maxPts]
        return res
