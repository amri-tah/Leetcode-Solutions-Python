# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        ops = 0
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                level.append(node.val)
            val_index = {n: i for i, n in enumerate(level)}
            sorted_level = sorted(level)
            for i in range(len(level)):
                if sorted_level[i]!=level[i]: 
                    ops+=1
                    j = val_index[sorted_level[i]]
                    level[i], level[j] = level[j], level[i]
                    val_index[level[j]] = j
                    val_index[level[i]] = i
        return ops