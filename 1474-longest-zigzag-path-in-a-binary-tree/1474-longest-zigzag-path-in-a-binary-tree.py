# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.path = 0
        def dfs(root, dir, currpath):
            if not root: return
            self.path = max(self.path, currpath)
            if dir=="R":
                dfs(root.left, "L", currpath+1)
                dfs(root.right, "R", 1)
            else:
                dfs(root.right, "R", currpath+1)
                dfs(root.left, "L", 1)
        dfs(root.left, "L", 1)
        dfs(root.right, "R", 1)
        return self.path