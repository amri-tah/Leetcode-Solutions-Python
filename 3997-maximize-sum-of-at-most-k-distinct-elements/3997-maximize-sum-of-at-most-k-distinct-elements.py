class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums.sort(reverse=True)
        visited = set()
        res = []
        for n in nums:
            if k>0:
                if n not in visited:
                    visited.add(n)
                    res.append(n)
                    k-=1
            else: return res
        return res