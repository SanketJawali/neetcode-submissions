class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 1: return ""

        # Initialize the first string as longest prefix
        prefix = strs[0]

        for s in strs:
            # Check if prefix is prefix of strs
            if prefix in s:
                continue
            # If not then remove one character from the prefix and check again
            while not prefix in s:
                if len(prefix) < 1: return ""
                prefix = prefix[:len(prefix) - 1]
        
        return prefix