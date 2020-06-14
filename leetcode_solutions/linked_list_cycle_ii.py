# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        amap = {}
        curr = head
        while curr:
            if amap.get(curr):
                return curr
            amap[curr] = True
            curr = curr.next
               
        return None
