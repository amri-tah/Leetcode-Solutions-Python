# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        sum = 0 
        stack = [(root, str(root.val))]
        
        while stack:
            node, value = stack.pop()
            if node.left is None and node.right is None:
                sum += int(value)
                
            if node.left:
                stack.append((node.left, value+str(node.left.val)))
            if node.right:
                stack.append((node.right, value+str(node.right.val)))
        return sum
    