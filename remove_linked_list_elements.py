# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        curr = head
        if not curr:
            return curr
        while curr and curr.val == val:
            curr = curr.next
        if not curr:
            return curr
        head = curr
        prev = curr
        res = prev
        curr = curr.next
        dup = True
        while dup:
            dup = False
            while curr:
                if curr.val == val:
                    prev.next = curr.next
                    dup = True
                prev = curr
                curr = curr.next
            curr = head
            
        return res
