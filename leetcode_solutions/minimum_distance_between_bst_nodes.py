# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        minimum = sys.maxsize
        curr = -sys.maxsize
        def inorder(node):
            if not node: return
            nonlocal curr
            nonlocal minimum
            inorder(node.left)
            minimum = min(minimum, node.val-curr)
            curr = node.val
            inorder(node.right)
        
        inorder(root)
        return minimum
