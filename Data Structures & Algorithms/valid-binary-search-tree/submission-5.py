# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.dfs(root, float("-inf"), float("inf"))

    def dfs(self, root: TreeNode, low: int, high: int) -> bool:
        if not root:
            return True
        
        if root.val >= high or root.val <= low:
            return False

        if root.left and root.left.val >= root.val:
            return False
        if root.right and root.right.val <= root.val:
            return False
        
        left = self.dfs(root.left, low, root.val)
        right = self.dfs(root.right, root.val, high)

        return left and right