# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            # No node
            return False
        
        if not root.left and not root.right:
            # Leaf node
            if root.val == targetSum:
                return True
            return False
        
        leftsum = self.hasPathSum(root.left, targetSum-root.val)
        rightsum = self.hasPathSum(root.right, targetSum-root.val)
        
        return leftsum or rightsum