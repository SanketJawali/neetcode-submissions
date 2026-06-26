# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        if not head.next: return head

        a, b, c = head, head.next, head.next.next
        a.next = None
        while b is not None:
            b.next = a
            a, b = b, c
            c = c.next if c else None
        head = a
        return head