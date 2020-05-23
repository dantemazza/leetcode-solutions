# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        K = 1
        def inorder(node):
            if not node:
                return None
            nonlocal K
            l = inorder(node.left)
            if l is not None:
                return l
            if K == k:
                return node.val
            K += 1
            r = inorder(node.right)
            if r is not None:
                return r
        return inorder(root)
        
