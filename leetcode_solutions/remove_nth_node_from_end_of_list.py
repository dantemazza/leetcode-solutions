# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        amap = {}
        curr = head
        i = 0
        while curr:
            amap[i] = curr
            curr = curr.next
            i += 1
        if n == i:
            return head.next
        curr = amap[i-n]
        amap[i-n-1].next = amap[i-n].next
        return head
