# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = num2 = 0

        power = 0
        p = l1  # pointer to iterate through l1

        while p is not None:
            num1 += p.val * (10 ** power)
            power += 1
            p = p.next
        
        power = 0
        p = l2

        while p is not None:
            num2 += p.val * (10 ** power)
            power += 1
            p = p.next

        res = str(num1 + num2)  # convert res to str for easier access of individual nums
        resultList = None

        for n in res[::-1]:
            if resultList is None:
                print("n: ", n)
                resultList = ListNode(val=int(n))
                p = resultList
                continue
            newNode = ListNode(val=int(n))
            p.next = newNode
            p = p.next
        
        return resultList