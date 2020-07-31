# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        p_q = []
        for index, node in enumerate(lists):
            if node:
                heappush(p_q, (node.val, index))
        
        head = ListNode()
        res = head
        while p_q:
            val, i = heappop(p_q)
            head.next = ListNode(val)
            head = head.next
            if lists[i] and lists[i].next:
                lists[i] = lists[i].next
                heappush(p_q, (lists[i].val, i))
        return res.next
             
            
