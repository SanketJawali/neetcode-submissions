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
        self.p = []
        self.findNode(root, subRoot.val)
        found = False
        for node in self.p:
            # print("P: ", self.p.val if self.p else None)
            found = found or self.isEqual(node, subRoot)
            if found:
                break
        return found
        
    def findNode(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root and not subRoot:
            return
        if root.val == target:
            print("Found subRoot root in Root")
            self.p.append(root)
        left = self.findNode(root.left, target) if root.left else None
        right = self.findNode(root.right, target) if root.right else None

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
        
        print(root.val, subRoot.val)
        if root.val != subRoot.val:
            return False
        
        left = self.isEqual(root.left, subRoot.left)
        right = self.isEqual(root.right, subRoot.right)

        return left and right