# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, minval, maxval):
            if not root: return True
            if not (root.val>minval and root.val<maxval): return False
            return dfs(root.left, minval, root.val) and dfs(root.right, root.val, maxval)
        return dfs(root, float('-inf'), float('inf'))