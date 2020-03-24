# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        return self.reverseK(head, k)
    def reverseK(self, head, k):
        if not head:
            return None
        prev = None
        curr = head
        post = curr
        end = None
        for i in range(k):
            if not curr:
                return self.reverseK(prev, i)
            post = curr.next
            curr.next = prev
            prev = curr
            curr = post
        head.next = self.reverseK(curr, k)
        return prev
