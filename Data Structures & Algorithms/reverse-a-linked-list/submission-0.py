# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # We can use 3 pointers a, b and c
        # initially: a -> b -> c -> ...
        # step: a <- b - c -> ...
        # step: move all 3 to next node
        # <- a - b -> c -> ... (here make 'b' point to 'a')
        # If b == c: we are at the end

        a = head
        
        tail = a
        b = a.next if a else None
        c = b.next if b else None

        first = True
        
        while a and a.next is not None:
            b.next = a
            tail = b

            if first:
                a.next = None
                first = not first
            
            if not c:
                break

            a = b
            b = c
            c = c.next

        return tail