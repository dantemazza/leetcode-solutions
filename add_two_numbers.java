/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        int sum = l1.val + l2.val;
        int carryOver = sum / 10;
        int currRem = sum % 10;
        ListNode nodeSum = new ListNode(currRem);
        
        ListNode curr1Node = l1.next;
        ListNode curr2Node = l2.next;
        ListNode currSum = nodeSum;
        int a = 1;
        
        while(curr1Node != null && curr2Node != null){
            sum = curr1Node.val + curr2Node.val + carryOver;
            carryOver = sum / 10;
            currRem = sum % 10;
            
            currSum.next = new ListNode(currRem);
            
            
            a++;
            currSum = currSum.next;
            curr1Node = curr1Node.next;
            curr2Node = curr2Node.next;
        }    
        ListNode currNode;
        
        if(curr1Node == null && curr2Node == null){
            if(carryOver != 0) currSum.next = new ListNode(carryOver);  
            return nodeSum;
        }
        
        if(curr1Node == null) currNode = curr2Node;
        else currNode = curr1Node;
        
        do{
        currSum.next = new ListNode((currNode.val + carryOver)%10);
        carryOver = (currNode.val + carryOver) / 10;
        currSum = currSum.next;
        currNode = currNode.next;
        }while(currNode != null);

        if(carryOver != 0) currSum.next = new ListNode(carryOver);
        
      return nodeSum;  
    }
}
