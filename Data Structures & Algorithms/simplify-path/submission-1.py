class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")

        stack = []
        for d in path:
            # Append valid directories to stack
            # Pop for ".."
            # Ignore "" and "."
            if d == "" or d == ".": continue
            elif d == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(d)
        return "/" + "/".join(stack)