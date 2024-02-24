class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max = 0
        while left<right:
            amt = (right-left)*min(height[left], height[right])
            if amt > max:
                max = amt
            if height[left] >= height[right]:
                right-=1
            else:
                left+=1
        return max
                
            