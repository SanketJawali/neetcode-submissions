class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        for i in range(len(strs[0])):
            c = strs[0][i]
            for s in strs:
                if len(s) - 1 < i:
                    return prefix
                if s[i] != c:
                    return prefix
            prefix += c
                
        return prefix