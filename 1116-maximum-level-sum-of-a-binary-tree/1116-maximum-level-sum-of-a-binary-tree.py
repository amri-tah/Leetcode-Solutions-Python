# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        level, maxsum = 1, -float("inf")
        while queue:
            levelsum = 0
            levellen = len(queue)
            for _ in range(levellen):
                node = queue.popleft()
                levelsum += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if levelsum>maxsum:
                maxsum =levelsum
                maxlevel = level
            level+=1
        return maxlevel