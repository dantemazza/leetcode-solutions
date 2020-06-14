# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        memo = {}
        return self.isBalanced2(root, memo)
        
    def isBalanced2(self, root, memo):
        if not root:
            return True
        return abs(self.height(root.left, memo)-self.height(root.right, memo)) < 2 and self.isBalanced2(root.left, memo) and self.isBalanced2(root.right, memo)
    
    def height(self, node, memo):
        if not node:        
            return 0
        if node in memo:
            return memo[node]
        memo[node] = 1 + max(self.height(node.right, memo), self.height(node.left, memo))
        return memo[node]
