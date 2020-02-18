# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def treeMin(node, parent=False, p = None):
            if not node:
                return node
            while node.left:
                p = node
                node = node.left
            if parent:
                return node, p
            return node
        p = None
        node = root
        if not node:
            return root
        while node.val != key:
            p = node
            if node.val > key:
                node = node.left
            elif node.val < key:
                node = node.right
            if not node:
                return root
        
        temp = None
        if not node.left or not node.right:
                
            if not node.left:
                temp = node.right
            elif not node.right:
                temp = node.left
            if not p:
                return temp
            if p.left == node:
                p.left = temp
            else:
                p.right = temp
        else:
            succ, parent = treeMin(node.right, True, node)
            if node == parent:
                node.val = succ.val
                node.right = succ.right
            else:   
                node.val = succ.val
                parent.left = succ.right
        
        return root
        
        
        
        
