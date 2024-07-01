# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        def inorder(root):
            if not root: return
            inorder(root.left)
            nodes.append(root.val)
            inorder(root.right)
            
        def buildBST(tnodes):
            if not tnodes: return
            mid = len(tnodes)//2
            return TreeNode(val=tnodes[mid], left=buildBST(tnodes[:mid]), right=buildBST(tnodes[mid+1:]))
        
        inorder(root)
        return buildBST(nodes)
        