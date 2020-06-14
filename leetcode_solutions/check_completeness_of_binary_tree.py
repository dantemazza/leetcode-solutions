# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        if not root:
            return True
        deque = [root]
        l = 0
        dequel = 1
        while(dequel == pow(2,l)): 
            dequel = 0
            for i in range(pow(2, l)):
                if deque[0].left:
                    dequel += 1
                deque.append(deque[0].left)
                if deque[0].right:
                    dequel += 1
                deque.append(deque[0].right)
                del deque[0]
            l += 1
        
        nullaz = False
        for i in deque:
            if i:
                if i.left or i.right or nullaz:
                    return False
            else:
                nullaz = True
        return True
        
