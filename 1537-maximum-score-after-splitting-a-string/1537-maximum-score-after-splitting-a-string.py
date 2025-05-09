class Solution:
    def maxScore(self, s: str) -> int:
        s = [int(x) for x in s]
        leftSum, rightSum, score = 0, sum(s), 0
        for i in range(len(s) - 1):
            if s[i] == 0: leftSum += 1
            else: rightSum -= 1
            score = max(score, leftSum + rightSum)
        return score