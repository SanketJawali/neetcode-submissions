class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for i, c in enumerate(s):
            if c != ']':
                stack.append(c)
                continue
            
            # Find encoded string within []
            encoded = ""
            while stack and stack[-1] != '[':
                encoded = stack.pop() + encoded
            stack.pop() # Pop '['

            # Find multiplier k
            k = ""
            while stack and stack[-1].isdigit():
                k = stack.pop() + k
            k = int(k)

            for _ in range(int(k)):
                stack.append(encoded)
        
        return "".join(stack)