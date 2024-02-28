class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visited = set()
        for value in nums:
            if value in visited: return value
            visited.add(value)