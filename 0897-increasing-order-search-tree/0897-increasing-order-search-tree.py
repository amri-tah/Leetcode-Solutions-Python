# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        queue = deque()
        def inorder(root):
            if not root: return None
            inorder(root.left)
            queue.append(root)
            inorder(root.right)
        inorder(root)
        
        new = queue.popleft()
        current = new
        while queue:
            node = queue.popleft()
            node.left = None
            current.right = node
            current = node
        
        current.right = None
        return new