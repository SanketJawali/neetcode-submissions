class Solution:
    def longestPalindrome(self, s: str) -> str:
        L, R = 0, 0

        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > (R - L + 1):
                    L, R = l, r
                l, r = l - 1, r + 1
            
            l, r = i, i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > (R - L + 1):
                    L, R = l, r
                l, r = l - 1, r + 1

        return s[L:R + 1]
