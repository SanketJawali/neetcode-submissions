/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if (head == null || head.next == null || left == right) {
            return head;
        }

        ListNode a = null;
        ListNode b = head;
        ListNode c = head.next;
        int bidx = 1;    // Tracks index of b ptr

        while (bidx < left) {
            a = b;
            b = c;
            c = c.next;
            bidx++;
        }

        ListNode l = a;
        ListNode r = b;
        while (bidx <= right) {
            b.next = a;

            a = b;
            b = c;
            c = c != null ? c.next : null;
            bidx++;
        }
        r.next = b;
        if (left > 1) 
            l.next = a;
        else
            head = a;
        
        return head;
    }
}