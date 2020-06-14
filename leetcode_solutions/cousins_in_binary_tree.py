# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        parentx = None
        parenty = None
        depthx = 0
        depthy = 0
            
        def dfs(node, parent, depth):
            if not node: 
                return 
            if node.val == x:
                nonlocal parentx
                parentx = parent
                nonlocal depthx 
                depthx = depth
            if node.val == y:
                nonlocal parenty
                parenty = parent
                nonlocal depthy 
                depthy = depth
            if node.left:
                dfs(node.left, node, depth+1)
            if node.right:
                dfs(node.right, node, depth+1)
        
        dfs(root, None, 0)
        # print(parentx, parenty, depthx, depthy)
        return parentx != parenty and depthx == depthy
