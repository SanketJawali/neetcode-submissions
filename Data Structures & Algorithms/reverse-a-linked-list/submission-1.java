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
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode a = head;
        ListNode b = a.next;
        ListNode c = b.next;

        a.next = null;
        while (a != null && b != null) {
            b.next = a;

            a = b;
            b = c;
            c = c == null ? null : c.next;
        }
        return a;
    }
}
