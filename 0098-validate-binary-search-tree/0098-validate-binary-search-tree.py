# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root: return [True, float('inf'), float('-inf')]
            left = dfs(root.left)
            right = dfs(root.right)
            is_valid = (left[0] and right[0] and
                        root.val > left[2] and
                        root.val < right[1])
            return [is_valid, min(root.val, left[1]), max(root.val, right[2])]
        return dfs(root)[0]
