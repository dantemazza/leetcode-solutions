# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        if root:
            self.stack.append(root)
            while self.stack[-1].left:
                self.stack.append(self.stack[-1].left)
        

    def next(self) -> int:
        node = self.stack.pop()
        res = node.val
        if node.right:
            self.stack.append(node.right)
            while self.stack[-1].left:
                self.stack.append(self.stack[-1].left)
        return res
            
        """
        @return the next smallest number
        """
        

    def hasNext(self) -> bool:
        return self.stack
        """
        @return whether we have a next smallest number
        """
        
    

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
