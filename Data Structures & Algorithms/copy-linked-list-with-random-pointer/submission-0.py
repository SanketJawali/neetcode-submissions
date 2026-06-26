"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        
        indexes = {}    # A map of original list node to it's index
        copynodes = {}  # Map to keep association between memory location and list index

        # Create the indexes map
        p = head
        i = 0
        while p is not None:
            indexes[p] = i
            p = p.next
            i += 1
        
        # Create the copylist without the randoms
        # Also create the copynodes to map each index to it's node
        copylist = Node(x=head.val)
        a, b = head.next, copylist
        i = 1
        copynodes[0] = copylist
        while a is not None:
            newNode = Node(x=a.val)
            b.next = newNode
            b = b.next
            
            copynodes[i] = newNode
            i += 1
            a = a.next

        # Add the randoms in copylist
        a, b = head, copylist
        while a is not None:
            if a.random and b:
                # print(f"Random ptr found, {a.val} -> {indexes[a.random].val}")
                b.random = copynodes[indexes[a.random]]

            a = a.next
            b = b.next if b is not None else b
        
        print("copy list:")
        self.printList(copylist)
        return copylist

    # Function to print a linkedlist
    def printList(self, head):
        if not head:
            print(head)
        
        indexes = {}    # A map of original list node to it's index
        copynodes = {}  # Map to keep association between memory location and list index

        p = head
        i = 0
        while p is not None:
            indexes[p] = i
            p = p.next
            i += 1
        
        a = head
        while a is not None:
            if a.random is not None:
                print(f"[{a.val}, {indexes[a.random]}] -> ", end='')
            else:
                print(f"{a.val} -> ", end='')
            
            a = a.next
        print()
