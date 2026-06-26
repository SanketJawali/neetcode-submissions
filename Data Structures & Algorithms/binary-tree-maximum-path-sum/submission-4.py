# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # For current node, check left path and right path
        # If leftpath sum > 0 add it to a current path sum
        # If rightpath sum > 0 add it to the current path sum
        # return the max currentpath sum
        # keep track of a current path sum variable
        # keep track of a global max path sum
        if not root: return 0
        if not root.left and not root.right: return root.val

        self.maxPathSum = float("-infinity")
        self.dfs(root)
        return self.maxPathSum

    def dfs(self, root: TreeNode) -> int:
        if not root: return 0
        pathsum = root.val
        
        leftpath = self.dfs(root.left)
        rightpath = self.dfs(root.right)

        # print("root, l, r: ", root.val, leftpath, rightpath)
        pathsum += leftpath if leftpath > 0 else 0
        pathsum += rightpath if rightpath > 0 else 0
        
        if self.maxPathSum < pathsum:
            self.maxPathSum = max(self.maxPathSum, pathsum)

        if leftpath < 0 and rightpath < 0: return root.val
        return max(leftpath + root.val, rightpath + root.val)