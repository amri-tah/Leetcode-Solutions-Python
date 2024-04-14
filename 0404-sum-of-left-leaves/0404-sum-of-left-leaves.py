# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        stack, sum = [root], 0

        while stack:
            node = stack.pop()
            if node.left:
                if not node.left.left and not node.left.right:  # if leaf node
                    sum += node.left.val
                else: # if not leaf node 
                    stack.append(node.left)
                    
            if node.right:
                stack.append(node.right)

        return sum