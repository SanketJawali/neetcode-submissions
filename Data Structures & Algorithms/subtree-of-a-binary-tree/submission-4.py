# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root and subRoot is not None:
            return False
        if root is not None and not subRoot:
            return False
        self.p = None
        self.found = False
        self.findNode(root, subRoot)
        return self.found
        
    def findNode(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root and not subRoot:
            return
        target = subRoot.val
        if root.val == target:
            # print("Found subRoot root in Root")
            if self.isEqual(root, subRoot):
                self.found = True
                return root
        left = self.findNode(root.left, subRoot) if root.left else None
        right = self.findNode(root.right, subRoot) if root.right else None

        if not left and not right:
            return
        return left if left else right

    def isEqual(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root and subRoot is not None:
            return False
        if root is not None and not subRoot:
            return False
        
        # print(root.val, subRoot.val)
        if root.val != subRoot.val:
            return False
        
        left = self.isEqual(root.left, subRoot.left)
        right = self.isEqual(root.right, subRoot.right)

        return left and right