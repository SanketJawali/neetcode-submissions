# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heapify, heappop, heappush, heapreplace

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # for l in lists:
        #     self.printList(l)

        if len(lists) == 0:
            return
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            return self.mergeTwoLists(lists[0], lists[1])
        
        head = None
        for i in range(1, len(lists)):
            if head is None:
                head = self.mergeTwoLists(lists[i - 1], lists[i])
                continue
            head = self.mergeTwoLists(head, lists[i])
        return head

    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        head, tail = None, ListNode()    # Dummy node
        l1, l2 = list1, list2
        while tail is not None:
            if l1 is None and l2 is None:
                break

            # Compare the nodes and get the smaller one
            small = l1 if l1 is not None else l2

            if small == l1 and l2 is not None and l2.val < l1.val:
                small = l2

            # Update head, tail and add node
            # Move l1 and l2
            if not head:
                head = small
            tail.next = small
            tail = tail.next
            if small == l1 and l1 is not None:
                l1 = l1.next
            elif small == l2 and l2 is not None:
                l2 = l2.next
        # print("Sorting list pair: ")
        # self.printList(head)
        return head

    def printList(self, head: ListNode) -> None:
        p = head
        while p is not None:
            print(f"{p.val} -> ", end="")
            p = p.next
        print("None")