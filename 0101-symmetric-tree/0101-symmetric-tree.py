# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def checkSym(p, q):
            if not q and not p:
                return True
            elif not q or not p:
                return False
            elif p.val!= q.val:
                return False
            return checkSym(p.left, q.right) and checkSym(q.left, p.right)
        return checkSym(root.left, root.right)
            