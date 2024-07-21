class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2: return n
        currStep, nextStep = 2, 1
        for i in range(2, n):
            temp = currStep+nextStep
            nextStep = currStep
            currStep = temp
        return currStep