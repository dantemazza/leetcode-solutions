# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        amap = {}
        node = head
        a = 0
        if not node:
            return False
        while node.next:
            amap[node] = True
            a += 1
            node = node.next
            if node in amap:
                return True
            
        return False
