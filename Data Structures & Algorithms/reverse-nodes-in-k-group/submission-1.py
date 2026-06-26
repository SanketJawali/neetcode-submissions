# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Start from head, check if there are k nodes in the list at least
        # If there aren't k nodes, do not reverse
        # If yes, reverse a sublist of k length; perform k reversals
        # Update head, set a tail pointer
        # After performing k flips, set the previous tail.next to middle pointer

        if not head: return None
        if head.next is None: return head
        if k == 1: return head  # Assuming that k == 1 doesn't change the list

        newHead = prevTail = nextGroup = tail = None
        group = head

        # While there are k nodes in list
        while True:
            # if not newHead: self.printList(head)
            # else: self.printList(newHead)
            # print("prevTail, nextGroup: ", prevTail, nextGroup)

            tail = self.getTail(group, k)
            if tail is None or group is None:
                break
            nextGroup = tail.next

            # Reverse k nodes
            reversedList = self.reverseList(group, tail, k)
            reverseHead, reverseTail = reversedList[0], reversedList[1]
            if not newHead:
                newHead = reverseHead
            reverseTail.next = nextGroup
            if prevTail:
                prevTail.next = reverseHead
            prevTail = reverseTail
            group = nextGroup
            
        return newHead

    def reverseList(self, head: ListNode, tail: ListNode, k: int) -> List[ListNode]:
        a, b, c = head, head.next, head.next.next

        for _ in range(k):
            if not b or a == tail:
                break

            # Flip the pointer
            b.next = a
            # Move pointer to next
            a, b = b, c
            c = c.next if c else None

        return [tail, head]

    def getTail(self, node: ListNode, k: int) -> Optional[ListNode]:
        if not node: return None
        for _ in range(k - 1):
            node = node.next
            k -= 1
            if node is None:
                return None
        return node
    
    def printList(self, node: ListNode) -> None:
        while node and node.next is not None:
            print(f"{node.val} -> ", end="")
            node = node.next
        print(None)