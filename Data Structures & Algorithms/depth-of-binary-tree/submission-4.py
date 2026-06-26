# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
        
    #     # Using DFS we can keep track of max depth
    #     currentDepth = 0
    #     maxDepth = 0

    #     stack = []
    #     p = root

    #     while p is not None:
    #         currentDepth += 1
    #         maxDepth = max(currentDepth, maxDepth)
    #         # print(p.val, currentDepth, stack)
            
    #         if p.left and p.right:
    #             stack.append((p.right, currentDepth))
    #         elif p.right:
    #             p = p.right
    #             continue
    #         elif not p.left and not p.right:
    #             if len(stack) > 0:
    #                 p, currentDepth = stack.pop()
    #                 continue
    #         p = p.left
                
    #     return maxDepth
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))