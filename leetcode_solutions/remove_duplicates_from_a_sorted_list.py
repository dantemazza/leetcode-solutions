# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        while True:
            if not curr:
                return head
            if not curr.next:
                return head  
            if curr.val == curr.next.val:
                if curr.next.next:
                    temp = curr.next.next
                    del curr.next
                    curr.next = temp
                else:
                    del curr.next
                    curr.next = None
                    return head
            if curr.next.val != curr.val:   
                curr = curr.next
        return head
                
