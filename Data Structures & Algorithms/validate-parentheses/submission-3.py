class Solution:
    def isValid(self, s: str) -> bool:
        # Basically s should be a palindrome
        # if every character matches to its pair then return true, else false

        # creating a dict to define the pairs of brackets
        pairs = {
            "[": "]",
            "{": "}",
            "(": ")",
        }

        stack = []

        for b in s:
            if b in pairs.keys():
                stack.append(b)
            else:
                if len(stack) > 0:
                    last = stack.pop()
                else:
                    return False
                if not pairs[str(last)] == str(b):
                    return False
        if not len(stack) == 0:
            return False
        return True