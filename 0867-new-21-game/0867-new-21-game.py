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
        dp = [0]*maxPts
        dp[0]=1
        currsum, res = 1, 0
        for i in range(1, n+1):
            prob = currsum/maxPts
            if i < k: currsum += prob   # still playing → add prob to window
            else: res += prob       # stopped → add prob to final result
            if i >= maxPts: currsum -= dp[i % maxPts]
            dp[i % maxPts] = prob
        return res
