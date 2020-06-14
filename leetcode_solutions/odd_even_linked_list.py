# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        odd = head
        res = odd
        even = head.next
        evenhead = even
        while even and odd and even.next:
            odd.next = even.next
            even.next = even.next.next
            odd = odd.next
            even = even.next

            
        odd.next = evenhead
        return res
            
