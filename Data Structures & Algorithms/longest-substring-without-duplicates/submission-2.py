from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l, r = 0, 0
        chars = defaultdict(int)

        for r in range(len(s)):
            chars[s[r]] += 1
            while r >= l and chars[s[r]] > 1:
                # Shrink the window to remove the repeated char
                chars[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            
        return res