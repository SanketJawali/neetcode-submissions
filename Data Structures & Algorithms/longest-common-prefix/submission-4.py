class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        # Consider first word is current prefix, find all the common chars one by one
        # for each char in the first string
        for i in range(len(strs[0])):
            for s in strs[1:]:
                if len(s) <= len(prefix): return prefix
                if not strs[0][i] == s[i]:
                    return prefix
            prefix += strs[0][i]
        
        return prefix