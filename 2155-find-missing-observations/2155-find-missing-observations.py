class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sum_n = mean*(len(rolls)+n)-sum(rolls)
        if sum_n<n or sum_n>6*n: return []
        result = [sum_n//n]*n
        for i in range(sum_n%n):
            result[i] += 1
        return result