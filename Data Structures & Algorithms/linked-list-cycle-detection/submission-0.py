# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Use 2 pointers
        # fist moves one step at a time
        # second moves 2 steps at a time
        # if pointers meet at any moment then there is a loop
        # if second pointer reaches null, there is no loop

        if head is None:
            return False
        slow, fast = head, head.next

        while fast is not None:
            slow = slow.next
            fast = fast.next.next if fast.next is not None else fast.next
            if slow == fast:
                return True
        
        return False
        