# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.pathsum = 0
        def backtrack(root, path):
            if not root: return
            path.append(str(root.val))
            if not root.left and not root.right: self.pathsum+=int("".join(path))
            if root.left: backtrack(root.left, path)
            if root.right: backtrack(root.right, path)
            path.pop()
        backtrack(root, [])
        return self.pathsum