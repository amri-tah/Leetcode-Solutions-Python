# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append(root)
        level = 0
        while queue:
            n = len(queue)
            prev = None
            for _ in range(n):
                node = queue.popleft()

                if (level%2==0 and node.val%2==0) or (level%2==1 and node.val%2==1): return False
                if prev is not None:
                    if (level%2==0 and prev>=node.val) or (level%2==1 and prev<=node.val): return False
                prev = node.val
                
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            level+=1

        return True
