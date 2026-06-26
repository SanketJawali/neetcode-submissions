# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next and n == 1:
            head = None
            return
        
        length = 0
        dummy = ListNode(next=head)
        a, b = head, dummy

        for _ in range(n):
            a = a.next
        while a:
            a = a.next
            b = b.next
        
        if b == dummy:
            head = head.next

        b.next = b.next.next

        return head