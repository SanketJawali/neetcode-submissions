# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head
        a1 = list1
        b1 = list2

        while a1 is not None and b1 is not None:
            if a1.val <= b1.val:
                current.next = a1
                a1 = a1.next
            else:
                current.next = b1
                b1 = b1.next
            
            current = current.next
        
        if a1 is None and b1 is not None:
            current.next = b1
        elif b1 is None and a1 is not None:
            current.next = a1
        
        return head.next