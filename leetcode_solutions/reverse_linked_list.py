# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        prev = None 
        post = curr
        while curr:
            post = curr.next
            curr.next = prev
            prev = curr
            curr = post
        
        return prev
        
