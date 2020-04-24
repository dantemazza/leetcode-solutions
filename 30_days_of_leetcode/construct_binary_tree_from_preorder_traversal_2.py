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
        stack = [output]
        for i in range(1, len(preorder)):
            if preorder[i] < stack[-1].val:
                node = TreeNode(preorder[i])
                stack[-1].left = node
                stack.append(node)
            else:
                pop = None
                while stack and stack[-1].val < preorder[i]:
                    pop = stack.pop()
                node = TreeNode(preorder[i])
                stack.append(node)
                pop.right = node
        return output
        
