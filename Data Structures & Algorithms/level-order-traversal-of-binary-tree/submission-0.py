# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        res = []
        level = []
        while len(queue) > 0:
            q = list(queue)
            queue.clear()
            for node in q:
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            print(queue, res, level)
            res.append(list(level))
            level.clear()

        return res