# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        output = TreeNode(preorder[0])
        for i in range(1, len(preorder)):
            node = output
            while True:
                if preorder[i] > node.val:
                    if node.right:
                        node = node.right
                    else:
                        node.right = TreeNode(preorder[i])
                        break
                else:
                    if node.left:
                        node = node.left
                    else:
                        node.left = TreeNode(preorder[i])
                        break
        return output
            
        

       
            
    
