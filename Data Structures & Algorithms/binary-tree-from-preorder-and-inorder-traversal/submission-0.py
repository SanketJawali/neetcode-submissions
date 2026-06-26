# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.indices = None

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) < 1 or len(inorder) < 1: return None

        root = preorder[0]
        node = TreeNode(val=root)

        division = self.divideList(inorder, root)

        leftPreorder = preorder[1:len(division[0])+1]
        rightPreorder = preorder[len(division[0])+1:]

        node.left = self.buildTree(leftPreorder, division[0])
        node.right = self.buildTree(rightPreorder, division[1])
        return node

    def divideList(self, inorder: List[int], key: int) -> List[List[int]]:
        result = []
        keyIdx = inorder.index(key)
        result.append(inorder[:keyIdx])
        result.append(inorder[keyIdx+1:])
        return result
