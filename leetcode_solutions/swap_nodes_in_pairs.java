/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode result = head;
        ListNode resultRet = result;
        while(result != null){
            if(result.next == null) break;
           int val1, val2;
            val1 = result.next.val;
            val2 = result.val; 
            result.val = val1;
            result.next.val = val2; 
            result = result.next.next;
        }
        
        
        return resultRet;
    }
}
