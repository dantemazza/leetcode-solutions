# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        curA = headA
        curB = headB
        Amap = {}
        while curA:
            Amap[curA] = True
            curA = curA.next
            
        while curB and not Amap.get(curB):
            curB = curB.next
        
        return curB
