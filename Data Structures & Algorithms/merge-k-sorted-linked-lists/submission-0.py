# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heapify, heappop, heappush, heapreplace

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        current = []
        heapify(current)
        head = tail = None
        for l in lists:
            self.printList(l)

        for i, node in enumerate(lists):
            heappush(current, (node.val, i, node))
        
        while len(current) > 0:
            # Get min
            _, i, p = current[0]
            # point tail.next to min node, new tail is min node
            if not head: head = p
            if not tail: tail = p
            # update current heap, replace current min with node next to min
            if p.next is None:
                heappop(current)
            else:
                heapreplace(current, (p.next.val, i, p.next))
            # if next of current min is None, just pop and don't add
            tail.next = p
            tail = p

        self.printList(head)
        return head
    
    def printList(self, head):
        p = head
        while p is not None:
            print(f"{p.val} -> ", end="")
            p = p.next
        print("None")