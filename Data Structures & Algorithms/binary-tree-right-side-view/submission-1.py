# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        queue = deque([root])
        result = []

        while len(queue) > 0:
            l = len(queue)
            right = None
            for _ in range(l):
                node = queue.popleft()
                right = node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(right)

        return result
            