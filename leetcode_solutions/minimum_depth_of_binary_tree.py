# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        return self.getMin(root)
    
    
    def getMin(self, node):
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        if not node.left:
            return 1 + self.getMin(node.right)
        if not node.right:
            return 1 + self.getMin(node.left) 
        return min(1+self.getMin(node.left), 1+self.getMin(node.right))
