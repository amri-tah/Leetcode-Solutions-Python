class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        visited = {}
        for index, value in enumerate(numbers):
            remaining = target - value
            if remaining in visited:
                return [visited[remaining]+1, index+1]
            else:
                visited[value] = index