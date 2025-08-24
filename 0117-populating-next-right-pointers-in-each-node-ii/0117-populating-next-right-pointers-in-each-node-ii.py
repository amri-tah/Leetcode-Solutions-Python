"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        queue = deque([root])
        root.next = None
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            for i in range(1, len(level)):
                level[i-1].next = level[i]
            level[-1].next=None
        return root