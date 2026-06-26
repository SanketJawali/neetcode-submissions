# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.goods = 0
        self.dfs(root, root.val, root.val)
        return self.goods
    
    def dfs(self, root: TreeNode, rootval: int, currmax: int):
        if not root:
            return
        # if not root.left and not root.right:
        if root.val >= rootval and root.val >= currmax:
            # print("Good: ", root.val)
            self.goods += 1
        if root.val > currmax: currmax = root.val
        left = self.dfs(root.left, rootval, currmax)
        right = self.dfs(root.right, rootval, currmax)

        return