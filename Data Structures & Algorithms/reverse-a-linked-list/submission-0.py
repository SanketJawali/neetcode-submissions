# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        a, b, c = head, head.next, head.next.next

        a.next = None   # Tail of updated LinkedList
        while a and b:
            b.next = a

            a = b
            b = c
            c = c.next if c else None
        
        return a