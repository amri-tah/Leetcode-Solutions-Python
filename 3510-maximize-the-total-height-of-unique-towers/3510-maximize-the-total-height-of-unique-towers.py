class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort()
        max_height, curr_height = 0, maximumHeight[-1]

        for i in range(len(maximumHeight)-1, -1, -1):
            if curr_height<=0: return -1
            curr_height = min(curr_height, maximumHeight[i])
            max_height += curr_height
            curr_height-=1
        return max_height
        
