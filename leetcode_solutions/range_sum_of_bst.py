# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        res = 0
        def find(node):
            nonlocal res
            if not node: return
            if node.val >= L and node.val <= R:
                res += node.val
            find(node.left)
            find(node.right)
        find(root)
        return res
