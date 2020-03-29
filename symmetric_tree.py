# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        layer = [root]
        
        while layer:
            newLayer = []
            for node in layer:
                if node:
                    newLayer.append(node.left)
                    newLayer.append(node.right)
            vals = [node.val if node else -1 for node in newLayer]
            if vals != vals[::-1]:
                return False
            layer = newLayer
        
        return True
                
                
        
