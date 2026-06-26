# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        head = ListNode()
        current = head

        a1 = list1
        a2 = list1.next if a1 else None

        b1 = list2
        b2 = list2.next if b1 else None
        
        first = True
        while a1 is not None and b1 is not None:
            aSb = True

            if a1.val <= b1.val:
                current.next = a1
                if first:
                    head = a1
            else:
                current.next = b1
                aSb = False
                if first:
                    head = b1

            if aSb:
                a1 = a2
                a2 = a2.next if a2 else None
            else:
                b1 = b2
                b2 = b2.next if b2 else None
            
            first = False

            current = current.next if current else None
        
        if a1 is None and b1 is not None:
            current.next = b1
        elif b1 is None and a1 is not None:
            current.next = a1
        
        return head