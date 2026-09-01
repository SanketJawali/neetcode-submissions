class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                # Skip one character and check for valid palindrome for rest of s
                return palindrome(l + 1, r) or palindrome(l, r - 1)
            l += 1
            r -= 1

        return True