# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        list1 = []
        list2 = []
        self.inorder(root1, list1)
        self.inorder(root2, list2)
        res = []
        i = 0
        j = 0
        while i < len(list1) or j < len(list2):
            if i < len(list1) and (j == len(list2) or list1[i] < list2[j]):
                res.append(list1[i])
                i += 1
            else:
                res.append(list2[j])
                j += 1
        return res
                
            
    
    def inorder(self, node, listNums):
        if not node:
            return 
        self.inorder(node.left, listNums)
        listNums.append(node.val)
        self.inorder(node.right, listNums)
        
