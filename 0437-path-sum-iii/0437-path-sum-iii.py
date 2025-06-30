# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.paths = 0
        hash = defaultdict(int) # sum: no of paths
        hash[0] = 1 # count of paths that give sum 0 = 1
        def dfs(node, curr):
            if not node: return
            curr += node.val
            self.paths += hash[curr - targetSum]
            hash[curr] += 1
            dfs(node.left, curr)
            dfs(node.right, curr)
            hash[curr] -= 1 
            return count

        dfs(root, 0)
        return self.paths