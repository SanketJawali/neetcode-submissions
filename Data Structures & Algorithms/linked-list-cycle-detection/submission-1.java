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
    public boolean hasCycle(ListNode head) {
        if (head == null) {
            return false;
        }

        ListNode s = head;
        ListNode f = head.next;

        while (f != null) {
            if (s == f) {
                return true;
            }

            s = s.next;
            f = f.next != null ? f.next.next : null;
        }
        return false;
    }
}
