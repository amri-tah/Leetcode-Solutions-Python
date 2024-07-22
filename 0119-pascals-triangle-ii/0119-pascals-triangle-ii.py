class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        dp = [1, 1]
        for i in range(2, rowIndex+1):
            output = [1]*(i+1)
            for j in range(1, i):
                output[j] = dp[j-1]+dp[j]
            dp = output
        return dp