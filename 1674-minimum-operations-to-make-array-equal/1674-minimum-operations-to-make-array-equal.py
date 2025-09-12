class Solution:
    def minOperations(self, n: int) -> int:
        # req value => sum/n
        # -=1 in the right side and +=1 in the left
        req = n
        ops = 0
        left, right = 1, 2*(n-1)+1
        while left<=right and left!=req and right!=req:
            ops+=req-left
            left+=2
            right-=2
        return ops
