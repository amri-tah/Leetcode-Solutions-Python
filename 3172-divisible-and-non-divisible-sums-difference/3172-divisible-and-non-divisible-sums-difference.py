class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        result = 0
        for i in range(1, n+1):
            if i%m!=0: result+=i
            else: result-=i
        return result