class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mem = {}
        def dp(i, j):
            if i==0 or j==0: return 0
            if (i,j) in mem: return mem[(i,j)]
            if text1[i-1]==text2[j-1]: res = 1+ dp(i-1, j-1)
            else: res = max(dp(i-1, j), dp(i, j-1))
            mem[(i,j)]=res
            return res
        return dp(len(text1), len(text2))