# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        depth_map = {}
        if not root:
            return 0
        return max(self.depth(root.left, depth_map) + self.depth(root.right, depth_map), self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
    
    def depth(self, root, depth_map):
        if not root:
            return 0
        if root in depth_map:
            return depth_map[root]    
        depth_map[root] = 1 + max(self.depth(root.left, depth_map), self.depth(root.right, depth_map))
        return depth_map[root]
