class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []
        # case in-sensitive, so convert to lower case
        s = s.lower()
        s = s.replace(" ", "")
        print(f"Processed str: {s}")

        tmp = "".join(char for char in s if char.isalnum())
        s = tmp
        print(f"Processed str: {s}")

        if len(s) % 2 == 1: # remove middle most char if odd length
            x = int(len(s) // 2)
            s = s[:x] + s[x + 1:]
        
        print(f"Processed str: {s}, len: {len(s)}")
        for i in range(0, int(len(s) / 2)):
            if not s[i].isalnum():
                continue
            stack.append(s[i])
        
        print(f"stack: {stack}")

        for i in range(int(len(s) / 2), len(s)):
            if not s[i].isalnum():
                continue
            if not stack.pop() == s[i]:
                return False
            
        return True if len(stack) == 0 else False
