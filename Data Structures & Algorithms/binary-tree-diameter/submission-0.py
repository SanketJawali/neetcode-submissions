# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        maxPath = 0
        currentPath = 0
        queue = deque([root])
        node = root

        while node is not None and len(queue) > 0:
            # Implement a BFS
            node = queue.popleft()

            if node.left is not None: queue.append(node.left)
            if node.right is not None: queue.append(node.right)

            currentPath = self.maxDepth(node.left) + self.maxDepth(node.right)
            maxPath = max(currentPath, maxPath)

        return maxPath 
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
