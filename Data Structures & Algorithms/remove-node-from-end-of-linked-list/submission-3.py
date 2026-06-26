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
        a, b = head, head

        # a goes fist and counts the length
        while a:
            length += 1
            a = a.next
        
        steps = length - n
        # print(steps)
        
        if steps == 0:
            head = b.next
        else:
            for _ in range(steps - 1):
                b = b.next
                steps -= 1
        
        b.next = b.next.next if b.next else None
        return head