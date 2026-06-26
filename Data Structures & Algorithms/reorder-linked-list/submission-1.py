# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        if not fast:
            return

        # Find the mid point of the list
        while fast is not None:
            slow = slow.next
            fast = fast.next.next if fast.next is not None else fast.next

        # invert the list direction after the mid section
        b = slow.next
        c = slow.next.next if b is not None else None
        tail = ListNode()

        while b is not None:
            b.next = slow
            if not c:
                tail = b
                break
            slow = b
            b = c
            c = c.next

        # Re-arrange
        # use 2 pointers h and t
        # h will iterate through list of head-mid; t iterate through tail-mid
        h, t = head, tail
        while True:
            hnext = h.next
            tnext = t.next

            h.next = t
            t.next = hnext

            h = hnext
            t = tnext
            if h == t:
                t.next = None
                break
            if h.next == t:
                t.next = None
                break