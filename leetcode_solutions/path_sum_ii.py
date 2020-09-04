# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        
        def add(node, path, sum):
            nonlocal res
            if not sum and not node.left and not node.right:
                res.append(copy.copy(path))
                path.pop()
                return 
            for curr in [node.left, node.right]:
                if curr:
                    path.append(curr.val)
                    add(curr, path, sum-curr.val)
            path.pop()
            
        if root:   
            add(root, [root.val], sum-root.val)
        return res
                
