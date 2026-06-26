# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: return ""
        # Convert the tree into a list
        nodes = []
        queue = deque([root])
        while len(queue) > 0:
            lenNodes = len(queue)
            for _ in range(lenNodes):
                node = queue.popleft()
                if node is not None:
                    nodes.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    nodes.append("null")
        # Trim the None values at end
        while nodes[-1] == "null":
            nodes.pop()
        
        # convert the list into a string
        final = ""

        # Use '#' to seperate data.
        # Syntax: [Number of nodes]#[Value 1 len]#[value1]#[value 2 len]#[value2]...
        # example: 3#2#10#2#20#1#5
        # Prefix the string with the length of the list (number of nodes)
        # Use length and separators to split the string
        final += (str(len(nodes)) + "#")

        for i, node in enumerate(nodes):
            l = len(str(node))
            # block = str(l) + "#" + str(node) + "#"
            block = str(node) + "#"
            final += block
        return final

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 0: return None

        # Get the total length, i.e., number of nodes
        split = data.split("#", 1)
        lenNodes, data = int(split[0]), split[1]

        nodes = deque([])
        # for each node, get the node value
        for _ in range(lenNodes):
            split = data.split("#", 1)
            val, data = split[0], split[1]
            val = None if val == "null" else int(val)
            nodes.append(val)

        # Build the tree
        head = None
        level = deque([])
        l = 0

        while len(nodes) > 0:
            for _ in range(2 ** l):
                if len(nodes) == 0: break
                left = right = None
                # print(nodes, level)

                if nodes[0] is not None:
                    left = TreeNode(val=nodes.popleft())
                else:
                    nodes.popleft()
                level.append(left)
                if not head and left:
                    head = left
                    continue

                if len(nodes) > 0:
                    if nodes[0] is not None:
                        right = TreeNode(val=nodes.popleft())
                    else:
                        nodes.popleft()
                    level.append(right)
                
                # if left: print("l: ", left.val, end=" ") 
                # else: print(None, end=" ")
                # if right: print("r: ", right.val, end=" ") 
                # else: print(None, end=" ")

                parent = level.popleft()
                # if parent: print("parent: ", parent.val) 
                # else: print("no parent")

                while not parent and len(level) > 0:
                    parent = level.popleft()
                if parent:
                    parent.left = left
                    parent.right = right
            l += 1

        return head