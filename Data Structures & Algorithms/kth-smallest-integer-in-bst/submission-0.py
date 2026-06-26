# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        res = self.dfs(root)
        if res: return res.val
        return -1

    def dfs(self, node: TreeNode) -> Optional[TreeNode]:
        if not node:
            return None

        left = self.dfs(node.left)
        self.k -= 1
        if self.k == 0:
            return node
        right = self.dfs(node.right)

        if left: return left
        if right: return right
        return None