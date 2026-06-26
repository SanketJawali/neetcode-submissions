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

        self.maxDiameter = 0
        self.dfs(root)

        return self.maxDiameter
    
    def dfs(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        currentDiameter = left + right
        self.maxDiameter = max(self.maxDiameter, currentDiameter)

        return 1 + max(left, right)