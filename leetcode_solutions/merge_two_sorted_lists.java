/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        
        if(l1 == null) return l2;
        else if(l2 == null) return l1;
        
        
        ListNode curr1Node = l1;
        ListNode curr2Node = l2;
        ListNode result = new ListNode((curr1Node.val > curr2Node.val) ? curr2Node.val : curr1Node.val);
        ListNode resultPtr = result;
        if(curr1Node.val > curr2Node.val){
            curr2Node = curr2Node.next;
        }else{
            curr1Node = curr1Node.next;
        }
        
        while(curr1Node  != null && curr2Node != null){
          if(curr1Node.val > curr2Node.val){
              result.next = new ListNode(curr2Node.val);
              curr2Node = curr2Node.next;
          }else{
              result.next = new ListNode(curr1Node.val);
              curr1Node = curr1Node.next;
          }
            
           result = result.next; 
        }
        
        result.next = (curr1Node == null) ? curr2Node : curr1Node;
        
        //when one of them goes null, the result can point to the one that isnt null
        
        
        
        return resultPtr;
    }
}
