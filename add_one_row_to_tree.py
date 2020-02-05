# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        q2 = deque()
        q1 = deque()
        q1.append(root);
        if d == 1:
            node = root
            root = TreeNode(v)
            root.left = node
            return root
        depth = 1
        while depth != d-1:
            while len(q1) > 0:
                node = q1.popleft()
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            depth += 1
            q1 += q2
            q2.clear()
        while len(q1) > 0:
            node = q1.popleft()
            left = node.left
            right = node.right
            node.left = TreeNode(v)
            node.right = TreeNode(v)
            node.left.left = left
            node.right.right = right
        
        return root
            
                
        
