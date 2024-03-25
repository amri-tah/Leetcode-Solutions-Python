class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        visited = set()
        output = []
        for num in nums:
            if num in visited and num not in output: output.append(num)
            else: visited.add(num)
        return output