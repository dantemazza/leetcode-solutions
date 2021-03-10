# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        nodes = {}
        def dfs(node, depth):
            if not node:
                return
            nonlocal nodes
            nodes[node] = depth
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        
        dfs(root, 2)
        for node, depth in nodes.items():
            if depth == d:
                left = node.left
                right = node.right
                node.left = TreeNode(v)
                node.right = TreeNode(v)
                node.left.left = left
                node.right.right = right
                
        return root
