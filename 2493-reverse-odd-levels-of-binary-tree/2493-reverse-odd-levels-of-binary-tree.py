# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def bfs(root):
            queue = deque()
            queue.append(root)
            level = 0
            
            while queue:
                n = len(queue)
                values = []
                nodes = []

                for _ in range(n):
                    node = queue.popleft()
                    nodes.append(node)
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)

                    if level%2==1: values.append(node.val)

                if level%2==1:
                    values.reverse()
                    for i in range(n):
                        nodes[i].val = values[i]

                level+=1
                
        bfs(root)
        return root