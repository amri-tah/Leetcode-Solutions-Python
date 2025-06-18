class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix = 0
        maxSum = 0
        for g in gain:
            prefix+=g
            maxSum = max(maxSum, prefix)

        return maxSum